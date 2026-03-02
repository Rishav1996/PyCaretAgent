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
from pycaretagent.utils.config import DEFAULT_MODEL
from pycaretagent.utils.tools.html_reporter_tool import save_html_report_tool
from pycaretagent.utils.instructions.classification_prompt import (
    CLASSIFICATION_PLANNER_INSTRUCTIONS,
    CLASSIFICATION_EXECUTOR_INSTRUCTIONS,
    CLASSIFICATION_REPORTER_INSTRUCTIONS
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

# --- Thinking Planner ---
# A common thinking planner for sub-agents to structure their process.
COMMON_THINKING_INSTRUCTIONS = (
    "ROLE: Internal Monologue\n"
    "OBJECTIVE: Think step-by-step to formulate a plan to accomplish your goal. "
    "Analyze your main instructions and the data provided in the session state. "
    "Break down the task into smaller, manageable steps. "
    "Finally, provide a clear plan of action before execution."
)

thinking_planner_agent = LlmAgent(
    name="thinking_planner",
    instruction=COMMON_THINKING_INSTRUCTIONS,
    model=DEFAULT_MODEL
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
    code_executor=UnsafeLocalCodeExecutor(),
    output_key="classification_results",
    thinking_planner=thinking_planner_agent
)

# Sub-Agent: Reporter (Generates markdown summary and styled HTML report)
classification_reporter = LlmAgent(
    name="classification_reporter",
    description="Summarizes results into markdown and uses save_html_report_tool for an HTML report.",
    instruction=CLASSIFICATION_REPORTER_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    tools=[save_html_report_tool],
    output_key="classification_report",
    thinking_planner=thinking_planner_agent
)

# Initialize the Classification Agent as a SequentialAgent
# This agent orchestrates the sub-agents in a strict sequence: 
# Planner -> Executor -> Reporter (w/ HTML)
classification_agent = SequentialAgent(
    name="classification_agent",
    description="Structured classification workflow with professional reporting.",
    sub_agents=[
        classification_planner, 
        classification_executor, 
        classification_reporter
    ]
)
