# PyCaretAgent

`PyCaretAgent` is an autonomous AI agent framework that extends **PyCaret** with advanced reasoning and tool-use capabilities using the **Google Generative AI SDK (google-adk)**. It bridges the gap between natural language requirements and production-ready machine learning pipelines.

## 🚀 Overview

`PyCaretAgent` implements a sophisticated hierarchical and sequential agent system. A **Root Agent** orchestrates specialized **Sub-Agents** (Classification, Regression, etc.), which are themselves structured as multi-step pipelines to ensure high-precision planning, execution, and professional reporting.

## ✨ Key Features

-   **Natural Language ML:** Trigger complex PyCaret workflows using simple English commands.
-   **Sequential Pipeline Orchestration:** Sub-agents follow a rigorous `Planner -> Executor -> Reporter` workflow.
-   **Intelligent Planning:** Lead ML Architect persona designs the pipeline based on dataset characteristics and filtered PyCaret functions.
-   **Automated Execution:** ML Automation persona executes Python code, handling imports and function calls.
-   **Experiment Tracking:** Built-in **MLflow** integration for real-time monitoring of parameters, metrics, and models at `http://127.0.0.1:5000`.
-   **Professional Reporting:** Automated generation of high-quality Markdown summaries and styled HTML reports for every session.
-   **Session ID Persistence:** Automated unique Session ID generation (`SESSION_ID`) for auditability and artifact organization.
-   **Safe Data Handling:** "No Memory" rule ensures large datasets are never read into memory; file paths are passed directly to PyCaret's `setup()`.

## 🏗️ Architecture

### 1. Root Agent
The primary orchestrator that validates user input (CSV presence, target variable) and delegates tasks to the appropriate specialized sub-agent.

### 2. Specialized Sub-Agents (Pipelines)
All sub-agents (Classification, Regression, Clustering, Anomaly, Time Series) are implemented as `SequentialAgent` pipelines:
-   **Planner:** Designs the PyCaret pipeline, identifies the target, and generates a unique `SESSION_ID`.
-   **Executor:** Executes the code, logs metrics/params to MLflow, and saves artifacts (models, plots).
-   **Reporter:** Synthesizes results into a professional Markdown summary and a styled HTML report.

## 📁 Project Structure

```text
PyCaretAgent/
├── pycaretagent/
│   ├── agent.py               # Root Orchestrator (delegates to sub-agents)
│   ├── __init__.py
│   └── utils/
│       ├── config.py          # Global configuration (Gemini models, MLflow URI)
│       ├── agents/            # Sequential Sub-Agent Definitions
│       │   ├── classification_agent.py # Planner -> Executor -> Reporter
│       │   ├── regression_agent.py     # Planner -> Executor -> Reporter
│       │   ├── clustering_agent.py     # Planner -> Executor -> Reporter
│       │   ├── anomaly_agent.py        # Planner -> Executor -> Reporter
│       │   └── ts_agent.py             # Planner -> Executor -> Reporter
│       ├── instructions/      # Persona-based System Prompts
│       │   ├── common_prompt.py        # Shared PyCaret function metadata (filtered by task)
│       │   ├── classification_prompt.py
│       │   ├── regression_prompt.py
│       │   ├── clustering_prompt.py
│       │   ├── anomaly_prompt.py
│       │   ├── ts_prompt.py
│       │   └── route_prompt.py         # Root agent routing logic
│       └── tools/             # Reusable Agent Tools
│           ├── html_reporter_tool.py   # Styled HTML report generator
│           └── file_validator_tool.py  # Path validation logic
├── results/                   # Session-specific artifacts & HTML reports (local)
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
-   **Artifacts:** 
    -   Input data copy logged to `input/` folder in MLflow.
    -   All outputs (models, plots, CSVs) logged to `results/` folder in MLflow.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
