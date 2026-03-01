# PyCaretAgent

`PyCaretAgent` is an autonomous AI agent framework that extends **PyCaret** with advanced reasoning and tool-use capabilities using the **Google Generative AI SDK (google-adk)**. It bridges the gap between natural language requirements and production-ready machine learning pipelines.

## 🚀 Overview

`PyCaretAgent` implements a sophisticated hierarchical and sequential agent system. A **Root Agent** orchestrates specialized **Sub-Agents** (Classification, Regression, etc.), which are themselves structured as multi-step pipelines to ensure high-precision planning, execution, and professional reporting.

## ✨ Key Features

-   **Natural Language ML:** Trigger complex PyCaret workflows using simple English commands.
-   **Sequential Pipeline Orchestration:** Sub-agents follow a rigorous `Planner -> Executor -> Reporter` workflow.
-   **Intelligent Planning:** Lead ML Architect persona designs the pipeline based on dataset characteristics.
-   **Automated Execution:** ML Automation persona executes Python code via `BuiltInCodeExecutor`, handling imports and function calls.
-   **Experiment Tracking:** Built-in **MLflow** integration for real-time monitoring of parameters, metrics, and models at `http://127.0.0.1:5000`.
-   **Professional Reporting:** Automated generation of high-quality Markdown summaries and styled HTML reports for every session.
-   **Session ID Persistence:** Automated unique Session ID generation (`SESSION_ID`) for auditability and artifact organization.
-   **Safe Data Handling:** "No Memory" rule ensures large datasets are never read into memory; file paths are passed directly to PyCaret's `setup()`.

## 🏗️ Architecture

### 1. Root Agent
The primary orchestrator that validates user input (CSV presence, target variable) and delegates tasks to the appropriate specialized sub-agent.

### 2. Specialized Sub-Agents (Pipelines)
Both **Classification** and **Regression** agents are implemented as `SequentialAgent` pipelines:
-   **Planner:** Designs the PyCaret pipeline, identifies the target, and generates a unique `SESSION_ID`.
-   **Executor:** Executes the code, logs metrics/params to MLflow, and saves artifacts (models, plots).
-   **Reporter:** Synthesizes results into a professional Markdown summary and a styled HTML report.

## 📁 Project Structure

```text
PyCaretAgent/
├── pycaretagent/
│   ├── agent.py               # Root Orchestrator (validates input & delegates)
│   ├── __init__.py
│   └── utils/
│       ├── config.py          # Global settings (Model names, MLflow URI)
│       ├── agents/            # Sub-Agent definitions
│       │   ├── classification_agent.py # Sequential: Planner -> Executor -> Reporter
│       │   ├── regression_agent.py     # Sequential: Planner -> Executor -> Reporter
│       │   ├── anomaly_agent.py
│       │   ├── clustering_agent.py
│       │   └── ts_agent.py
│       ├── instructions/      # Optimized system prompts
│       │   ├── common_prompt.py        # Shared PyCaret function metadata
│       │   ├── classification_prompt.py
│       │   ├── regression_prompt.py
│       │   └── route_prompt.py         # Root agent routing logic
│       └── tools/             # Reusable agent tools
│           ├── html_reporter_tool.py   # Saves styled HTML reports to results/
│           └── file_validator_tool.py  # Ensures datasets exist before processing
├── results/                   # local storage for Session Artifacts & HTML Reports
├── conductor/                 # Project management & workflow specifications
├── pyproject.toml             # Project dependencies and metadata
├── requirements.txt           # Flat dependency list
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
-   **Experiment Name:** `classification_{session_id}` or `regression_{session_id}`
-   **Artifacts:** Input data copy (`input/`), saved models, and plots are stored under `results/`.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
