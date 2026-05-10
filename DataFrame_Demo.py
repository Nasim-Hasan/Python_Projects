import pandas as pd

# Sample data
df = pd.DataFrame({
    "name": ["A", "B", "C", "D", "E", "F"],
    "score": [10, 20, 30, 40, 50, 60]
})

print(df.head())        # First 5 rows (default)
print(df.head(3))       # First 3 rows
print(df.head(-2))      # All rows except the last 2
print(df.iloc[:3])      # Equivalent to head(3)
print(df.tail())        # Last 5 rows (default)
print(df.tail(2))       # Last 2 rows