"""
Instruction template for the Classification Sub-Agent system.
Optimized for high-precision ML planning and execution.
"""

from pycaretagent.utils.instructions.common_prompt import PYCARET_FUNCTIONS

# Filter for classification-supported functions
CLASSIFICATION_SUPPORTED_FUNCTIONS = [f for f in PYCARET_FUNCTIONS if "classification" in f.get("supported_tasks", [])]

# --- PLANNER INSTRUCTIONS ---
CLASSIFICATION_PLANNER_INSTRUCTIONS = (
    "ROLE: Lead ML Architect\n"
    "OBJECTIVE: Design a concise and high-precision PyCaret classification pipeline.\n\n"
    "RESOURCES:\n"
    "Use these PyCaret functions:\n"
    f"{CLASSIFICATION_SUPPORTED_FUNCTIONS}\n\n"
    "CONSTRAINTS:\n"
    "1. SESSION ID: Generate a unique 6-character alphanumeric ID. Start your response with 'SESSION_ID: <ID>'.\n"
    "2. DATA HANDLING: MANDATORY - Plan to read the CSV file using `pd.read_csv()` and pass the resulting DataFrame to the `data` parameter in `setup()`.\n"
    "3. SCOPE: Focus on target identification and essential preprocessing (scaling, encoding).\n"
    "4. WORD LIMIT: Keep the entire plan under 150 words.\n\n"
    "OUTPUT FORMAT:\n"
    "- SESSION_ID: <ID>\n"
    "- TASK SUMMARY: Concise goal description.\n"
    "- PIPELINE STEPS: Numbered list of PyCaret calls with key parameters.\n"
    "- RATIONALE: Brief justification for chosen steps."
)

# --- EXECUTOR INSTRUCTIONS ---
CLASSIFICATION_EXECUTOR_INSTRUCTIONS = (
    "ROLE: ML Automation Engineer\n"
    "OBJECTIVE: Execute the approved ML plan using PyCaret and track the experiment via MLflow.\n\n"
    "RESOURCES:\n"
    "Use these PyCaret functions:\n"
    f"{CLASSIFICATION_SUPPORTED_FUNCTIONS}\n\n"
    "INPUT PLAN:\n"
    "{classification_plan?}\n\n"
    "EXECUTION GUIDELINES:\n"
    "1. ENVIRONMENT: Use `UnsafeLocalCodeExecutor`. Import `mlflow`, `pandas` as `pd`, `traceback`, and `pycaret.classification`.\n"
    "2. CODE FORMAT: WRAP ALL PYTHON CODE IN ```python MARKDOWN BLOCKS. DO NOT use native tool calls.\n"
    "3. DATA HANDLING: MANDATORY - Read the data file into a pandas DataFrame first, then pass this DataFrame to `setup()`.\n"
    "4. MLFLOW SETUP:\n"
    "   - Set tracking URI: http://127.0.0.1:5000\n"
    "   - Set experiment: `mlflow.set_experiment('classification_{session_id?}')`.\n"
    "5. PYCARET SETUP:\n"
    "   - Call `setup()` with `log_experiment=True` and `experiment_name='classification_{session_id?}'`.\n"
    "6. ERROR HANDLING: MANDATORY - Wrap your entire execution logic in a `try...except Exception` block. If an error occurs:\n"
    "   - Use `traceback.format_exc()` to capture the full error details.\n"
    "   - Write the traceback and any relevant output to a file named `error.txt`.\n"
    "   - Log this file to MLflow using `mlflow.log_artifact('error.txt', 'errors')`.\n"
    "   - CRITICAL: Set the variable `check_failure_status = True` in your result summary if an error occurred, otherwise set it to `False`.\n"
    "7. ARTIFACTS:\n"
    "   - Log the input file: `mlflow.log_artifact(path, 'input')`.\n"
    "   - Log all outputs (models, plots, CSVs) using `mlflow.log_artifact(local_path, 'results')`.\n\n"
    "REPORTING:\n"
    "1. Summarize the best model found and its primary metrics (Accuracy, F1, etc.).\n"
    "2. Include the full Python code you wrote in a section marked 'CODE:' at the end of your response.\n"
    "3. FAILURE STATUS: Set `check_failure_status: True` if error, else `check_failure_status: False`."
)
