import google.auth
from google.adk.agents import Agent
from google.adk.tools.bigquery import BigQueryToolset, BigQueryCredentialsConfig
from google.adk.models import Gemini

model = Gemini(model="gemini-2.5-flash")
credentials, project_id = google.auth.default()
credentials_config = BigQueryCredentialsConfig(credentials=credentials)

bq_tools = BigQueryToolset(credentials_config=credentials_config)

analyst_agent = Agent(
    name="MiracleAnalyst",
    model=model,
    instruction="""
    You are a Cloud Data Analyst for an eCommerce company.
    You have access to the 'bigquery-public-data.thelook_ecommerce' dataset.
    When a user asks a question:
    1. Find the right tables in that dataset.
    2. Write and execute the SQL query using your tools.
    3. Explain the business insight clearly to the user.
    """,
    tools=[bq_tools]
)

root_agent = analyst_agent