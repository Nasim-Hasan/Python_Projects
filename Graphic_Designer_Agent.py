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

def graphic_designer_agent(trend_insights: str, caption_style: str = "short punchy", size: str = "1024x1024") -> dict:
    """
    Uses aisuite to generate a marketing prompt/caption and OpenAI (directly) to generate Args:
    trend_insights (str): Trend summary from the researcher agent.
    caption_style (str): Optional style hint for caption.
    size (str): Image resolution (e.g., '1024x1024').
    Returns:
    dict: A dictionary with image_url, prompt, and caption.
    """
    #utils.log_agent_title_html("Graphic Designer Agent", " ")
    print("Graphic Designer Agent")
    # Step 1: Generate prompt and caption using aisuite
    system_message = (
    "You are a visual marketing assistant. Based on the input trend insights, "
    "write a creative and visual prompt for an AI image generation model, and also")
    user_prompt = f"""
    Trend insights:
    {trend_insights}
    Please output:
    1. A vivid, descriptive prompt to guide image generation.
    2. A marketing caption in style: {caption_style}.
    Respond in this format:
    {{"prompt": "...", "caption": "..."}}
    """
    chat_response = client.chat.completions.create(
    model="openai:o4-mini",
    messages=[
    {"role": "system", "content": system_message},
    {"role": "user", "content": user_prompt}
    ]
    )
    content = chat_response.choices[0].message.content.strip()
    match = re.search(r'\{.*\}', content, re.DOTALL)
    parsed = json.loads(match.group(0)) if match else {"error": "No JSON returned"}
    prompt = parsed["prompt"]
    caption = parsed["caption"]
    # Step 2: Generate image directly using openai-python
    openai_client = openai.OpenAI()
    image_response = openai_client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size=size,
    quality="standard",
    n=1,
    response_format="url"
    )
    image_url = image_response.data[0].url
    # Save image locally
    img_bytes = requests.get(image_url).content
    img = Image.open(BytesIO(img_bytes))
    filename = os.path.basename(image_url.split("?")[0])
    image_path = filename
    img.save(image_path)
    # Log summary with local image
    #utils.log_final_summary_html(f"""
    print(f"""
    <h3>Generated Image and Caption</h3>
    <p><strong>Image Path:</strong> <code>{image_path}</code></p>
    <p><strong>Generated Image:</strong></p>
    <img src="{image_path}" alt="Generated Image" style="max-width: 100%; height: auto;">
    <p><strong>Prompt:</strong> {prompt}</p>
    <p><strong>Caption:</strong> {caption}</p>
    """)
    return {
    "image_url": image_url,
    "prompt": prompt,
    "caption": caption,
    "image_path": image_path
    }

graphic_designer_agent_result = graphic_designer_agent(
trend_insights="Round Shaped Sunglasses"
)