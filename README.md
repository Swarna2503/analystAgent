AI Data Analyst built using the **Google Agent Development Kit (ADK)**. This agent translates natural language into optimized SQL to query the `thelook_ecommerce` public dataset on Google BigQuery.

## 🏗️ System Architecture
* **LLM:** Gemini 2.5 Flash (via Google ADK)
* **Data Warehouse:** Google BigQuery
* **Compute:** Google Cloud Run
* **Framework:** Google Agent Development Kit (ADK)

## Agent Intelligence (`agent.py`)
The agent is configured as a **Senior Data Analyst** with the following capabilities:
1.  **Tooling:** Integrated `BigQueryToolset` with automated credential handling.
2.  **Reasoning:** A three-step loop: Find appropriate tables -> Generate & execute SQL -> Explain business insights.
3.  **Model:** Utilizes `gemini-1.5-flash` for high-speed reasoning and accurate SQL generation.

---

## 🚀 Deployment Commands (GCP)
These are the exact steps used to deploy the backend to Google Cloud:

### List of Commands
```bash
gcloud init
gcloud auth login
gcloud config set project [YOUR_PROJECT_ID]
gcloud builds submit --tag gcr.io/[PROJECT_ID]/ecommerce-agent
adk deploy cloud_run

##API Integration
{
  "appName": "ecommerce_agent",
  "userId": "username",
  "sessionId": "chat_01",
  "newMessage": {
    "parts": [{"text": "Show me the top 5 products by revenue"}]
  }
}
