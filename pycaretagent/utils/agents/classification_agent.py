"""
Classification Sub-Agent for PyCaretAgent.
Specializes in categorical prediction workflows using PyCaret's Classification module.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.code_executors import UnsafeLocalCodeExecutor
from pycaretagent.utils.config import DEFAULT_MODEL, BUILTIN_PLANNER, GENERATE_CONTENT_CONFIG
from pycaretagent.utils.callbacks import (
    extract_session_id_callback
)
from pycaretagent.utils.tools.csv_analytics_tool import csv_analytics_tool
from pycaretagent.utils.tools.session_id_generator_tool import session_id_generator_tool
from pycaretagent.utils.agents.deploy_agent import get_deploy_agent
from pycaretagent.utils.instructions.classification_prompt import (
    CLASSIFICATION_EXECUTOR_INSTRUCTIONS
)

# Classification Agent: Senior ML Automation Architect
# Architects and executes the classification workflow.
classification_agent = LlmAgent(
    name="classification_agent",
    description="Architects and executes the classification workflow using PyCaret functions.",
    instruction=CLASSIFICATION_EXECUTOR_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    generate_content_config=GENERATE_CONTENT_CONFIG,
    code_executor=UnsafeLocalCodeExecutor(error_retry_attempts=10),
    planner=BUILTIN_PLANNER,
    tools=[csv_analytics_tool, session_id_generator_tool],
    sub_agents=[get_deploy_agent()],
    after_agent_callback=extract_session_id_callback
)
