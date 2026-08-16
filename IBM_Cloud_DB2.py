#pip install ibm_db ibmcloudant
import ibm_db
import os, json
from dotenv import load_dotenv
from ibm_cloud_sdk_core import ApiException

# 1. Load Credentials
load_dotenv("Secrets.env")
CLOUD_DSN_DRIVER = os.environ["CLOUD_DSN_DRIVER"]
CLOUD_DSN_DATABASE =  os.environ["CLOUD_DSN_DATABASE"]
CLOUD_HOST_NAME = os.environ["CLOUD_HOST_NAME"]
CLOUD_DSN_PORT = os.environ["CLOUD_DSN_PORT"]
CLOUD_DSN_PROTOCOL = os.environ["CLOUD_DSN_PROTOCOL"]
CLOUD_DSN_UID = os.environ["CLOUD_DSN_UID"]
CLOUD_DSN_PWD = os.environ["CLOUD_DSN_PWD"]
CLOUD_DSN_SECURITY = os.environ["CLOUD_DSN_SECURITY"]

#2. Construct the Connection String
conn_string = (
    f"DRIVER={CLOUD_DSN_DRIVER};"
    f"DATABASE={CLOUD_DSN_DATABASE};"
    f"HOSTNAME={CLOUD_HOST_NAME};"
    f"PORT={CLOUD_DSN_PORT};"
    f"PROTOCOL={CLOUD_DSN_PROTOCOL};"
    f"UID={CLOUD_DSN_UID};"
    f"PWD={CLOUD_DSN_PWD};"
    f"SECURITY={CLOUD_DSN_SECURITY};"
)

try:
    #3. Establish connection to the database
    conn = ibm_db.connect(conn_string, "", "")
    print("Successfully connected to IBM Cloud Db2!")

    # 4. Define the SQL query using '?' as placeholders for security
    # Replace 'MY_SCHEMA.CUSTOMERS' and columns with your actual table design
    sql_query = "INSERT INTO MY_SCHEMA.CUSTOMERS (ID, FIRST_NAME, LAST_NAME) VALUES (?, ?, ?)"

    # 5. Prepare the SQL Statement
    stmt = ibm_db.prepare(conn, sql_query)
    
    # 6. Define Data Row to Insert
    row_data = (101, "Jane", "Doe")
    
    # 7. Execute the Statement with the Data
    if ibm_db.execute(stmt, row_data):
        print("Row inserted successfully!")
    else:
        print("Failed to insert row.")

#8. Capturing the Exceptions
except ApiException as ae:
    print(f"IBM Cloudant API exception occurred: {ae.code} - {ae.message}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")



