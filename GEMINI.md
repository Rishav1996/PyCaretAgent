# PyCaretAgent

## Project Overview

`PyCaretAgent` is an agentic extension of the **PyCaret** library. It leverages the **Google Generative AI SDK (google-adk)** to create a hierarchical and sequential agent system:
- **Root Agent (Router):** The primary entry point (an `Agent`) that interacts with the user, validates requirements, and delegates work.
- **Specialized Sub-Agents:** Tasks like Classification and Regression are structured as `SequentialAgent` pipelines:
    - **Planner Agent:** Designs the ML workflow, performs technical research using the `google_search_tool`, and generates a Session ID.
    - **Executor Agent:** Enhanced with a centralized `BUILTIN_PLANNER` (4096 thinking budget), it executes Python code and performs real-time research.


The project facilitates a complete machine learning lifecycle, starting from automated data analysis and preprocessing, moving through model training and optimization, and concluding with model deployment.

## Tech Stack

- **Python:** 3.12+
- **AutoML Core:** [PyCaret](https://pycaret.org/)
- **Agent Orchestration:** [Google Generative AI SDK](https://github.com/google-gemini/google-adk) (`google-adk`)
- **Data Engine:** [DuckDB](https://duckdb.org/)
- **Search Tool:** Google Search grounding via ADK.
- **Dependency Management:** `uv` / `pip`

## Project Structure

- `pycaretagent/`: Core package.
    - `agent.py`: Orchestrating Root Agent (Router).
    - `utils/`: Core utilities and helper functions.
        - `config.py`: Centralized configuration (Models and Shared Planners).
        - `callbacks.py`: Centralized execution flow logic (Session ID extraction, state management).
        - `agents/`: Specialized Sub-Agent definitions (Classification, Regression, etc.).
        - `instructions/`: Optimized persona-based system prompts.
        - `tools/`: Reusable agent tools and tool-wrappers.
            - `file_validator_tool.py`: CSV path validation.
            - `google_search_tool.py`: Agent-as-Tool implementation for integrated research.
- `runs/`: Local storage for session-specific artifacts (`{session_id}/`).
- `results/`: Final session results and global artifacts.
- `sample_dataset/`: Organized test data with usage instructions.
    - `anomaly detection/`
    - `classification/`
    - `clustering/`
    - `regression/`
    - `timeseries forecasting/`
- `conductor/`: Project management and detailed specifications.
- `GEMINI.md`: Project-specific instructions and context for Gemini CLI (this file).

## Development Guidelines

- **Agent Hierarchy & Sequence:** Maintain the distinction between the Root Router and Sub-Agent pipelines. Ensure sub-agents follow the Planner -> Executor sequence.
- **Import Convention:** Always use `google.adk` for imports from the Google Generative AI SDK.
- **Centralized Components:**
    - **Planners:** Use the `BUILTIN_PLANNER` (4096 budget) from `config.py` for all executors.
    - **Callbacks:** All flow-control logic must reside in `callbacks.py`.
- **Agent-as-Tool Pattern:** Complex tool behaviors (like research) must be implemented as an internal `Agent` wrapped in an `AgentTool` to enable direct, synchronous invocation.
- **Instruction Management:** Prompts must be centralized in `pycaretagent/utils/instructions/`. Use the `SHARED_SEARCH_INSTRUCTIONS` to inform agents of their research capabilities.
- **Data Handling:** MANDATORY: All planning agents must plan to read CSV files using `pd.read_csv()` and pass the resulting DataFrame to PyCaret's `setup()`.
- **Error Resilience:** Executors use `error_retry_attempts=10` to automatically rerun and fix code on failure. 
- **Task Finality:** Executors are instructed to provide a final summary and conclude the task upon successful completion to exit the agent's control loop.
- **State Management:** Use the session state (`callback_context.state`) to pass Session IDs and task status between agents in the pipeline.

## Conductor Context

Refer to `conductor/index.md` for detailed product requirements, track progress, and the evolving implementation plan as guided by the user.
