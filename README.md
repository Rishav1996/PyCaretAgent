# PyCaretAgent

`PyCaretAgent` is an autonomous AI agent framework that extends **PyCaret** with advanced reasoning and tool-use capabilities using the **Google Generative AI SDK (google-adk)**. It bridges the gap between natural language requirements and production-ready machine learning pipelines.

## 🚀 Overview

`PyCaretAgent` implements a sophisticated hierarchical and sequential agent system. A **Root Agent** (Router) orchestrates specialized **Sub-Agents** (Classification, Regression, etc.), which are themselves structured as multi-step pipelines to ensure high-precision planning and execution.

## ✨ Key Features

-   **Natural Language ML:** Trigger complex PyCaret workflows using simple English commands.
-   **Sequential Pipeline Orchestration:** Sub-agents follow a rigorous `Planner -> Executor` workflow.
-   **Advanced Reasoning (Centralized Planner):** Sub-agents leverage a centralized `BuiltInPlanner` configured in `config.py` with an optimized **4096 thinking budget** to perform deep reasoning before taking action.
-   **Integrated Research (Google Search Tool):** All agents have access to a dedicated `google_search_tool` (implemented as an `Agent` wrapped in an `AgentTool`) to research documentation for PyCaret or Pandas.
-   **Centralized State & Logic:** 
    -   **Unified Callbacks:** All execution flow logic (Session ID extraction, success signaling) is centralized in `callbacks.py` for maximum maintainability.
-   **Self-Correction & Robustness:** 
    -   **Automatic Error Recovery:** Executors are configured with `error_retry_attempts=10`, allowing the agent to automatically rerun and fix its own code if an execution error occurs.
    -   **Task Finality:** All specialized executors are instructed to provide a final summary and conclude the task upon successful completion to efficiently exit the control loop.
-   **Standardized Data Handling:** MANDATORY requirement for planners to use `pd.read_csv()` and pass the resulting DataFrame to PyCaret's `setup()`.
-   **Isolated Session Storage:** ALL session-specific artifacts (models, plots, etc.) are saved in `runs/{session_id}/`.


## 🏗️ Architecture

### 1. Root Agent
The primary orchestrator (an `Agent`) that validates user input (CSV presence via `csv_validator_tool`) and delegates tasks to the appropriate specialized sub-agent.

### 2. Specialized Sub-Agents (Pipelines)
All sub-agents (Classification, Regression, Clustering, Anomaly, Time Series) are implemented as `SequentialAgent` pipelines:
-   **Planner:** Uses centralized callbacks to extract and persist `SESSION_ID` and designs the PyCaret pipeline.
-   **Executor:** Uses the centralized `BUILTIN_PLANNER` to execute code and manage artifacts.

## 📁 Project Structure

```text
PyCaretAgent/
├── pycaretagent/
│   ├── agent.py               # Root Orchestrator (Router)
│   ├── __init__.py
│   └── utils/
│       ├── config.py          # Centralized configuration (Planners, Models)
│       ├── callbacks.py       # Centralized execution flow & state logic
│       ├── agents/            # Sequential Sub-Agent Definitions
│       │   ├── anomaly_agent.py
│       │   ├── classification_agent.py
│       │   ├── clustering_agent.py
│       │   ├── regression_agent.py
│       │   └── ts_agent.py
│       ├── instructions/      # Persona-based System Prompts (Optimized)
│       │   ├── anomaly_prompt.py
│       │   ├── classification_prompt.py
│       │   ├── clustering_prompt.py
│       │   ├── common_prompt.py
│       │   ├── google_search_prompt.py
│       │   ├── regression_prompt.py
│       │   ├── route_prompt.py
│       │   └── ts_prompt.py
│       └── tools/             # Reusable Agent Tools & Tool-Wrappers
│           ├── file_validator_tool.py
│           └── google_search_tool.py  # Agent-as-Tool implementation
├── runs/                      # Session-specific isolated artifact storage (local)
├── results/                   # Final session results and global artifacts
├── sample_dataset/            # Organized test datasets with instructions
│   ├── anomaly detection/
│   ├── classification/
│   ├── clustering/
│   ├── regression/
│   └── timeseries forecasting/
├── conductor/                 # Project management & track specifications
├── pyproject.toml             # Dependency management (uv/pip)
└── README.md                  # Project documentation
```

## 🛠️ Getting Started

### Prerequisites
-   Python 3.12 or higher.

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

### Basic Usage
Initialize the root agent and provide a path to your dataset:
```python
from pycaretagent.agent import root_agent
```
Example prompt: *"Perform a classification task on 'sample_dataset/classification/heart.csv' where the target is 'target'."*

## 📄 License
This project is licensed under the MIT License.
