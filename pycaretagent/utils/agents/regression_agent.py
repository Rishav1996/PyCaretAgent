"""
Regression Sub-Agent for PyCaretAgent.
Specializes in numerical value prediction using PyCaret's Regression module,
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
from pycaretagent.utils.instructions.regression_prompt import (
    REGRESSION_PLANNER_INSTRUCTIONS,
    REGRESSION_EXECUTOR_INSTRUCTIONS
)

# Sub-Agent: Planner (Analyzes the task and plans the regression workflow)
regression_planner = LlmAgent(
    name="regression_planner",
    description="Analyzes the regression task and plans the ML workflow.",
    instruction=REGRESSION_PLANNER_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    output_key="regression_plan",
    tools=[google_search_tool],
    after_agent_callback=extract_session_id_callback
)

# Sub-Agent: Executor (Performs training, comparison, and evaluation)
regression_executor = LlmAgent(
    name="regression_executor",
    description="Executes the planned regression workflow using PyCaret functions.",
    instruction=REGRESSION_EXECUTOR_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    code_executor=UnsafeLocalCodeExecutor(),
    planner=BUILTIN_PLANNER,
    tools=[google_search_tool],
    before_model_callback=check_failure_status_callback,
    after_agent_callback=check_execution_success_callback
)

# Initialize the Regression Agent as a SequentialAgent
# This agent orchestrates the sub-agents in a strict sequence: 
# Planner -> Executor
regression_agent = SequentialAgent(
    name="regression_agent",
    description="Structured regression workflow.",
    sub_agents=[
        regression_planner, 
        regression_executor
    ]
)
