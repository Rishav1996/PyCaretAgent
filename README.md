# PyCaretAgent

`PyCaretAgent` is an autonomous AI agent framework that extends **PyCaret** with advanced reasoning and tool-use capabilities using the **Google Generative AI SDK (google-adk)**. It bridges the gap between natural language requirements and production-ready machine learning pipelines.

## 🚀 Overview

`PyCaretAgent` implements a sophisticated hierarchical and sequential agent system. A **Root Agent** orchestrates specialized **Sub-Agents** (Classification, Regression, etc.), which are themselves structured as multi-step pipelines to ensure high-precision planning and execution.

## ✨ Key Features

-   **Natural Language ML:** Trigger complex PyCaret workflows using simple English commands.
-   **Sequential Pipeline Orchestration:** Sub-agents follow a rigorous `Planner -> Executor` workflow.
-   **Advanced Reasoning (Built-In Planner):** The sub-agents leverage the ADK `BuiltInPlanner` to perform deep reasoning and formulate step-by-step plans before taking action, ensuring higher reliability and better task decomposition.
-   **Self-Correction & Robustness:** 
    -   **Retry Logic:** `UnsafeLocalCodeExecutor` is configured with 10 retry attempts to automatically fix and re-run code on failure.
    -   **Intelligent Re-runs:** A `check_failure_status_callback` ensures that the agent only proceeds when tasks are successfully completed, skipping redundant calls based on the `check_failure_status` variable.
-   **Standardized Data Handling:** Mandatory requirement for the planning agent to use `pd.read_csv()` and pass the resulting DataFrame to PyCaret's `setup()`, ensuring high compatibility and performance.
-   **Isolated Session Storage:** ALL generated files (CSVs, plots, models, errors) are saved in a session-specific directory at `temp/{session_id}/` to ensure artifact isolation and organization.
-   **Local Code Execution:** Uses `UnsafeLocalCodeExecutor` for robust, high-performance code execution directly in the local environment.
-   **Exhaustive Experiment Tracking:** Built-in **MLflow** integration for real-time monitoring.
    -   **Metrics:** Mandatory logging of every evaluation metric (Accuracy, AUC, R2, etc.) via `mlflow.log_metric()`.
    -   **Parameters:** Mandatory logging of any custom parameters passed to PyCaret functions via `mlflow.log_param()`.
-   **Comprehensive Error Logging:** Automated capture of full tracebacks using the `traceback` module, saved to `temp/{session_id}/error.txt` and logged as MLflow artifacts.
-   **Session ID Persistence:** Automated unique Session ID generation for auditability and artifact organization.

## 🏗️ Architecture

### 1. Root Agent
The primary orchestrator (an `LlmAgent`) that validates user input (CSV presence via `csv_validator_tool`, target variable) and delegates tasks to the appropriate specialized sub-agent.

### 2. Specialized Sub-Agents (Pipelines)
All sub-agents (Classification, Regression, Clustering, Anomaly, Time Series) are implemented as `SequentialAgent` pipelines:
-   **Planner:** Designs the PyCaret pipeline, identifies the target, and generates a unique `SESSION_ID`.
-   **Executor:** (Enhanced with BuiltInPlanner) Formulates a plan, generates and executes Python code within a `try-except` block, logs metrics/params to MLflow, and saves artifacts to the session-specific `temp/` folder.

## 📁 Project Structure

```text
PyCaretAgent/
├── pycaretagent/
│   ├── agent.py               # Root Orchestrator (delegates to sub-agents)
│   ├── __init__.py
│   └── utils/
│       ├── config.py          # Global configuration (Gemini models, MLflow URI)
│       ├── agents/            # Sequential Sub-Agent Definitions (with ADK Planners)
│       │   ├── classification_agent.py
│       │   ├── regression_agent.py
│       │   ├── clustering_agent.py
│       │   ├── anomaly_agent.py
│       │   └── ts_agent.py
│       ├── instructions/      # Persona-based System Prompts
│       │   ├── common_prompt.py
│       │   ├── classification_prompt.py
│       │   ├── regression_prompt.py
│       │   ├── clustering_prompt.py
│       │   ├── anomaly_prompt.py
│       │   ├── ts_prompt.py
│       │   └── route_prompt.py
│       └── tools/             # Reusable Agent Tools
│           └── file_validator_tool.py
├── temp/                      # Session-specific isolated artifact storage (local)
├── results/                   # Final session results and global artifacts
├── conductor/                 # Project management & track specifications
├── pyproject.toml             # Dependency management (uv/pip)
├── requirements.txt           # Environment requirements
└── README.md                  # Project documentation
```

## 🛠️ Getting Started

### Prerequisites
-   Python 3.12 or higher.
-   `uv` (recommended) or `pip`.
-   A local MLflow server.

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/PyCaretAgent.git
    cd PyCaretAgent
    ```
2.  **Install dependencies:**
    ```bash
    uv pip install .
    ```
3.  **Start MLflow:**
    ```bash
    mlflow ui --port 5000
    ```

### Basic Usage
Initialize the root agent and provide a path to your dataset:
```python
from pycaretagent.agent import root_agent
# (Integration code for running the agent)
```
Example prompt: *"Perform a classification task on 'data/heart.csv' where the target is 'target'. Use all default PyCaret steps."*

## 📊 Experiment Tracking
All experiments are automatically tracked in MLflow.
-   **Experiment Name:** `[task]_{session_id}`
-   **Artifact Folders:** 
    -   `input`: Copy of the original dataset.
    -   `results`: Models, plots, and CSV outputs.
    -   `errors`: `error.txt` containing full tracebacks in case of execution failure.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
