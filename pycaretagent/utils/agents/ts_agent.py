"""
Time Series Sub-Agent for PyCaretAgent.
Specializes in forecasting workflows using PyCaret's Time Series module.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.code_executors import UnsafeLocalCodeExecutor
from pycaretagent.utils.config import DEFAULT_MODEL, BUILTIN_PLANNER, GENERATE_CONTENT_CONFIG
from pycaretagent.utils.callbacks import (
    extract_session_id_callback
)
from pycaretagent.utils.tools.google_search_tool import google_search_tool
from pycaretagent.utils.tools.csv_analytics_tool import csv_analytics_tool
from pycaretagent.utils.tools.session_id_generator_tool import session_id_generator_tool
from pycaretagent.utils.instructions.ts_prompt import (
    TS_EXECUTOR_INSTRUCTIONS
)

# Time Series Agent: Senior ML Automation Architect
# Architects and executes the time series forecasting workflow.
ts_agent = LlmAgent(
    name="ts_agent",
    description="Architects and executes the time series forecasting workflow using PyCaret functions.",
    instruction=TS_EXECUTOR_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    generate_content_config=GENERATE_CONTENT_CONFIG,
    code_executor=UnsafeLocalCodeExecutor(error_retry_attempts=10),
    planner=BUILTIN_PLANNER,
    tools=[google_search_tool, csv_analytics_tool, session_id_generator_tool],
    after_agent_callback=extract_session_id_callback
)
