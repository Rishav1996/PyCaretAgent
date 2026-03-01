# PyCaretAgent

`PyCaretAgent` is an autonomous AI agent framework that extends **PyCaret** with advanced reasoning and tool-use capabilities using the **Google Generative AI SDK (google-adk)**.

## Overview

`PyCaretAgent` implements a hierarchical and sequential agent system. It features a **Root Agent** that orchestrates specialized **Sub-Agents** (Classification, Regression, etc.), which are themselves structured as sequential pipelines to ensure high-precision ML planning, execution, and reporting.

## Key Features

-   **Agentic PyCaret Extension:** Natural language interface to trigger automated ML pipelines.
-   **Sequential Pipeline Orchestration:** Sub-agents (like Classification and Regression) use a structured `Planner -> Executor -> Reporter` workflow.
-   **Experiment Tracking:** Integrated **MLflow** for monitoring experiments, parameters, and models at `http://127.0.0.1:5000`.
-   **Session ID Persistence:** Automated session ID generation and state sharing across the pipeline for auditability.
-   **Professional Reporting:** Automated generation of both Markdown summaries and styled HTML reports saved locally.
-   **Cloud Deployment:** Ready for model deployment directly to cloud platforms (AWS, Azure, GCP).

## Architecture

### Root Agent
The primary entry point for user interaction and high-level task delegation.

### Specialized Sub-Agents (Sequential)
-   **Classification & Regression Agents:**
    -   **Planner:** ML Architect persona that designs the PyCaret pipeline and generates a Session ID.
    -   **Executor:** ML Automation persona that executes code via `BuiltInCodeExecutor` and logs to MLflow.
    -   **Reporter:** Data Storyteller persona that synthesizes results into Markdown and HTML formats.

## Project Structure

```text
pycaretagent/
├── agent.py               # Orchestrating Root Agent
└── utils/
    ├── agents/            # Sub-Agent definitions (Classification, Regression, etc.)
    ├── instructions/      # Optimized prompt templates (Planner, Executor, Reporter)
    │   ├── common_prompt.py  # Shared PyCaret function definitions
    ├── tools/             # Reusable tools (HTML Reporter, etc.)
    └── config.py          # Global configuration & MLflow URI
results/                   # Local storage for session artifacts and HTML reports
```

## Getting Started

### Prerequisites

-   Python 3.12 or higher.
-   `uv` (recommended) or `pip`.
-   A local MLflow server running at `http://127.0.0.1:5000`.

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/PyCaretAgent.git
cd PyCaretAgent

# Install dependencies
uv pip install .
```

### Running MLflow
```bash
mlflow ui --port 5000
```

## Usage

(Implementation in progress. Use the root agent to initiate a classification or regression task by providing a dataset path and a target variable.)

## License

[MIT License](LICENSE)
