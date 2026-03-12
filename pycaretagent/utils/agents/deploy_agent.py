"""
Deployment & Integrity Sub-Agent for PyCaretAgent.
Handles post-training artifact verification and deployment packaging.
"""

from google.adk.agents.llm_agent import LlmAgent
from pycaretagent.utils.config import DEFAULT_MODEL, BUILTIN_PLANNER, GENERATE_CONTENT_CONFIG
from pycaretagent.utils.tools.csv_analytics_tool import csv_analytics_tool
from pycaretagent.utils.tools.file_ops_tool import file_writer_tool, file_copy_tool, find_file_tool
from pycaretagent.utils.instructions.deploy_prompt import DEPLOY_INSTRUCTIONS

def get_deploy_agent():
    """
    Returns a new instance of the Deployment Agent.
    Required because ADK agents can only have one parent.
    """
    return LlmAgent(
        name="deploy_agent",
        description="Finalizes the ML lifecycle by verifying artifacts and preparing production-ready wrappers.",
        instruction=DEPLOY_INSTRUCTIONS,
        model=DEFAULT_MODEL,
        generate_content_config=GENERATE_CONTENT_CONFIG,
        planner=BUILTIN_PLANNER,
        tools=[csv_analytics_tool, file_writer_tool, file_copy_tool, find_file_tool],
        disallow_transfer_to_parent=True
    )
