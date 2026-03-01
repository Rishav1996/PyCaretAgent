"""
Clustering Sub-Agent for PyCaretAgent.
Specializes in unsupervised grouping workflows using PyCaret's Clustering module.
"""

from google.adk.agents.llm_agent import LlmAgent
from pycaretagent.utils.config import DEFAULT_MODEL
from pycaretagent.utils.instructions.clustering_prompt import CLUSTERING_INSTRUCTIONS

# Initialize the Clustering Agent with its specialized instructions
clustering_agent = LlmAgent(
    name="clustering_agent",
    description="Expert in clustering tasks, unsupervised pattern discovery, and model selection.",
    instruction=CLUSTERING_INSTRUCTIONS,
    model=DEFAULT_MODEL
)
