"""
Shared callbacks for PyCaretAgent to control execution flow and manage session state.
"""

import re
from typing import Any
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmRequest, LlmResponse
from google.genai import types

def extract_session_id_callback(callback_context: CallbackContext):
    """
    Generic callback to extract the Session ID from any planner's response 
    and store it in the session state for downstream agents.
    """
    # Scan all values in the state for the SESSION_ID pattern
    for value in callback_context.state.values():
        if isinstance(value, str):
            match = re.search(r"SESSION_ID:\s*([A-Za-z0-9]+)", value)
            if match:
                session_id = match.group(1)
                callback_context.state["session_id"] = session_id
                return None
    
    return None

def check_execution_success_callback(callback_context: CallbackContext):
    """
    Generic callback to signal that an executor ran successfully.
    """
    callback_context.state["task_completed"] = True
    return None

def check_failure_status_callback(
    callback_context: CallbackContext, llm_request: LlmRequest
) -> Any:
    """
    MANDATORY: Checks 'check_failure_status' in session state.
    If False, it means the previous run succeeded, so skip redundant execution.
    """
    status = callback_context.state.get("check_failure_status")
    if status is False:
        return LlmResponse(
            content=types.Content(
                role="model",
                parts=[types.Part(text="Task already completed successfully. Skipping redundant execution.")]
            )
        )
    
    return None
