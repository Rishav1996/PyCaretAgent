"""
Regression Sub-Agent for PyCaretAgent.
Specializes in numerical value prediction using PyCaret's Regression module.
"""

from google.adk.agents.llm_agent import LlmAgent
from pycaretagent.utils.config import DEFAULT_MODEL
from pycaretagent.utils.instructions.regression_prompt import REGRESSION_INSTRUCTIONS

# Initialize the Regression Agent with its specialized instructions
regression_agent = LlmAgent(
    name="regression_agent",
    description="Expert in regression tasks, error analysis, and optimization.",
    instruction=REGRESSION_INSTRUCTIONS,
    model=DEFAULT_MODEL
)
