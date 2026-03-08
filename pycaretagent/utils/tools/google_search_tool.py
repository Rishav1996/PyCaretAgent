"""
Google Search Sub-Agent for PyCaretAgent.
Specializes in performing internet research using the Google Search tool.
"""

from google.adk import Agent
from google.adk.tools import google_search, AgentTool
from pycaretagent.utils.config import DEFAULT_MODEL, GENERATE_CONTENT_CONFIG
from pycaretagent.utils.instructions.google_search_prompt import GOOGLE_SEARCH_INSTRUCTIONS

# Internal Agent for search operations
_google_search_agent = Agent(
    name="google_search_tool",
    description="Tool whose job it is to perform Google search queries and answer questions about results.",
    instruction=GOOGLE_SEARCH_INSTRUCTIONS,
    model=DEFAULT_MODEL,
    generate_content_config=GENERATE_CONTENT_CONFIG,
    tools=[google_search]
)

# Export as an AgentTool
google_search_tool = AgentTool(agent=_google_search_agent)
