import requests
import os
from dotenv import load_dotenv
# 1. Load the specific custom environment file
load_dotenv(dotenv_path="Secrets.env")

# 2. Retrieve the API key using os.getenv
api_key = os.getenv("SERPER_API_KEY")

#3. Setup the API
url = f"https://google.serper.dev/search?q=apple+inc&apiKey={api_key}"

payload = {}
headers = {}

#4. Getting the Response from the Specific API
response = requests.request("GET", url, headers=headers, data=payload)

#5. Printing the Response
print(response.text)