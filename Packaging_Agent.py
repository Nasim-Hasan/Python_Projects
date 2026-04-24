# =========================
# Imports
# =========================
# --- Standard library ---
import base64
import json
import os
import re
from datetime import datetime
from io import BytesIO
# --- Third-party ---
import requests
import openai
from PIL import Image
from dotenv import load_dotenv
from IPython.display import Markdown, display
import aisuite
# --- Local / project ---
import tools
import utils
# =========================
# Environment & Client
# =========================
load_dotenv()
client = aisuite.Client()

def packaging_agent(trend_summary: str, image_url: str, quote: str, justification:str, output_path: str) -> str:
    """
    Packages the campaign assets into a beautifully formatted markdown report for executive Args:
    trend_summary (str): Summary of the market trends.
    image_url (str): URL of the campaign image.
    quote (str): Marketing quote to overlay.
    justification (str): Explanation for the quote.
    output_path (str): Path to save the markdown report.
    Returns:
    str: Path to the saved markdown file.
    """
    #utils.log_agent_title_html("Packaging Agent", " ")
    print("Packaging Agent")
    # We use this path in the src of the <img>
    styled_image_html = f"""
    ![Open the generated file to see]({image_url})
    """
    beautified_summary = client.chat.completions.create(
    model="openai:o4-mini",
    messages=[
    {"role": "system", "content": "You are a marketing communication expert"}, 
    {"role": "user", "content": f"""Please rewrite the following trend summary to be clear, professional, and engaging for \"\"\"{trend_summary.strip()}\"\"\"
    """}
    ]
    ).choices[0].message.content.strip()
    #utils.log_tool_result_html(beautified_summary)
    print(beautified_summary)
    # Combine all parts into markdown
    markdown_content = f"""# Summer Sunglasses Campaign – Executive Summary"""
    ## Refined Trend Insights
    {beautified_summary}
    ## Campaign Visual
    {styled_image_html}
    ## Campaign Quote
    {quote.strip()}
    ## Why This Works
    {justification.strip()}
    """"
    *Report generated on {datetime.now().strftime('%Y-%m-%d')}*
    """
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    return output_path

packaging_agent_result = packaging_agent(
trend_summary="Round Shaped Sunglasses",
image_url="C:\\",
quote="quote",
justification="justification",
output_path=f"campaign_summary_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.md"
)