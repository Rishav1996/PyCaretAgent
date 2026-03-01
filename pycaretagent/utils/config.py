"""
Centralized configuration management for PyCaretAgent.
Handles model selection and environment variable loading.
"""

import os
from dotenv import load_dotenv

# Load sensitive and configurable parameters from .env
load_dotenv()

# Centralized Model Names using the latest Gemini versions
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gemini-3-flash-preview")

# MLflow Tracking Configuration
# Logs will be sent to the local MLflow server
MLFLOW_TRACKING_URI = "http://127.0.0.1:5000"

# Configuration map for easy extension and access across the project
MODEL_CONFIG = {
    "default": DEFAULT_MODEL,
    "mlflow_tracking_uri": MLFLOW_TRACKING_URI
}
