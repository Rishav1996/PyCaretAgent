# PyCaretAgent

## Project Overview

`PyCaretAgent` is an agentic extension of the **PyCaret** library. It leverages the **Google Generative AI SDK (google-adk)** to create a hierarchical and sequential agent system:
- **Root Agent:** The primary entry point that interacts with the user, validates requirements, and delegates work.
- **Sequential Sub-Agents:** Specialized sub-agents (Classification, Regression, etc.) are structured as pipelines:
    - **Planner Agent:** Designs the ML workflow and generates a Session ID.
    - **Executor Agent:** Runs Python code via `UnsafeLocalCodeExecutor` and logs to MLflow.

The project facilitates a complete machine learning lifecycle, starting from automated data analysis and preprocessing, moving through model training and optimization, and concluding with model deployment on cloud platforms.

## Tech Stack

- **Python:** 3.12+
- **AutoML Core:** [PyCaret](https://pycaret.org/)
- **Agent Orchestration:** [Google Generative AI SDK](https://github.com/google-gemini/google-adk) (`google-adk`)
- **Experiment Tracking:** [MLflow](https://mlflow.org/) (Running on `http://127.0.0.1:5000`)
- **Data Engine:** [DuckDB](https://duckdb.org/)
- **Cloud Deployment:** (Targeting AWS, Azure, GCP via PyCaret's deployment features)
- **Dependency Management:** `uv` / `pip`

## Project Structure

- `pycaretagent/`: Core package.
    - `agent.py`: Orchestrating Root Agent.
    - `utils/`: Core utilities and helper functions.
        - `agents/`: Specialized Sub-Agent definitions (Classification, Regression, etc.).
        - `instructions/`: Centralized prompt templates.
            - `common_prompt.py`: Shared PyCaret function data.
        - `tools/`: Reusable agent tools (e.g., `file_validator_tool.py`).
        - `config.py`: Global configuration and MLflow settings.
- `results/`: Local storage for session artifacts and input data copies.
- `conductor/`: Project management and detailed specifications.
- `GEMINI.md`: Project-specific instructions and context for Gemini CLI (this file).

## Development Guidelines

- **Agent Hierarchy & Sequence:** Maintain the distinction between Root and Sub-Agents. Ensure sub-agents follow the Planner -> Executor sequence for consistency.
- **Import Convention:** Always use `google.adk` for imports from the Google Generative AI SDK, never `google_adk`.
- **Instruction Management:** Prompts must be centralized in `pycaretagent/utils/instructions/` and utilize state placeholders like `{session_id}`.
- **Data Handling:** Never read entire datasets into memory. Always pass file paths as literal strings to PyCaret's `setup()` function.
- **Experiment Tracking:** Every execution must be tracked in MLflow under an experiment named `[task]_{session_id}`.
- **Tool Logic:** Reusable tools should be placed in `pycaretagent/utils/tools/`.
- **PyCaret Integration:** Deeply integrate with PyCaret's functional API. The agents should act as intelligent wrappers around PyCaret functions.
- **End-to-End Lifecycle:** Every workflow should consider the path from raw data to a deployed cloud endpoint.
- **State Management:** Use the session state to pass data (like Session IDs and plans) between agents in the pipeline.

## Conductor Context

Refer to `conductor/index.md` for detailed product requirements, track progress, and the evolving implementation plan as guided by the user.
