"""
Clustering Sub-Agent for PyCaretAgent.
Specializes in unsupervised grouping workflows using PyCaret's Clustering module,
implemented as a SequentialAgent for structured processing.
"""

import re
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.code_executors import UnsafeLocalCodeExecutor
from pycaretagent.utils.config import DEFAULT_MODEL
from pycaretagent.utils.tools.html_reporter_tool import save_html_report_tool
from pycaretagent.utils.instructions.clustering_prompt import (
    CLUSTERING_PLANNER_INSTRUCTIONS,
    CLUSTERING_EXECUTOR_INSTRUCTIONS,
    CLUSTERING_REPORTER_INSTRUCTIONS
)

def extract_session_id_callback(callback_context: CallbackContext):
    """
    Callback to extract the Session ID from the planner's response 
    and store it in the session state for downstream agents.
    """
    plan_text = callback_context.state.get("clustering_plan", "")
    
    match = re.search(r"SESSION_ID:\s*([A-Za-z0-9]+)", plan_text)
    if match:
        session_id = match.group(1)
        callback_context.state["session_id"] = session_id
    
    return None

# --- Thinking Planner ---
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

# Sub-Agent: Planner (Analyzes the task and plans the clustering workflow)
clustering_planner = LlmAgent(
    name="clustering_planner",
    description="Analyzes the clustering task and plans the ML workflow.",
    instruction=CLUSTERING_PLANNER_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    output_key="clustering_plan",
    after_agent_callback=extract_session_id_callback
)

# Sub-Agent: Executor (Performs training, comparison, and evaluation)
clustering_executor = LlmAgent(
    name="clustering_executor",
    description="Executes the planned clustering workflow using PyCaret functions.",
    instruction=CLUSTERING_EXECUTOR_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    code_executor=UnsafeLocalCodeExecutor(),
    output_key="clustering_results",
    thinking_planner=thinking_planner_agent
)

# Sub-Agent: Reporter (Generates markdown summary and styled HTML report)
clustering_reporter = LlmAgent(
    name="clustering_reporter",
    description="Summarizes results into markdown and uses save_html_report_tool for an HTML report.",
    instruction=CLUSTERING_REPORTER_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    tools=[save_html_report_tool],
    output_key="clustering_report",
    thinking_planner=thinking_planner_agent
)

# Initialize the Clustering Agent as a SequentialAgent
# This agent orchestrates the sub-agents in a strict sequence: 
# Planner -> Executor -> Reporter (w/ HTML)
clustering_agent = SequentialAgent(
    name="clustering_agent",
    description="Structured clustering workflow with professional reporting.",
    sub_agents=[
        clustering_planner, 
        clustering_executor, 
        clustering_reporter
    ]
)
