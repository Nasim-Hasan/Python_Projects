# ==== Imports ====
from __future__ import annotations
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import json
from dotenv import load_dotenv
from openai import OpenAI
import re, io, traceback
from typing import Any, Dict, Optional
from tinydb import Query, where
# Utility modules
import utils # helper functions for prompting/printing
import inv_utils # functions for inventory, transactions, schema building, and TinyDB
load_dotenv()
client = OpenAI()


# ---------- LLM Code generation ----------
def generate_llm_code(
prompt: str,
*,
inventory_tbl,
transactions_tbl,
model: str = "gpt-4.1-mini",
temperature: float = 0.2,
) -> str:
    """
    Ask the LLM to produce a plan-with-code response.
    Returns the FULL assistant content (including surrounding text and tags).
    The actual code extraction happens later in execute_generated_code.
    """
    schema_block = inv_utils.build_schema_block(inventory_tbl, transactions_tbl)
    prompt = PROMPT.format(schema_block=schema_block, question=prompt)
    resp = client.chat.completions.create(
    model=model,
    temperature=temperature,
    messages=[
    {
    "role": "system",
    "content": "You write safe, well-commented TinyDB code to handle data"},
    {"role": "user", "content": prompt},
    ],
    )
    content = resp.choices[0].message.content or ""
    return content

# --- Helper: extract code between <execute_python>...</execute_python> ---
def _extract_execute_block(text: str) -> str:
    """
    Returns the Python code inside <execute_python>...</execute_python>.
    If no tags are found, assumes 'text' is already raw Python code.
    """
    if not text:
     raise RuntimeError("Empty content passed to code executor.")
    m = re.search(r"<execute_python>(.*?)</execute_python>", text, re.DOTALL)
    return m.group(1).strip() if m else text.strip()

# ----------Code generation ----------
def execute_generated_code(
code_or_content: str,
*,
db,
inventory_tbl,
transactions_tbl,
user_request: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Execute code in a controlled namespace.
    Accepts either raw Python code OR full content with <execute_python> tags.
    Returns minimal artifacts: stdout, error, and extracted answer.
    """
    # Extract code here (now centralized)
    code = _extract_execute_block(code_or_content)
    SAFE_GLOBALS = {
    "Query": Query,
    "get_current_balance": inv_utils.get_current_balance,
    "next_transaction_id": inv_utils.next_transaction_id,
    "user_request": user_request or "",
    }
    SAFE_LOCALS = {
    "db": db,
    "inventory_tbl": inventory_tbl,
    "transactions_tbl": transactions_tbl,
    }
    # Capture stdout from the executed code
    _stdout_buf, _old_stdout = io.StringIO(), sys.stdout
    sys.stdout = _stdout_buf
    err_text = None
    try:
     exec(code, SAFE_GLOBALS, SAFE_LOCALS)
    except Exception:
     err_text = traceback.format_exc()
    finally:
     sys.stdout = _old_stdout
    printed = _stdout_buf.getvalue().strip()
    # Extract possible answers set by the generated code
    answer = (
    SAFE_LOCALS.get("answer_text")
    or SAFE_LOCALS.get("answer_rows")
    or SAFE_LOCALS.get("answer_json"))
    return {
        "code": code, # <- ya sin etiquetas
        "stdout": printed,
        "error": err_text,
        "answer": answer,
        "transactions_tbl": transactions_tbl.all(), # For inspection
        "inventory_tbl": inventory_tbl.all(), # For inspection
    }

def customer_service_agent(
question: str,
*,
db,
inventory_tbl,
transactions_tbl,
model: str = "o4-mini",
temperature: float = 1.0,
reseed: bool = False
) -> dict:
    """
    End-to-end helper:
    1) (Optional) reseed inventory & transactions
    2) Generate plan-as-code from `question`
    3) Execute in a controlled namespace
    4) Render before/after snapshots and return artifacts
    Returns:
    {
    "full_content": <raw LLM response (may include <execute_python> tags)>,
    "exec": {
    "code": <extracted python>,
    "stdout": <plan logs>,
    "error": <traceback or None>,
    "answer": <answer_text/rows/json>,
    "inventory_after": [...],
    "transactions_after": [...]
    }
    }
    """
    # 0) Optional reseed
    if reseed:
     inv_utils.create_inventory()
     inv_utils.create_transactions()
    # 1) Show the question
    utils.print_html(question, title="User Question")
    # 2) Generate plan-as-code (FULL content)
    full_content = generate_llm_code(
    question,
    inventory_tbl=inventory_tbl,
    transactions_tbl=transactions_tbl,
    model=model,
    temperature=temperature,
    )
    utils.print_html(full_content, title="Plan with Code (Full Response)")
    # 3) Before snapshots
    utils.print_html(json.dumps(inventory_tbl.all(), indent=2), title="Inventory Table utils.print_html(json.dumps(transactions_tbl.all(), indent=2), title=Transactions # 1") 
    # 4) Execute the generated code in a controlled namespace and capture artifacts
    exec_res = execute_generated_code(
    full_content,
    db=db,
    inventory_tbl=inventory_tbl,
    transactions_tbl=transactions_tbl,
    user_request=question,
    )
    # 5) After snapshots + final answer
    utils.print_html(exec_res["answer"], title="Plan Execution · Extracted Answer")
    utils.print_html(json.dumps(inventory_tbl.all(), indent=2), title="Inventory Table utils.print_html(json.dumps(transactions_tbl.all(), indent=2), title=Transactions # 2") 
    # 6) Return artifacts
    return {
    "full_content": full_content,
    "exec": {
    "code": exec_res["code"],
    "stdout": exec_res["stdout"],
    "error": exec_res["error"],
    "answer": exec_res["answer"],
    "inventory_after": inventory_tbl.all(),
    "transactions_after": transactions_tbl.all(),
      },
    }

prompt = "I want to buy 3 pairs of classic sunglasses and 1 pair of aviator sunglasses."
out = customer_service_agent(
    prompt,
    db=db,
    inventory_tbl=inventory_tbl,
    transactions_tbl=transactions_tbl,
    model="o4-mini",
    temperature=1.0,
    reseed=True # set False to keep current state of the inventory and the transactions
)