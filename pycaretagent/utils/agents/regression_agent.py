"""
Regression Sub-Agent for PyCaretAgent.
Specializes in numerical value prediction using PyCaret's Regression module,
implemented as a SequentialAgent for structured processing.
"""

import re
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.code_executors import BuiltInCodeExecutor
from pycaretagent.utils.config import DEFAULT_MODEL
from pycaretagent.utils.tools.html_reporter_tool import save_html_report_tool
from pycaretagent.utils.instructions.regression_prompt import (
    REGRESSION_PLANNER_INSTRUCTIONS,
    REGRESSION_EXECUTOR_INSTRUCTIONS,
    REGRESSION_REPORTER_INSTRUCTIONS
)

def extract_session_id_callback(callback_context: CallbackContext):
    """
    Callback to extract the Session ID from the planner's response 
    and store it in the session state for downstream agents.
    """
    plan_text = callback_context.state.get("regression_plan", "")
    
    match = re.search(r"SESSION_ID:\s*([A-Za-z0-9]+)", plan_text)
    if match:
        session_id = match.group(1)
        callback_context.state["session_id"] = session_id
    
    return None

# Sub-Agent: Planner (Analyzes the task and plans the regression workflow)
regression_planner = LlmAgent(
    name="regression_planner",
    description="Analyzes the regression task and plans the ML workflow.",
    instruction=REGRESSION_PLANNER_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    output_key="regression_plan",
    after_agent_callback=extract_session_id_callback
)

# Sub-Agent: Executor (Performs training, comparison, and evaluation)
regression_executor = LlmAgent(
    name="regression_executor",
    description="Executes the planned regression workflow using PyCaret functions.",
    instruction=REGRESSION_EXECUTOR_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    code_executor=BuiltInCodeExecutor(),
    output_key="regression_results"
)

# Sub-Agent: Reporter (Generates markdown summary and styled HTML report)
regression_reporter = LlmAgent(
    name="regression_reporter",
    description="Summarizes results into markdown and uses save_html_report_tool for an HTML report.",
    instruction=REGRESSION_REPORTER_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    tools=[save_html_report_tool],
    output_key="regression_report"
)

# Initialize the Regression Agent as a SequentialAgent
# This agent orchestrates the sub-agents in a strict sequence: 
# Planner -> Executor -> Reporter (w/ HTML)
regression_agent = SequentialAgent(
    name="regression_agent",
    description="Structured regression workflow with professional reporting.",
    sub_agents=[
        regression_planner, 
        regression_executor, 
        regression_reporter
    ]
)
