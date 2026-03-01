"""
Classification Sub-Agent for PyCaretAgent.
Specializes in categorical prediction workflows using PyCaret's Classification module.
"""

from google.adk.agents.llm_agent import LlmAgent
from pycaretagent.utils.config import DEFAULT_MODEL
from pycaretagent.utils.instructions.classification_prompt import CLASSIFICATION_INSTRUCTIONS

# Initialize the Classification Agent with its specialized instructions
classification_agent = LlmAgent(
    name="classification_agent",
    description="Expert in classification tasks, automated feature engineering, and model selection.",
    instruction=CLASSIFICATION_INSTRUCTIONS,
    model=DEFAULT_MODEL
)
