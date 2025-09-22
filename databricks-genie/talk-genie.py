import requests
import time
import csv
from openai import OpenAI

# ==== CONFIGURATION ====
DATABRICKS_INSTANCE = "https://adb-<databricks URL>.azuredatabricks.net"  # replace with your workspace URL
TOKEN = "<DAPI TOKEN VALUE>"  # replace with your PAT
SPACE_ID = "<SPACE ID>"      # replace with your Genie Space ID
# PROMPT = "How much did total CCR portfolio exposure (MPE) decrease month-over-month in the year 2024, and what were the main drivers?"
PROMPT = "How much did total CCR portfolio exposure (MPE) decrease month-over-month in the year 2024, and what were the main drivers?"


# ==== API ENDPOINTS ====
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

START_CONV_URL = f"{DATABRICKS_INSTANCE}/api/2.0/genie/spaces/{SPACE_ID}/start-conversation"


# ==== 1. Start Conversation ====
start_payload = {"content": PROMPT}

resp = requests.post(START_CONV_URL, headers=HEADERS, json=start_payload)
resp.raise_for_status()
data = resp.json()

conversation_id = data["conversation_id"]
message_id = data["message_id"]

print(f"Conversation started (conversation_id={conversation_id}, message_id={message_id})")


# ==== 2. Poll for Response ====
status_url = f"{DATABRICKS_INSTANCE}/api/2.0/genie/spaces/{SPACE_ID}/conversations/{conversation_id}/messages/{message_id}"

while True:
    poll = requests.get(status_url, headers=HEADERS)
    poll.raise_for_status()
    result = poll.json()

    state = result.get("status")
    
    if state == "COMPLETED":
        print("\n✅ Genie Response:\n")
        print(result["attachments"][0]["query"]['query'])   # Natural language response
        result["attachments"][0]["query"]['query']
        
        attachment_id = result["attachments"][0]["attachment_id"]

        result_url = f"{DATABRICKS_INSTANCE}/api/2.0/genie/spaces/{SPACE_ID}/conversations/{conversation_id}/messages/{message_id}/query-result/{attachment_id}"
        query_result = requests.get(result_url, headers=HEADERS)
        result = query_result.json()

        dataFrameHead = []
        for column in result["statement_response"]["manifest"]["schema"]['columns']:
            dataFrameHead.append(column['name'])
        dataFrame = [dataFrameHead]
        dataFrame += result["statement_response"]["result"]["data_array"]
        print(dataFrame)
        OPENAI_API_KEY = "<open ai key>"

        def get_insights(dataFrame, prompt):
            # Prepare the data as CSV string for context
            csv_data = "\n".join([",".join(map(str, row)) for row in dataFrame])
            system_prompt = (
                "You are a professional business data analyst. "
                "Analyze the following tabular data a                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       nd provide insights relevant to the business question. "
                "Data:\n" + csv_data +
                "\n\nBusiness Question:\n" + prompt
            )
            client = OpenAI(
                api_key=OPENAI_API_KEY
            )
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                store=True,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": "Please analyse and generate insights on the data and answer the business question. Please provide only the summary."}
                ],
                max_tokens=500,
                top_p=0.1
            )
            return response.choices[0].message.content

        insights = get_insights(dataFrame, PROMPT)
        print("\n OpenAI Insights:\n", insights)
        break
    elif state == "failed":
        print("❌ Genie failed to generate a response:", result)
        break
    else:
        print("⏳ Waiting for response...")
        time.sleep(2)