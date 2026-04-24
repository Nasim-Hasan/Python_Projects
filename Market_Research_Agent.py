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

def market_research_agent(return_messages: bool = False):
    #utils.log_agent_title_html("Market Research Agent", " ")
    print("Market Research Agent")
    prompt_ = f"""
    You are a fashion market research agent tasked with preparing a trend analysis for a Your goal:
    1. Explore current fashion trends related to sunglasses using web search.
    2. Review the internal product catalog to identify items that align with those trends.
    3. Recommend one or more products from the catalog that best match emerging trends.
    4. If needed, today date is {datetime.now().strftime("%Y-%m-%d")}.
    You can call the following tools:
    - tavily_search_tool: to discover external web trends.
    - product_catalog_tool: to inspect the internal sunglasses catalog.
    Once your analysis is complete, summarize:
    - The top 2–3 trends you found.
    - The product(s) from the catalog that fit these trends.
    - A justification of why they are a good fit for the summer campaign.
    """
    messages = [{"role": "user", "content": prompt_}]
    tools_ = tools.get_available_tools()
    while True:
        response = client.chat.completions.create(
        model="openai:o4-mini",
        messages=messages,
        tools=tools_,
        tool_choice="auto"
        )
        msg = response.choices[0].message
        if msg.content:
            #utils.log_final_summary_html(msg.content)
            print(msg.content)
            return (msg.content, messages) if return_messages else msg.content
        if msg.tool_calls:
            for tool_call in msg.tool_calls:
                #utils.log_tool_call_html(tool_call.function.name, tool_call)
                print(f"Tool call: {tool_call.function.name} with args {tool_call.arguments}")
                result = tools.handle_tool_call(tool_call)
                #utils.log_tool_result_html(result)
                print(f"Tool result: {result}")
        messages.append(msg)
        messages.append(tools.create_tool_response_message(tool_call))
        
            
market_research_result = market_research_agent()