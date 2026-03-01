"""
Anomaly Detection Sub-Agent for PyCaretAgent.
Specializes in unsupervised outlier detection using PyCaret's Anomaly Detection module.
"""

from google.adk.agents.llm_agent import LlmAgent
from pycaretagent.utils.config import DEFAULT_MODEL
from pycaretagent.utils.instructions.anomaly_prompt import ANOMALY_INSTRUCTIONS

# Initialize the Anomaly Detection Agent with its specialized instructions
anomaly_agent = LlmAgent(
    name="anomaly_agent",
    description="Expert in anomaly detection tasks, outlier identification, and model selection.",
    instruction=ANOMALY_INSTRUCTIONS,
    model=DEFAULT_MODEL
)
