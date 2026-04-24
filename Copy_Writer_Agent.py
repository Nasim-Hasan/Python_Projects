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

def copywriter_agent(image_path: str, trend_summary: str, model: str = "openai:o4-mini"):
    """
    Uses aisuite (OpenAI only) to send an image and a trend summary and return a campaign Args:
    image_path (str): URL of the image to be analyzed.
    trend_summary (str): Text from the researcher agent.
    model (str): OpenAI model (e.g., openai:o4-mini, openai:gpt-4o)
    Returns:
    dict: {
    "quote": "...",
    "justification": "...",
    "image_path": "..."
    }
    """
    #utils.log_agent_title_html("Copywriter Agent", " ")
    print("Copywriter Agent")
    # Step 1: Load local image and encode as base64
    with open(image_path, "rb") as f:
       img_bytes = f.read()
    b64_img = base64.b64encode(img_bytes).decode("utf-8")
    # Step 2: Build OpenAI-compliant multimodal message
    messages = [
    {
    "role": "system",
    "content": "You are a copywriter that creates elegant campaign quotes based on visual and textual inputs."
    },
    {
    "role": "user",
    "content": [
        {
            "type": "image_url",
            "image_url": {
            "url": f"data:image/png;base64,{b64_img}",
            "detail": "auto"
            }
        },
        {
            "type": "text",
            "text": f"""
            Here is a visual marketing image and a trend analysis:
            Trend summary:
            \"\"\"{trend_summary}\"\"\"
            Please return a JSON object like:
            {{
            "quote": "A short, elegant campaign phrase (max 12 words)",
            "justification": "Why this quote matches the image and trend"
            }}"""
        }
    ]
    }
    ]
    # Step 3: Send request via aisuite
    response = client.chat.completions.create(
    model=model,
    messages=messages,
    )
    # Step 4: Parse JSON response
    content = response.choices[0].message.content.strip()
    #utils.log_final_summary_html(content)
    print(content)
    try:
        match = re.search(r'\{.*\}', content, re.DOTALL)
        parsed = json.loads(match.group(0)) if match else {"error": "No valid JSON returned"}
    except Exception as e:
        parsed = {"error": f"Failed to parse: {e}", "raw": content}
    parsed["image_path"] = image_path
    return parsed

copywriter_agent_result = copywriter_agent(
image_path="C:\\",
trend_summary="Round Shaped Sunglasses"
)