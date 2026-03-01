"""
Time Series Sub-Agent for PyCaretAgent.
Specializes in forecasting workflows using PyCaret's Time Series module.
"""

from google.adk.agents.llm_agent import LlmAgent
from pycaretagent.utils.config import DEFAULT_MODEL
from pycaretagent.utils.instructions.ts_prompt import TS_INSTRUCTIONS

# Initialize the Time Series Agent with its specialized instructions
ts_agent = LlmAgent(
    name="ts_agent",
    description="Expert in time series forecasting tasks, stationarity testing, and model selection.",
    instruction=TS_INSTRUCTIONS,
    model=DEFAULT_MODEL
)
