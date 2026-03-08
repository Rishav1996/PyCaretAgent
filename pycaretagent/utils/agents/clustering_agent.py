"""
Clustering Sub-Agent for PyCaretAgent.
Specializes in unsupervised grouping workflows using PyCaret's Clustering module,
implemented as a SequentialAgent for structured processing.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.code_executors import UnsafeLocalCodeExecutor
from pycaretagent.utils.config import DEFAULT_MODEL, BUILTIN_PLANNER, GENERATE_CONTENT_CONFIG
from pycaretagent.utils.callbacks import (
    extract_session_id_callback, 
    check_execution_success_callback
)
from pycaretagent.utils.tools.google_search_tool import google_search_tool
from pycaretagent.utils.instructions.clustering_prompt import (
    CLUSTERING_PLANNER_INSTRUCTIONS,
    CLUSTERING_EXECUTOR_INSTRUCTIONS
)

# Sub-Agent: Planner (Analyzes the task and plans the clustering workflow)
clustering_planner = LlmAgent(
    name="clustering_planner",
    description="Analyzes the clustering task and plans the ML workflow.",
    instruction=CLUSTERING_PLANNER_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    generate_content_config=GENERATE_CONTENT_CONFIG,
    output_key="clustering_plan",
    tools=[google_search_tool],
    after_agent_callback=extract_session_id_callback
)

# Sub-Agent: Executor (Performs training, comparison, and evaluation)
clustering_executor = LlmAgent(
    name="clustering_executor",
    description="Executes the planned clustering workflow using PyCaret functions.",
    instruction=CLUSTERING_EXECUTOR_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    generate_content_config=GENERATE_CONTENT_CONFIG,
    code_executor=UnsafeLocalCodeExecutor(error_retry_attempts=10),
    planner=BUILTIN_PLANNER,
    after_agent_callback=check_execution_success_callback
)

# Initialize the Clustering Agent as a SequentialAgent
# This agent orchestrates the sub-agents in a strict sequence: 
# Planner -> Executor
clustering_agent = SequentialAgent(
    name="clustering_agent",
    description="Structured clustering workflow.",
    sub_agents=[
        clustering_planner, 
        clustering_executor
    ]
)
