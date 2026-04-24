import json
import aisuite as ai
from dotenv import load_dotenv
from datetime import datetime
_ = load_dotenv()
# Create an instance of the AISuite client
client = ai.Client()

def get_current_time() -> str:
    """
    Returns the current time as a string.
    """
    return datetime.now().strftime("%H:%M:%S")

# Message structure
prompt = "What time is it?"
messages = [
{
"role": "user",
"content": prompt,
}
]

response = client.chat.completions.create(
model="openai:gpt-4o",
messages=messages,
tools=[get_current_time],
max_turns=5
)
# See the LLM response
print(response.choices[0].message.content)