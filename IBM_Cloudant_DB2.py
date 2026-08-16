#Install
#pip install ibmcloudant
import os, json
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

# 1. Load credentials
load_dotenv("Secrets.env")
CLOUDANT_API_KEY = os.environ["CLOUDANT_API_KEY"]
CLOUDANT_SERVICE_URL = os.environ["CLOUDANT_SERVICE_URL"]
CLOUDANT_DB = os.environ["CLOUDANT_DB"]
CLOUDANT_DOC_ID = os.environ["CLOUDANT_DOC_ID"]

# 2. Setup authenticator with your IBM Cloud API Key
authenticator = IAMAuthenticator(CLOUDANT_API_KEY)

# 3. Initialize the Cloudant client with your Service URL
client = CloudantV1(authenticator=authenticator)
client.set_service_url(CLOUDANT_SERVICE_URL)

# 4. Fetch a specific document from a database
response = client.get_document(db=CLOUDANT_DB, doc_id=CLOUDANT_DOC_ID)

document = response.get_result()
print(document)

