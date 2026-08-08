import os
import requests
from ibm_granite_community.notebook_utils import get_env_var
from langchain_core.utils.utils import convert_to_secret_str
from langchain_ollama import ChatOllama
from langchain_replicate import ChatReplicate

model_path = "ibm-granite/granite-4.1-8b"

try: # Look for a locally accessible Ollama server for the model
    response = requests.get(os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434"))
    llm = ChatOllama(
        model="granite4.1:3b",
        num_predict=2000, # Set the maximum number of tokens to generate as output.
        temperature=0.0,
    )
except Exception: # Use Replicate for the model
    llm = ChatReplicate(
        model=model_path,
        replicate_api_token=get_env_var("REPLICATE_API_TOKEN"),
        model_kwargs={
            "max_completion_tokens": 2000, # Set the maximum number of tokens to generate as output.
            "temperature": 0.0,
        },
    )