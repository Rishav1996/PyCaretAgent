# PyCaretAgent

## Project Overview

`PyCaretAgent` is an agentic extension of the **PyCaret** library. It leverages the **Google Generative AI SDK (google-adk)** to create a hierarchical agent system:
- **Root Agent:** The primary entry point that interacts with the user, validates requirements (CSV, target, task type), and delegates work.
- **Sub-Agents:** Specialized agents for specific machine learning tasks:
    - **Classification Agent**: Handles categorical prediction.
    - **Regression Agent**: Handles numerical value prediction.
    - **Clustering Agent**: Handles unsupervised grouping.
    - **Anomaly Agent**: Handles outlier detection.
    - **Time Series Agent**: Handles forecasting.

The project facilitates a complete machine learning lifecycle, starting from automated data analysis and preprocessing, moving through model training and optimization, and concluding with model deployment on cloud platforms.

## Tech Stack

- **Python:** 3.12+
- **AutoML Core:** [PyCaret](https://pycaret.org/)
- **Agent Orchestration:** [Google Generative AI SDK](https://github.com/google-gemini/google-adk) (`google-adk`)
- **Experiment Tracking:** [MLflow](https://mlflow.org/)
- **Data Engine:** [DuckDB](https://duckdb.org/)
- **Cloud Deployment:** (Targeting AWS, Azure, GCP via PyCaret's deployment features)
- **Dependency Management:** `uv` / `pip`

## Project Structure

- `pycaretagent/`: Core package.
    - `agent.py`: Orchestrating Root Agent.
    - `utils/`: Core utilities and helper functions.
        - `agents/`: Specialized Sub-Agent definitions (Classification, Regression, Clustering, Anomaly, Time Series).
        - `instructions/`: Centralized prompt templates for all agents.
        - `tools/`: Reusable agent tools (e.g., `file_validator_tool.py`).
        - `config.py`: Global configuration and model settings.
        - `logging.py`: MLflow logging utilities and callbacks.
- `log/`: Local storage for MLflow session logs.
- `conductor/`: Project management and detailed specifications.
- `GEMINI.md`: Project-specific instructions and context for Gemini CLI (this file).

## Development Guidelines

- **Agent Hierarchy:** Always maintain the distinction between Root and Sub-Agents. Tools should be granular and specific to the agent's domain.
- **Import Convention:** Always use `google.adk` for imports from the Google Generative AI SDK, never `google_adk`.
- **Instruction Management:** Prompts must be centralized in `pycaretagent/utils/instructions/` for consistency and easier tuning.
- **Tool Logic:** Reusable tools should be placed in `pycaretagent/utils/tools/`.
- **PyCaret Integration:** Deeply integrate with PyCaret's functional API. The agents should act as intelligent wrappers around PyCaret functions.
- **End-to-End Lifecycle:** Every workflow should consider the path from raw data to a deployed cloud endpoint.
- **State Management:** Use DuckDB or shared state objects to pass data and context between agents.
- **Environment Variables:** Use `.env` and `pycaretagent/utils/config.py` for all configurable parameters like model names and API keys.

## Conductor Context

Refer to `conductor/index.md` for detailed product requirements, track progress, and the evolving implementation plan as guided by the user.
