"""
Main orchestration module for PyCaretAgent.
Defines the Root Agent responsible for routing user requests to specialized sub-agents.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import FunctionTool
from pycaretagent.utils.config import DEFAULT_MODEL
from pycaretagent.utils.instructions.route_prompt import ROUTE_INSTRUCTIONS
from pycaretagent.utils.agents.classification_agent import classification_agent
from pycaretagent.utils.agents.regression_agent import regression_agent
from pycaretagent.utils.agents.clustering_agent import clustering_agent
from pycaretagent.utils.agents.anomaly_agent import anomaly_agent
from pycaretagent.utils.agents.ts_agent import ts_agent
from pycaretagent.utils.tools.file_validator_tool import check_csv_presence
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define validation tools for the Root Agent
csv_validator_tool = FunctionTool(func=check_csv_presence)

# Initialize the Root Agent with its routing logic and all specialized sub-agents
root_agent = LlmAgent(
    name="root_agent",
    description="Orchestrator agent that validates requirements and delegates to specialized ML sub-agents.",
    instruction=ROUTE_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    tools=[csv_validator_tool],
    sub_agents=[
        classification_agent,
        regression_agent,
        clustering_agent,
        anomaly_agent,
        ts_agent
    ]
)
