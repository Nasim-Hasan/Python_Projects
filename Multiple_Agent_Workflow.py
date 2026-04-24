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
from Copy_Writer_Agent import copywriter_agent
from Packaging_Agent import packaging_agent
from Market_Research_Agent import market_research_agent
from Graphic_Designer_Agent import graphic_designer_agent
# =========================
# Environment & Client
# =========================
load_dotenv()
client = aisuite.Client()

def multiple_agent_workflow(output_path: str = "campaign_summary.md")->dict:
    """
    Runs the full summer sunglasses campaign pipeline:
    1. Market research (search trends + match products)
    2. Generate visual + caption
    3. Generate quote based on image + trend
    4. Create executive markdown report
    Returns:
    dict: Dictionary containing all intermediate results + path to final report
    """
    # 1. Run market research agent
    trend_summary = market_research_agent()
    print(" Market research completed")
    # 2. Generate image + caption
    visual_result = graphic_designer_agent(trend_insights=trend_summary)
    image_path = visual_result["image_path"]
    print(" Image generated")
    # 3. Generate quote based on image + trends
    quote_result = copywriter_agent(image_path=image_path, trend_summary=trend_summary)
    quote = quote_result.get("quote", "")
    justification = quote_result.get("justification", "")
    print(" Quote created")
    # 4. Generate markdown report
    md_path = packaging_agent(
    trend_summary=trend_summary,
    image_url=image_path,
    quote=quote,
    justification=justification,
    output_path=f"campaign_summary_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.md")
    print(f" Report generated: {md_path}")
    return {
    "trend_summary": trend_summary,
    "visual": visual_result,
    "quote": quote_result,
    "markdown_path": md_path
    }

results = multiple_agent_workflow()
with open(results["markdown_path"], "r", encoding="utf-8") as f:
  md_content = f.read()
display(Markdown(md_content)) 