# PyCaretAgent

## Project Overview

`PyCaretAgent` is an agentic extension of the **PyCaret** library. It leverages the **Google Generative AI SDK (google-adk)** to create a high-precision autonomous ML system:
- **Root Agent (Router):** The primary entry point (an `Agent`) that interacts with the user, validates requirements (e.g., CSV existence), and delegates work.
- **Specialized Sub-Agents:** Tasks like Classification and Regression are handled by **Senior ML Automation Architects** (executors) that manage the entire ML lifecycle in a unified flow.
- **Offline-First Architecture:** The system is designed for high-precision autonomous execution using local tools and analytics, eliminating dependency on internet-based research agents.

The project facilitates a complete machine learning lifecycle
, starting from automated data analysis and schema discovery, moving through model training and comparison, and concluding with model persistence and code archiving.

## Tech Stack

- **Python:** 3.12+
- **AutoML Core:** [PyCaret](https://pycaret.org/)
- **Agent Orchestration:** [Google Generative AI SDK](https://github.com/google-gemini/google-adk) (`google-adk`)
- **Data Engine:** [DuckDB](https://duckdb.org/)
- **Dependency Management:** `uv` / `pip`

## Project Structure

- `pycaretagent/`: Core package.
    - `agent.py`: Orchestrating Root Agent (Router).
    - `utils/`: Core utilities and helper functions.
        - `config.py`: Centralized configuration (Models and Shared Planners).
        - `callbacks.py`: Centralized execution flow logic (Session ID extraction, state management).
        - `agents/`: Specialized Sub-Agent definitions (Classification, Regression, etc.).
        - `instructions/`: Role-based system prompts (Senior ML Automation Architect).
        - `tools/`: Reusable agent tools.
            - `file_validator_tool.py`: CSV path validation.
            - `csv_analytics_tool.py`: Programmatic pandas metadata retrieval (info, describe).
            - `session_id_generator_tool.py`: Unique run identification.
- `runs/`: Local storage for session-specific artifacts (`{session_id}/`).
    - Sub-folders: `plots/`, `models/`, `metrics/`.
- `sample_dataset/`: Organized test data with usage instructions.
- `conductor/`: Project management and detailed specifications.
- `GEMINI.md`: Project-specific instructions and context for Gemini CLI (this file).

## Development Guidelines

- **Simplified Agent Architecture:** Sub-agents are single-agent executors (Automation Architects) that handle analysis, planning, and code execution.
- **Import Convention:** Always use `google.adk` for imports from the Google Generative AI SDK.
- **Centralized Components:**
    - **Planners:** Use the `BUILTIN_PLANNER` (4096 budget) from `config.py` for all sub-agents.
    - **Callbacks:** Flow-control logic resides in `callbacks.py`.
- **Data Intelligence:** MANDATORY: Use `csv_analytics_tool` to evaluate schemas before designing the PyCaret setup.
- **Session Tracking:** MANDATORY: Call `session_id_generator_tool` at the start of every run to establish directory isolation.
- **Instruction Management:** Prompts are centralized in `pycaretagent/utils/instructions/`. Use the `SHARED_SEARCH_INSTRUCTIONS` for consistent research and data analytics protocols. **MANDATORY: Agents must use ONLY the provided PyCaret functions.**
- **Error Resilience:** Agents use `error_retry_attempts=10` to automatically fix code on failure. 
- **Task Finality:** Agents must provide a final summary and conclude the task to exit the control loop upon success.
- **Workspace Hierarchy:** All artifacts must be saved under `runs/{session_id?}/` and organized into `plots/`, `models/`, and `metrics/`.

## Conductor Context

Refer to `conductor/index.md` for detailed product requirements, track progress, and the evolving implementation plan.
