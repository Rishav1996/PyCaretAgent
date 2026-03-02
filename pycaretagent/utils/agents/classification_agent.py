"""
Classification Sub-Agent for PyCaretAgent.
Specializes in categorical prediction workflows using PyCaret's Classification module,
now implemented as a SequentialAgent for more structured processing.
"""

import re
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.code_executors import UnsafeLocalCodeExecutor
from google.adk.planners import BuiltInPlanner
from google.genai import types
from pycaretagent.utils.config import DEFAULT_MODEL
from pycaretagent.utils.instructions.classification_prompt import (
    CLASSIFICATION_PLANNER_INSTRUCTIONS,
    CLASSIFICATION_EXECUTOR_INSTRUCTIONS
)

def extract_session_id_callback(callback_context: CallbackContext):
    """
    Callback to extract the Session ID from the planner's response 
    and store it in the session state for downstream agents.
    """
    plan_text = callback_context.state.get("classification_plan", "")
    
    match = re.search(r"SESSION_ID:\s*([A-Za-z0-9]+)", plan_text)
    if match:
        session_id = match.group(1)
        callback_context.state["session_id"] = session_id
    
    return None

def check_execution_success_callback(callback_context: CallbackContext):
    """
    Callback to check if the executor ran successfully.
    Signals that the task is done.
    """
    callback_context.state["task_completed"] = True
    return None

def check_failure_status_callback(callback_context: CallbackContext, llm_request):
    """
    Callback to check if the previous run failed.
    """
    # Check the state for failure status. 
    # If False, it means success, so we skip.
    status = callback_context.state.get("check_failure_status")
    if status is False:
        return "Task already completed successfully. Skipping redundant execution."
    return None

# --- Built-In Planner ---
# Uses the model's native thinking capabilities.
builtin_planner = BuiltInPlanner(
    thinking_config=types.ThinkingConfig(
        include_thoughts=True,
        thinking_budget=1024
    )
)

# Sub-Agent: Planner (Analyzes the task and plans the workflow)
classification_planner = LlmAgent(
    name="classification_planner",
    description="Analyzes the classification task and plans the ML workflow.",
    instruction=CLASSIFICATION_PLANNER_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    output_key="classification_plan",
    after_agent_callback=extract_session_id_callback
)

# Sub-Agent: Executor (Performs training, comparison, and evaluation)
classification_executor = LlmAgent(
    name="classification_executor",
    description="Executes the planned classification workflow using PyCaret functions.",
    instruction=CLASSIFICATION_EXECUTOR_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    code_executor=UnsafeLocalCodeExecutor(error_retry_attempts=10),
    planner=builtin_planner,
    before_model_callback=check_failure_status_callback,
    after_agent_callback=check_execution_success_callback
)

# Initialize the Classification Agent as a SequentialAgent
# This agent orchestrates the sub-agents in a strict sequence: 
# Planner -> Executor
classification_agent = SequentialAgent(
    name="classification_agent",
    description="Structured classification workflow.",
    sub_agents=[
        classification_planner, 
        classification_executor
    ]
)
