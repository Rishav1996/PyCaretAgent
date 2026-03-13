# PyCaretAgent

`PyCaretAgent` is an autonomous AI agent framework that extends **PyCaret** with advanced reasoning and tool-use capabilities using the **Google Generative AI SDK (google-adk)**. It bridges the gap between natural language requirements and production-ready machine learning pipelines.

## 🚀 Overview

`PyCaretAgent` implements a high-precision autonomous ML system. A **Supervisor Agent** (Router) orchestrates specialized **Sub-Agents** (Classification, Regression, etc.), which are designed as **Senior ML Automation Architects** capable of handling the entire lifecycle from data intelligence to model persistence.

## ✨ Key Features

-   **Natural Language ML:** Trigger complex PyCaret workflows using simple English commands.
-   **Autonomous ML Lifecycle:** Sub-agents handle analysis, planning, and execution in a single unified flow.
-   **Offline-First Architectural Design:** Focused on high-precision execution without dependency on external internet research tools.
-   **Advanced Reasoning (Centralized Planner):** All agents leverage a centralized `BuiltInPlanner` configured with an optimized **4096 thinking budget** for deep architectural reasoning.
-   **Data Intelligence:** Uses a dedicated `csv_analytics_tool` to programmatically retrieve schemas, distributions, and null counts before pipeline design.
-   **Code Execution & Function Limits:**
    -   **Strict Function Limit:** Agents are mandated to use ONLY the provided PyCaret functions listed in the instructions.
    -   **Markdown Code Execution:** Uses the ADK's internal code execution triggered by ```python markdown blocks.
-   **Programmatic Session Tracking:** Uses `session_id_generator_tool` to ensure every run is uniquely identified and isolated.
-   **Structured Workspace Management:** Automatically creates and organizes artifacts into `plots/`, `models/`, and `metrics/` sub-directories within isolated session folders.
-   **Self-Correction & Robustness:** 
    -   **Automatic Error Recovery:** Executors use `error_retry_attempts=10` to automatically rerun and fix code on failure.
    -   **Task Finality:** Agents provide comprehensive final summaries and conclude tasks to exit the control loop efficiently.
-   **Isolated Session Storage:** ALL session-specific artifacts are saved in `runs/{session_id}/`.

## 🏗️ Architecture

### 1. Supervisor Agent
The primary entry point (an `Agent`) that validates user requirements (e.g., CSV path validation via `csv_validator_tool`) and routes the request to the appropriate specialized sub-agent.

### 2. Specialized Sub-Agents (Senior ML Automation Architects)
Sub-agents (Classification, Regression, Clustering, Anomaly, Time Series) are implemented as highly specialized `LlmAgent` instances:
-   **Data Intelligence Phase:** Analyzes dataset metadata using `csv_analytics_tool`.
-   **Architectural Phase:** Designs the ML pipeline and generates a unique `SESSION_ID`.
-   **Execution Phase:** Implements the pipeline using PyCaret, saving all code, data snapshots, models, and visualizations.
-   **Verification & Deployment Phase:** Handover to `deploy_agent` to create a production package in `runs/{session_id}/deploy/` (running on **Port 5000**):
    -   `deploy.py`: FastAPI REST API wrapper with Pydantic data models.
    -   `test.py`: Automated integration test script for the API.
    -   `requirements.txt`: Environment dependencies for deployment.
    -   `dockerfile`: Containerization script for cloud deployment (python:3.11-slim).
    -   `local-instructions.md`: Step-by-step guide for local Docker deployment.
    -   `aws-instructions.md`: Guide for deploying to AWS (ECR/ECS).
    -   `gcp-instructions.md`: Guide for deploying to GCP (Cloud Run).
    -   `azure-instructions.md`: Guide for deploying to Azure (ACR/ACI).
-   **Organization Phase:** Persists all artifacts into a structured directory hierarchy.

## 📁 Project Structure

```text
PyCaretAgent/
├── pycaretagent/
│   ├── agent.py               # Root Orchestrator (Router)
│   ├── __init__.py
│   └── utils/
│       ├── config.py          # Centralized configuration (Planners, Models)
│       ├── callbacks.py       # Centralized execution flow & state logic
│       ├── agents/            # Specialized Sub-Agent Definitions
│       │   ├── anomaly_agent.py
│       │   ├── classification_agent.py
│       │   ├── clustering_agent.py
│       │   ├── deploy_agent.py
│       │   ├── regression_agent.py
│       │   └── ts_agent.py
│       ├── instructions/      # Role-based System Prompts (Optimized)
│       │   ├── anomaly_prompt.py
│       │   ├── classification_prompt.py
│       │   ├── clustering_prompt.py
│       │   ├── common_prompt.py
│       │   ├── deploy_prompt.py
│       │   ├── regression_prompt.py
│       │   ├── route_prompt.py
│       │   └── ts_prompt.py
│       └── tools/             # Reusable Agent Tools
│           ├── file_validator_tool.py
│           ├── file_ops_tool.py       # Safe Write/Copy/Find operations
│           ├── csv_analytics_tool.py
│           └── session_id_generator_tool.py
├── runs/                      # Isolated Session Storage ({session_id}/)
├── sample_dataset/            # Organized test datasets with instructions
├── conductor/                 # Project management & track specifications
├── pyproject.toml             # Dependency management (uv/pip)
└── README.md                  # Project documentation
```

## 🛠️ Getting Started

### Prerequisites
-   Python 3.11 or higher.

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

## 📊 Sample Runs

For reference, the following session IDs in the `runs/` directory correspond to specific ML tasks:

| Task Type | Session ID | Key Artifacts |
| :--- | :--- | :--- |
| **Regression** | `S3Y66V` | `final_regression_model.pkl`, `residuals.png`, `feature_importance.png` |
| **Classification** | `WHGV1L` | `final_pipeline.pkl`, `feature_importance.png`, `results.csv` |
| **Time Series** | `F34R8N` | `final_ts_model.pkl`, `results.csv` |
| **Clustering** | `IFHGX6` | `amazon_clustering_model.pkl`, `logs.txt` |
| **Anomaly Detection** | `DC04XC` | `iforest_mango_model.pkl`, `price_dist.png` |

Each run includes a complete `deploy/` package with FastAPI wrappers and multi-cloud deployment guides.

## 📄 License
This project is licensed under the MIT License.
