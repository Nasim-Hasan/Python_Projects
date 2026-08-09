import requests
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv("Secrets.env")

serper_api_key = os.getenv("SERPER_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check API keys
if not serper_api_key:
    raise ValueError("SERPER_API_KEY is missing from Secrets.env")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is missing from Secrets.env")


# 1. Call the Serper API
url = "https://google.serper.dev/search"

headers = {
    "X-API-KEY": serper_api_key,
    "Content-Type": "application/json"
}

payload = {
    "q": "Apple Inc"
}

api_response = requests.post(
    url,
    headers=headers,
    json=payload,
    timeout=30
)

# Raise an error if Serper failed
api_response.raise_for_status()

# Get the actual JSON data
search_data = api_response.json()

print("Serper response:")
print(search_data)


# 2. Create the prompt
prompt = f"""
Analyze the following search results about Apple Inc.

Summarize the key information in a clear and concise way.

Search results:
{search_data}
"""


# 3. Connect to OpenAI
client = OpenAI(
    api_key=openai_api_key
)

response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\nAI Summary:")
print(response.choices[0].message.content)