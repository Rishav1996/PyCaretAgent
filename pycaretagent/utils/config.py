"""
Centralized configuration management for PyCaretAgent.
Handles model selection and environment variable loading.
"""

from dotenv import load_dotenv
from pathlib import Path
from google.adk.planners import BuiltInPlanner
from google.genai import types

# Load sensitive and configurable parameters from .env
load_dotenv()

# Root directory of the project
ROOT_DIR = Path(__file__).parent.parent.parent

# Results directory for final session results and global artifacts
RESULTS_DIR = ROOT_DIR / "results"

# Runs directory for session-specific isolated artifact storage
RUNS_DIR = ROOT_DIR / "runs"

# Centralized Model Names using the latest Gemini versions
DEFAULT_MODEL = "gemini-3.1-flash-lite-preview"
# DEFAULT_MODEL = "gemini-2.5-flash"
# DEFAULT_MODEL = "gemini-3-flash-preview"

# --- Shared Agent Components ---

# Optimized Retry Policy for handling rate-limiting (429) and transient errors.
# Wrapped in GenerateContentConfig as per ADK troubleshooting guide.
GENERATE_CONTENT_CONFIG = types.GenerateContentConfig(
    http_options=types.HttpOptions(
        retry_options=types.HttpRetryOptions(
            attempts=10,
            initial_delay=30.0,
            max_delay=60.0,
            exp_base=2,
            jitter=1.0,
            http_status_codes=[429, 500, 503]
        )
    )
)

# Centralized Planner with optimized thinking budget for complex ML tasks.
BUILTIN_PLANNER = BuiltInPlanner(
    thinking_config=types.ThinkingConfig(
        include_thoughts=True,
        thinking_budget=4096
    )
)

