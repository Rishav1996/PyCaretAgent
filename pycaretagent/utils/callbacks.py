"""
Shared callbacks for PyCaretAgent to control execution flow and manage session state.
"""

import re
from google.adk.agents.callback_context import CallbackContext

def extract_session_id_callback(callback_context: CallbackContext):
    """
    Generic callback to extract the Session ID from any planner's response 
    and store it in the session state for downstream agents.
    """
    # Scan all values in the state for the SESSION_ID pattern
    # callback_context.state is a State object, use to_dict() to get values
    state_dict = callback_context.state.to_dict()
    for value in state_dict.values():
        if isinstance(value, str):
            match = re.search(r"SESSION_ID:\s*([A-Za-z0-9]+)", value)
            if match:
                session_id = match.group(1)
                callback_context.state["session_id"] = session_id
                return None
    
    return None
