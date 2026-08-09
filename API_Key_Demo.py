import os
from dotenv import load_dotenv

# 1. Load the specific custom environment file
load_dotenv(dotenv_path="Secrets.env")

# 2. Retrieve the API key using os.getenv
api_key = os.getenv("SERPER_API_KEY")

# 3. Use the key securely (or throw an error if it is missing)
if not api_key:
    raise ValueError("API Key not found! Please check your Secrets.env file.")

print("API Key loaded successfully!")
