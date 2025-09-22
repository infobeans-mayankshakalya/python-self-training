import streamlit as st
import requests
from openai import OpenAI
import pandas as pd

# ==== CONFIGURATION ====
DATABRICKS_INSTANCE = "https://dbc-<databricks url>.cloud.databricks.com"
TOKEN = "<dapi token>"
SPACE_ID = "<space id>"      # replace with your Genie Space ID
# PROMPT = "How much did total CCR portfolio exposure (MPE) decrease month-over-month in the year 2024, and what were the main drivers?"
# PROMPT = "What share of total exposure comes from the top 20 counterparties?"

# --- FUNCTIONS ---
def query_genie(question: str):
    # return "Select * from table", [["col1", "col2"], [1, 2], [3, 4]]  # Dummy return for testing without API calls
    HEADERS = {"Authorization": f"Bearer {TOKEN}"}

    START_CONV_URL = f"{DATABRICKS_INSTANCE}/api/2.0/genie/spaces/{SPACE_ID}/start-conversation"

    # ==== 1. Start Conversation ====
    start_payload = {"content": f"Provide response to the following question keep the Human readable column names, Question: {question}"}

    resp = requests.post(START_CONV_URL, headers=HEADERS, json=start_payload)
    resp.raise_for_status()
    data = resp.json()

    conversation_id = data["conversation_id"]
    message_id = data["message_id"]
    status_url = f"{DATABRICKS_INSTANCE}/api/2.0/genie/spaces/{SPACE_ID}/conversations/{conversation_id}/messages/{message_id}"

    while True:
        poll = requests.get(status_url, headers=HEADERS)
        poll.raise_for_status()
        result = poll.json()

        state = result.get("status")
        
        if state == "COMPLETED":
            sql = result["attachments"][0]["query"]['query']
            
            attachment_id = result["attachments"][0]["attachment_id"]

            result_url = f"{DATABRICKS_INSTANCE}/api/2.0/genie/spaces/{SPACE_ID}/conversations/{conversation_id}/messages/{message_id}/query-result/{attachment_id}"
            query_result = requests.get(result_url, headers=HEADERS)
            result = query_result.json()

            dataFrameHead = []
            for column in result["statement_response"]["manifest"]["schema"]['columns']:
                dataFrameHead.append(column['name'])
            dataFrame = [dataFrameHead]
            dataFrame += result["statement_response"]["result"]["data_array"]
            return sql, dataFrame

def summarize_with_openai(dataFrame: list, prompt: str):
    # return "This is a dummy summary."  # Dummy return for testing without API calls
    # Prepare the data as CSV string for context
    # Convert dataFrame (list of lists) to list of dicts with column names as keys
    csv_data = "\n".join([",".join(map(str, row)) for row in dataFrame])
    system_prompt = (
        "You are a Principal Risk Analyst."
        "Analyze the following tabular data, for any summary stay strict to the provided data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      nd provide insights relevant to the business question. "
        "Data:\n" + csv_data +
        "\n\nBusiness Question:\n" + prompt
    )
    OPENAI_API_KEY = "<open ai key>"
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
    # st.write(response)
    return response.choices[0].message.content


# --- STREAMLIT APP ---
st.set_page_config(page_title="Genie + OpenAI Data Assistant", layout="wide")

st.title("Databricks Genie + OpenAI Data Assistant")

question = st.text_input("Ask a question about your data:")

if st.button("Run Query") and question:
    with st.spinner("Querying Genie API..."):
        try:
            sql, df = query_genie(question)
            header_row = df[:1][0] if df else []
            df = pd.DataFrame(df[1:], columns=header_row)  # Convert to DataFrame for better display
            st.subheader("Genie SQL & Results:")
            st.code(sql, language="sql")
            st.dataframe(df, width="stretch", hide_index=False)
        except Exception as e:
            st.error(f"Error querying Genie API: {e}")
            st.stop()

    with st.spinner("Summarizing with OpenAI..."):
        try:
            summary = summarize_with_openai(df, question)
            st.subheader("AI Summary:")
            st.write(summary)
        except Exception as e:
            st.error(f"Error summarizing with OpenAI: {e}")
