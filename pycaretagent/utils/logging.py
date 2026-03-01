"""
MLflow logging utility for PyCaretAgent.
Provides callbacks to log ADK session information to MLflow.
"""

import mlflow
import os
from google.adk.agents.callback_context import CallbackContext
from pycaretagent.utils.config import MLFLOW_TRACKING_URI

def init_mlflow():
    """Initializes MLflow tracking URI."""
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    # Ensure the experiment exists
    mlflow.set_experiment("PyCaretAgent_Sessions")

def mlflow_session_logger_callback(callback_context: CallbackContext):
    """
    Callback to log the ADK session_id to MLflow.
    This runs at the start of an agent's execution.
    """
    session_id = callback_context.session
    agent_name = callback_context.agent_name
    
    # Start an MLflow run for this session
    # We use nested=True in case there's already a run active
    with mlflow.start_run(run_name=f"Session_{session_id}", nested=True):
        mlflow.log_param("session_id", session_id)
        mlflow.log_param("agent_name", agent_name)
        mlflow.log_dict({"status": "started"}, "session_info.json")
    
    return None # Allow execution to proceed
