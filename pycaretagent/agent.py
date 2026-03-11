"""
Main orchestration module for PyCaretAgent.
Defines the Root Agent responsible for routing user requests to specialized sub-agents.
"""

from google.adk.agents.llm_agent import LlmAgent
from pycaretagent.utils.config import DEFAULT_MODEL, GENERATE_CONTENT_CONFIG
from pycaretagent.utils.tools.file_validator_tool import csv_validator_tool
from pycaretagent.utils.instructions.route_prompt import ROUTE_INSTRUCTIONS as ROOT_AGENT_INSTRUCTIONS

# Import specialized sub-agents
from pycaretagent.utils.agents.classification_agent import classification_agent
from pycaretagent.utils.agents.regression_agent import regression_agent
from pycaretagent.utils.agents.clustering_agent import clustering_agent
from pycaretagent.utils.agents.anomaly_agent import anomaly_agent
from pycaretagent.utils.agents.ts_agent import ts_agent

# The Root Agent acts as a Router.
# Reverted back to LlmAgent as per user request.
root_agent = LlmAgent(
    name="pycaret_root_agent",
    description="Primary entry point for PyCaretAgent. Validates input and routes to ML specialists.",
    instruction=ROOT_AGENT_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    generate_content_config=GENERATE_CONTENT_CONFIG,
    tools=[csv_validator_tool],
    sub_agents=[
        classification_agent,
        regression_agent,
        clustering_agent,
        anomaly_agent,
        ts_agent
    ]
)
