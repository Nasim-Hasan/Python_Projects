import requests
from openai import OpenAI

#1. Setup Variables
url = f"https://api.openai.com"
payload = {}
headers = {}

#2. Fetching the Data
print(requests.get('https://api.openai.com').status_code)
print(requests.request("GET", url, headers=headers, data=payload).text)

client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="Say hello in one sentence."
)

print(response.output_text)