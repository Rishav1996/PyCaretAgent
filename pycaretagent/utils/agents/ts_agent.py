"""
Time Series Sub-Agent for PyCaretAgent.
Specializes in forecasting workflows using PyCaret's Time Series module,
implemented as a SequentialAgent for structured processing.
"""

import re
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.code_executors import UnsafeLocalCodeExecutor
from pycaretagent.utils.config import DEFAULT_MODEL
from pycaretagent.utils.tools.html_reporter_tool import save_html_report_tool
from pycaretagent.utils.instructions.ts_prompt import (
    TS_PLANNER_INSTRUCTIONS,
    TS_EXECUTOR_INSTRUCTIONS,
    TS_REPORTER_INSTRUCTIONS
)

def extract_session_id_callback(callback_context: CallbackContext):
    """
    Callback to extract the Session ID from the planner's response 
    and store it in the session state for downstream agents.
    """
    plan_text = callback_context.state.get("ts_plan", "")
    
    match = re.search(r"SESSION_ID:\s*([A-Za-z0-9]+)", plan_text)
    if match:
        session_id = match.group(1)
        callback_context.state["session_id"] = session_id
    
    return None

# Sub-Agent: Planner (Analyzes the task and plans the time series workflow)
ts_planner = LlmAgent(
    name="ts_planner",
    description="Analyzes the forecasting task and plans the ML workflow.",
    instruction=TS_PLANNER_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    output_key="ts_plan",
    after_agent_callback=extract_session_id_callback
)

# Sub-Agent: Executor (Performs training, comparison, and evaluation)
ts_executor = LlmAgent(
    name="ts_executor",
    description="Executes the planned forecasting workflow using PyCaret functions.",
    instruction=TS_EXECUTOR_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    code_executor=UnsafeLocalCodeExecutor(),
    output_key="ts_results"
)

# Sub-Agent: Reporter (Generates markdown summary and styled HTML report)
ts_reporter = LlmAgent(
    name="ts_reporter",
    description="Summarizes results into markdown and uses save_html_report_tool for an HTML report.",
    instruction=TS_REPORTER_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    tools=[save_html_report_tool],
    output_key="ts_report"
)

# Initialize the Time Series Agent as a SequentialAgent
# This agent orchestrates the sub-agents in a strict sequence: 
# Planner -> Executor -> Reporter (w/ HTML)
ts_agent = SequentialAgent(
    name="ts_agent",
    description="Structured time series forecasting workflow with professional reporting.",
    sub_agents=[
        ts_planner, 
        ts_executor, 
        ts_reporter
    ]
)
