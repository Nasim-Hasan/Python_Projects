# =========================
# Imports
# =========================
# --- Standard library
from datetime import datetime
import json
import re
# --- Third-party ---
from aisuite import Client
# --- Local / project ---
import research_tools
import utils
client = Client()

def find_references(task: str, model: str = "openai:gpt-4o", return_messages: str = "default"):
    """Perform a research task using external tools (arxiv, tavily, wikipedia)."""
    prompt = f"""
    You are a research function with access to:
    - arxiv_tool: academic papers
    - tavily_tool: general web search (return JSON when asked)
    - wikipedia_tool: encyclopedic summaries
    Task:
    {task}
    Today is {datetime.now().strftime('%Y-%m-%d')}.
    """.strip()
    messages = [{"role": "user", "content": prompt}]
    tools = [
    research_tools.arxiv_search_tool,
    research_tools.tavily_search_tool,
    research_tools.wikipedia_search_tool,
    ]
    try:
        response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        tool_choice="auto",
        max_turns=5,
        )
        content = response.choices[0].message.content
        return (content, messages) if return_messages else content
    except Exception as e:
        return f"[Model Error: {e}]"

research_task = "Find 2 recent papers about recent developments in black hole science"
research_result = find_references(research_task)
utils.print_html(
research_result,
title="Research Function Output"
)