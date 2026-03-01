# Workflow: PyCaretAgent

The `PyCaretAgent` workflow is designed to handle an end-to-end machine learning lifecycle, from data analysis to model deployment, guided by a hierarchical agent system.

## Key Phases

### 1. Root Agent Orchestration
-   Setup the **Root Agent** using the **Google Generative AI SDK**.
-   Implement mandatory validation logic (CSV, Target, Task Type).
-   Register all specialized sub-agents.

### 2. Specialized Sub-Agent Implementation
-   **Classification/Regression/Clustering/Anomaly/TS Agents:** Setup specific sub-agent logic and tools for automated machine learning.
-   Implement tool-based communication and data sharing between the root agent and sub-agents.

### 3. Data Validation & Preprocessing
-   Root Agent validates datasets using the `check_csv_presence` tool.
-   Preprocessing steps are planned and executed based on identified task requirements.

### 4. Machine Learning Pipeline
-   Sub-agents execute the PyCaret functional API (e.g., `setup`, `compare_models`, `tune_model`).
-   Experiment results are logged and tracked via MLflow.

### 5. Cloud Platform Deployment
-   The Root Agent coordinates the final model deployment.
-   Integration with cloud platforms (AWS, Azure, GCP) to serve endpoints.

## Iterative Development

The implementation will follow a step-by-step approach, starting with the Root Agent routing logic and validation tools, and proceeding through each specialized sub-agent and its unique PyCaret integration requirements.
