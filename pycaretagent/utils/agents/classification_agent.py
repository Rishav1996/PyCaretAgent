"""
Classification Sub-Agent for PyCaretAgent.
Specializes in categorical prediction workflows using PyCaret's Classification module,
now implemented as a SequentialAgent for more structured processing.
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
from pycaretagent.utils.instructions.classification_prompt import (
    CLASSIFICATION_PLANNER_INSTRUCTIONS,
    CLASSIFICATION_EXECUTOR_INSTRUCTIONS
)

# Sub-Agent: Planner (Analyzes the task and plans the workflow)
classification_planner = LlmAgent(
    name="classification_planner",
    description="Analyzes the classification task and plans the ML workflow.",
    instruction=CLASSIFICATION_PLANNER_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    generate_content_config=GENERATE_CONTENT_CONFIG,
    output_key="classification_plan",
    tools=[google_search_tool],
    after_agent_callback=extract_session_id_callback
)

# Sub-Agent: Executor (Performs training, comparison, and evaluation)
classification_executor = LlmAgent(
    name="classification_executor",
    description="Executes the planned classification workflow using PyCaret functions.",
    instruction=CLASSIFICATION_EXECUTOR_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    generate_content_config=GENERATE_CONTENT_CONFIG,
    code_executor=UnsafeLocalCodeExecutor(error_retry_attempts=10),
    planner=BUILTIN_PLANNER,
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
