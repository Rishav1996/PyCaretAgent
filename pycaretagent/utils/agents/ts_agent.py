"""
Time Series Sub-Agent for PyCaretAgent.
Specializes in forecasting workflows using PyCaret's Time Series module,
implemented as a SequentialAgent for structured processing.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.code_executors import UnsafeLocalCodeExecutor
from pycaretagent.utils.config import DEFAULT_MODEL, BUILTIN_PLANNER
from pycaretagent.utils.callbacks import (
    extract_session_id_callback, 
    check_execution_success_callback, 
    check_failure_status_callback
)
from pycaretagent.utils.tools.google_search_tool import google_search_tool
from pycaretagent.utils.instructions.ts_prompt import (
    TS_PLANNER_INSTRUCTIONS,
    TS_EXECUTOR_INSTRUCTIONS
)

# Sub-Agent: Planner (Analyzes the task and plans the time series workflow)
ts_planner = LlmAgent(
    name="ts_planner",
    description="Analyzes the forecasting task and plans the ML workflow.",
    instruction=TS_PLANNER_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    output_key="ts_plan",
    tools=[google_search_tool],
    after_agent_callback=extract_session_id_callback
)

# Sub-Agent: Executor (Performs training, comparison, and evaluation)
ts_executor = LlmAgent(
    name="ts_executor",
    description="Executes the planned forecasting workflow using PyCaret functions.",
    instruction=TS_EXECUTOR_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    code_executor=UnsafeLocalCodeExecutor(),
    planner=BUILTIN_PLANNER,
    tools=[google_search_tool],
    before_model_callback=check_failure_status_callback,
    after_agent_callback=check_execution_success_callback
)

# Initialize the Time Series Agent as a SequentialAgent
# This agent orchestrates the sub-agents in a strict sequence: 
# Planner -> Executor
ts_agent = SequentialAgent(
    name="ts_agent",
    description="Structured time series forecasting workflow.",
    sub_agents=[
        ts_planner, 
        ts_executor
    ]
)
