"""
Centralized configuration management for PyCaretAgent.
Handles model selection and environment variable loading.
"""

import os
from dotenv import load_dotenv
from pathlib import Path

# Load sensitive and configurable parameters from .env
load_dotenv()

# Root directory of the project
ROOT_DIR = Path(__file__).parent.parent.parent

# Results directory for sessions and artifacts
RESULTS_DIR = ROOT_DIR / "results"

# Centralized Model Names using the latest Gemini versions
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gemini-3-flash-preview")

# MLflow Tracking Configuration
MLFLOW_TRACKING_URI = "http://127.0.0.1:5000"
