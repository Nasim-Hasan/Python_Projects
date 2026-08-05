#pip install -q pandas scikit-learn streamlit joblib requests
import pandas
import sklearn
import streamlit 
import streamlit as st
import joblib
import requests
import pandas as pd
import numpy as np
import subprocess
import sys
import time
import webbrowser
from pathlib import Path
from collections import defaultdict
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

print(pandas.__version__)
print(sklearn.__version__)
print(streamlit.__version__)
print(joblib.__version__)
print(requests.__version__)

# Create data directory if it doesn't exist
Path("data").mkdir(exist_ok=True)

csv_path = Path("results.csv")

# Download only if the file doesn't already exist
if not csv_path.exists():
    url = "https://raw.githubusercontent.com/academic-initiative/skillsbuild/main/ai-in-sports/football-predictor/data/results.csv"
    response = requests.get(url)
    response.raise_for_status()
    csv_path.write_bytes(response.content)
    print("Downloaded results.csv")
else:
    print("results.csv already exists, skipping download.")

# Load into DataFrame
matches = pd.read_csv(csv_path)
matches["date"] = pd.to_datetime(matches["date"])

print("Shape:", matches.shape)
print("Date range:", matches["date"].min(), "→", matches["date"].max())
matches.head(3)

# --- Top 10 most frequent tournaments ---
print("Top 10 tournaments by match count:")
print(matches["tournament"].value_counts().head(10).to_string())

# --- Top 15 teams by total matches played ---
print("\nTop 15 teams by total matches played:")
team_counts = (
    pd.concat([matches["home_team"], matches["away_team"]])
    .value_counts()
    .head(15)
)
print(team_counts.to_string())

# --- Matches per decade ---
print("\nMatches per decade:")
decade = (matches["date"].dt.year // 10 * 10).rename("decade")
decade_counts = decade.value_counts().sort_index()
for d, count in decade_counts.items():
    print(f"  {d}s: {count}")

MAJOR_TOURNAMENTS = {
    "Soccer World Cup",
    "Soccer World Cup qualification",
    "UEFA Euro",
    "UEFA Euro qualification",
    "Copa América",
    "African Cup of Nations",
}

# Helper functions — operate on a list of (goals_for, goals_against, won) tuples
def winrate(hist):
    return sum(h[2] for h in hist) / len(hist) if hist else 0.5

def goal_avg(hist):
    return sum(h[0] for h in hist) / len(hist) if hist else 1.0

def recent_form(hist):
    last10 = hist[-10:]
    return sum(h[2] for h in last10) / 10 if len(last10) == 10 else 0.5

# Filter to 1990-onwards and sort chronologically
filtered = (matches[matches["date"] >= pd.to_datetime("1990-01-01")])

team_history = defaultdict(list)  # team -> [(goals_for, goals_against, won), ...]
rows = []

for _, row in filtered.iterrows():
    home, away = row["home_team"], row["away_team"]
    h_hist = team_history[home]
    a_hist = team_history[away]

    # --- Compute features from history BEFORE this match ---
    feat = {
        "date": row["date"],
        "home_team": home,
        "away_team": away,
        "team_a_winrate": winrate(h_hist),
        "team_b_winrate": winrate(a_hist),
        "team_a_goal_avg": goal_avg(h_hist),
        "team_b_goal_avg": goal_avg(a_hist),
        "team_a_recent_form": recent_form(h_hist),
        "team_b_recent_form": recent_form(a_hist),
        "is_neutral": int(row["neutral"]),
        "is_major_tournament": int(row["tournament"] in MAJOR_TOURNAMENTS),
    }

    # Outcome: 0 = home win, 1 = draw, 2 = away win
    hs, as_ = row["home_score"], row["away_score"]
    feat["outcome"] = 0 if hs > as_ else (1 if hs == as_ else 2)
    rows.append(feat)

    # --- Update history AFTER computing features (no leakage) ---
    home_won = int(hs > as_)
    away_won = int(as_ > hs)
    team_history[home].append((hs, as_, home_won))
    team_history[away].append((as_, hs, away_won))

features_df = pd.DataFrame(rows)

print(features_df.shape)
features_df.head(3)

feature_cols = [
    "team_a_winrate",
    "team_b_winrate",
    "team_a_goal_avg",
    "team_b_goal_avg",
    "team_a_recent_form",
    "team_b_recent_form",
    "is_neutral",
    "is_major_tournament",
]

# Time-based split: train < 2018-01-01, test >= 2018-01-01
cutoff = pd.Timestamp("2018-01-01")
train_df = features_df[features_df["date"] < cutoff]
test_df  = features_df[features_df["date"] >= cutoff]

X_train = train_df[feature_cols]
X_test  = test_df[feature_cols]
y_train = train_df["outcome"]
y_test  = test_df["outcome"]

print("X_train shape:", X_train.shape)
print("X_test  shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test  shape:", y_test.shape)
print()
print("y_train class distribution:")
print(pd.Series(y_train).value_counts(normalize=True).sort_index().round(3).to_string())

# Train
model = RandomForestClassifier(n_estimators=200, max_depth=12, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Test accuracy
acc = accuracy_score(y_test, y_pred)
print(f"Test accuracy: {acc * 100:.2f}%")

# Baseline: always predict the most frequent class in y_train
most_frequent = np.bincount(y_train).argmax()
baseline_acc = accuracy_score(y_test, np.full(len(y_test), most_frequent))
print(f"Baseline accuracy (most frequent class): {baseline_acc * 100:.2f}%")

# Confusion matrix
labels = [0, 1, 2]
label_names = ["Home win", "Draw", "Away win"]
cm = confusion_matrix(y_test, y_pred, labels=labels)
header = f"{'':12s}" + "".join(f"{n:>12s}" for n in label_names)
print("\nConfusion matrix (rows=actual, cols=predicted):")
print(header)
for row_name, row in zip(label_names, cm):
    print(f"{row_name:12s}" + "".join(f"{v:12d}" for v in row))

# Feature importances
print("\nFeature importances (descending):")
importances = model.feature_importances_
sorted_idx = np.argsort(importances)[::-1]
for i in sorted_idx:
    print(f"  {feature_cols[i]:35s} {importances[i]:.4f}")

# --- Step 1: Create models/ directory ---
Path("models").mkdir(exist_ok=True)

# --- Build the set of Soccer World Cup qualification teams ---
wcq = matches[matches["tournament"] == "Soccer World Cup qualification"]
soccer_teams = set(wcq["home_team"]).union(set(wcq["away_team"]))

# --- Build team_stats dictionary ---
team_stats = {}

all_teams = set(matches["home_team"]).union(set(matches["away_team"]))

for team in all_teams:
    # Skip non-Soccer-World-Cup-eligible entities
    if team not in soccer_teams:
        continue

    home_mask = matches["home_team"] == team
    away_mask = matches["away_team"] == team

    home_rows = matches[home_mask]
    away_rows = matches[away_mask]

    total_matches = len(home_rows) + len(away_rows)

    # Require at least 30 matches
    if total_matches < 30:
        continue

    # Wins: home win = home_score > away_score; away win = away_score > home_score
    home_wins = (home_rows["home_score"] > home_rows["away_score"]).sum()
    away_wins = (away_rows["away_score"] > away_rows["home_score"]).sum()
    total_wins = home_wins + away_wins

    # Goals scored
    home_goals = home_rows["home_score"].sum()
    away_goals = away_rows["away_score"].sum()
    total_goals = home_goals + away_goals

    # Recent form: last 10 matches by date
    home_records = home_rows[["date", "home_score", "away_score"]].copy()
    home_records["won"] = (home_records["home_score"] > home_records["away_score"]).astype(int)

    away_records = away_rows[["date", "home_score", "away_score"]].copy()
    away_records["won"] = (away_records["away_score"] > away_records["home_score"]).astype(int)

    all_records = pd.concat([pd.DataFrame(home_records[["date", "won"]]), pd.DataFrame(away_records[["date", "won"]])]).sort_values("date")

    last10 = all_records.tail(10)
    if len(last10) == 10:
        recent_form_val = float(last10["won"].sum() / 10)
    else:
        recent_form_val = 0.5

    team_stats[team] = {
        "winrate": float(total_wins / total_matches),
        "goal_avg": float(total_goals / total_matches),
        "recent_form": recent_form_val,
        "matches_played": int(total_matches),
    }

# --- Step 2: Save model and team data ---
joblib.dump(model, "models/match_predictor.pkl")
joblib.dump({"team_stats": team_stats, "feature_cols": feature_cols}, "models/team_data.pkl")

# --- Print summary ---
print(f"Teams stored: {len(team_stats)}")

top5 = (
    sorted(
        [(t, s) for t, s in team_stats.items() if s["matches_played"] >= 100],
        key=lambda x: x[1]["winrate"],
        reverse=True,
    )[:5]
)
print("\nTop 5 teams by win rate (≥ 100 matches):")
for team, s in top5:
    print(f"  {team:30s}  winrate={s['winrate']:.3f}  matches={s['matches_played']}")

def predict_match(team_a, team_b, is_neutral=True, is_major_tournament=True):
    """Predict match outcome probabilities for team_a vs team_b.

    Returns a dict with keys team_a_win_prob, draw_prob, team_b_win_prob.
    Training labels: 0 = team_a win, 1 = draw, 2 = team_b win.
    """
    if team_a not in team_stats:
        raise ValueError(f"Team '{team_a}' not found in team_stats. Check spelling or use a team with sufficient match history.")
    if team_b not in team_stats:
        raise ValueError(f"Team '{team_b}' not found in team_stats. Check spelling or use a team with sufficient match history.")

    stats_a = team_stats[team_a]
    stats_b = team_stats[team_b]

    row = pd.DataFrame([{
        "team_a_winrate":       stats_a["winrate"],
        "team_b_winrate":       stats_b["winrate"],
        "team_a_goal_avg":      stats_a["goal_avg"],
        "team_b_goal_avg":      stats_b["goal_avg"],
        "team_a_recent_form":   stats_a["recent_form"],
        "team_b_recent_form":   stats_b["recent_form"],
        "is_neutral":           int(is_neutral),
        "is_major_tournament":  int(is_major_tournament),
    }])

    # Guarantee column order matches training
    row = row.reindex(columns=feature_cols)

    proba = model.predict_proba(row)

    return {
        "team_a_win_prob": float(proba[0][0]),
        "draw_prob":       float(proba[0][1]),
        "team_b_win_prob": float(proba[0][2]),
    }


result1 = predict_match("Brazil", "Argentina")
print("Brazil vs Argentina:", result1)

result2 = predict_match("Germany", "Brazil")
print("Germany vs Brazil:  ", result2)

#writefile app.py
st.set_page_config(
    page_title="Soccer 2026 Match Predictor",
    page_icon="⚽",
    layout="centered",
)

@st.cache_resource
def load_artifacts():
    model = joblib.load(Path("models/match_predictor.pkl"))
    team_data = joblib.load(Path("models/team_data.pkl"))
    team_stats = team_data["team_stats"]
    feature_cols = team_data["feature_cols"]
    return model, team_stats, feature_cols


model, team_stats, feature_cols = load_artifacts()

st.title("⚽ Soccer 2026 Match Predictor")
st.caption("Predictions are based on historical international football results.")

team_names = sorted(team_stats.keys())

col1, col2 = st.columns(2)
with col1:
    default_a = team_names.index("Brazil") if "Brazil" in team_names else 0
    team_a = st.selectbox("Team A", team_names, index=default_a)
with col2:
    default_b = team_names.index("Argentina") if "Argentina" in team_names else 1
    team_b = st.selectbox("Team B", team_names, index=default_b)

is_neutral = st.checkbox("Neutral venue", value=True)
is_major = st.checkbox("Major tournament (e.g. World Cup)", value=True)

if st.button("Predict", type="primary", use_container_width=True):
    if team_a == team_b:
        st.error("Please pick two different teams.")
    else:
        stats_a = team_stats[team_a]
        stats_b = team_stats[team_b]

        row = pd.DataFrame([{
            feature_cols[0]: stats_a["winrate"],
            feature_cols[1]: stats_b["winrate"],
            feature_cols[2]: stats_a["goal_avg"],
            feature_cols[3]: stats_b["goal_avg"],
            feature_cols[4]: stats_a["recent_form"],
            feature_cols[5]: stats_b["recent_form"],
            feature_cols[6]: int(is_neutral),
            feature_cols[7]: int(is_major),
        }])

        proba = model.predict_proba(row)[0]
        p_a, p_draw, p_b = float(proba[0]), float(proba[1]), float(proba[2])

        mc1, mc2, mc3 = st.columns(3)
        mc1.metric(f"{team_a} wins", f"{p_a * 100:.1f}%")
        mc2.metric("Draw", f"{p_draw * 100:.1f}%")
        mc3.metric(f"{team_b} wins", f"{p_b * 100:.1f}%")

        st.progress(p_a, text=f"{team_a} wins")
        st.progress(p_draw, text="Draw")
        st.progress(p_b, text=f"{team_b} wins")

        comparison = pd.DataFrame(
            {
                "Win rate": [f"{stats_a['winrate']:.3f}", f"{stats_b['winrate']:.3f}"],
                "Avg goals scored": [f"{stats_a['goal_avg']:.2f}", f"{stats_b['goal_avg']:.2f}"],
                "Recent form (last 10)": [f"{stats_a['recent_form']:.1f}", f"{stats_b['recent_form']:.1f}"],
                "Matches played": [stats_a["matches_played"], stats_b["matches_played"]],
            },
            index=[team_a, team_b],
        )
        st.table(comparison)

streamlit_process = subprocess.Popen(
    [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        "app.py",
        "--server.headless",
        "true",
        "--server.port",
        "8501",
        "--browser.gatherUsageStats",
        "false",
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
)

print("Starting Streamlit server...")
time.sleep(4)

webbrowser.open("http://localhost:8501")

print("Streamlit app is running at http://localhost:8501")
print("To stop the server, run streamlit_process.terminate() in a new cell.")



