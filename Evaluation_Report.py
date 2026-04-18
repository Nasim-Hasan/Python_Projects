# =========================
# Imports
# =========================
# --- Standard library
import re
import json
# list of preferred domains for Tavily results
TOP_DOMAINS = {
# General reference / institutions / publishers
"wikipedia.org", "nature.com", "science.org", "sciencemag.org", "cell.com"
"mit.edu", "stanford.edu", "harvard.edu", "nasa.gov", "noaa.gov", "europa.eu"
# CS/AI venues & indexes
"arxiv.org", "acm.org", "ieee.org", "neurips.cc", "icml.cc", "openreview.net"
# Other reputable outlets
"elifesciences.org", "pnas.org", "jmlr.org", "springer.com", "sciencedirect.com"
# Extra domains (case-specific additions)
"pbs.org", "nova.edu", "nvcc.edu", "cccco.edu",
# Well known programming sites
"codecademy.com", "datacamp.com"
}

def evaluate_tavily_results(TOP_DOMAINS, raw: str, min_ratio=0.4):
    """
    Evaluate whether plain-text research results mostly come from preferred domains.
    Args:
    TOP_DOMAINS (set[str]): Set of preferred domains (e.g., 'arxiv.org', 'nature.com)
    raw (str): Plain text or Markdown containing URLs.
    min_ratio (float): Minimum preferred ratio required to pass (e.g., 0.4 = 40%).
    Returns:
    tuple[bool, str]: (flag, markdown_report)
    flag -> True if PASS, False if FAIL
    markdown_report -> Markdown-formatted summary of the evaluation
    """
    # Extract URLs from the text
    url_pattern = re.compile(r'https?://[^\s\]\)>\}]+', flags=re.IGNORECASE)
    urls = url_pattern.findall(raw)
    if not urls:
        return False, """### Evaluation — Tavily Preferred Domains
        No URLs detected in the provided text.
        Please include links in your research results.
        """
    # Count preferred vs total
    total = len(urls)
    preferred_count = 0
    details = []
    for url in urls:
        domain = url.split("/")[2]
        preferred = any(td in domain for td in TOP_DOMAINS)
        if preferred:
            preferred_count += 1
        details.append(f"- {url} → {' PREFERRED' if preferred else ' NOT PREFERRED'}")
    ratio = preferred_count / total if total > 0 else 0.0
    flag = ratio >= min_ratio
    # Markdown report
    report = f"""
    ### Evaluation — Tavily Preferred Domains
    - Total results: {total}
    - Preferred results: {preferred_count}
    - Ratio: {ratio:.2%}
    - Threshold: {min_ratio:.0%}
    - Status: {" PASS" if flag else " FAIL"}
    **Details:**
    {chr(10).join(details)}
    """
    return flag, report

# Example usage
# TODO: Define or load research_result variable with actual research data
research_result = "Find 2 recent papers about recent developments in black hole science:" \
"\n- https://arxiv.org/abs/1234.5678" \
"\n- https://nature.com/article/abcd1234" \
"\n- https://untrustedsource.com/article/xyz9876" \
"\n- https://wikipedia.org/wiki/Black_hole" \
#research_result ="Find 2 recent papers about recent developments in black hole science"
print("Research Results = " + research_result)
flag, report = evaluate_tavily_results(TOP_DOMAINS, research_result)
print(report)

