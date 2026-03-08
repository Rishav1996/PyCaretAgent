"""
Anomaly Detection Sub-Agent for PyCaretAgent.
Specializes in unsupervised outlier detection using PyCaret's Anomaly Detection module,
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
from pycaretagent.utils.instructions.anomaly_prompt import (
    ANOMALY_PLANNER_INSTRUCTIONS,
    ANOMALY_EXECUTOR_INSTRUCTIONS
)

# Sub-Agent: Planner (Analyzes the task and plans the anomaly detection workflow)
anomaly_planner = LlmAgent(
    name="anomaly_planner",
    description="Analyzes the anomaly detection task and plans the ML workflow.",
    instruction=ANOMALY_PLANNER_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    output_key="anomaly_plan",
    tools=[google_search_tool],
    after_agent_callback=extract_session_id_callback
)

# Sub-Agent: Executor (Performs training, comparison, and evaluation)
anomaly_executor = LlmAgent(
    name="anomaly_executor",
    description="Executes the planned anomaly detection workflow using PyCaret functions.",
    instruction=ANOMALY_EXECUTOR_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    code_executor=UnsafeLocalCodeExecutor(),
    planner=BUILTIN_PLANNER,
    tools=[google_search_tool],
    before_model_callback=check_failure_status_callback,
    after_agent_callback=check_execution_success_callback
)


# Initialize the Anomaly Agent as a SequentialAgent
# This agent orchestrates the sub-agents in a strict sequence: 
# Planner -> Executor
anomaly_agent = SequentialAgent(
    name="anomaly_agent",
    description="Structured anomaly detection workflow.",
    sub_agents=[
        anomaly_planner, 
        anomaly_executor
    ]
)
