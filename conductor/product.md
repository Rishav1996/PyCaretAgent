# Product Definition: PyCaretAgent

`PyCaretAgent` is a powerful agentic extension for the **PyCaret** library, designed to automate the entire machine learning lifecycle through natural language interaction and intelligent task delegation.

## Core Vision

The product enables users to interact with a **Root Agent** (powered by Google ADK) that intelligently orchestrates specialized **Sub-Agents** to perform complex data science tasks. These agents act as expert assistants that leverage PyCaret's automated ML capabilities to deliver high-quality models and insights.

## Key Features

1.  **Hierarchical Agent Architecture:**
    -   **Root Agent:** High-level planning, user interaction, requirement validation (CSV, Target), and sub-agent orchestration.
    -   **Classification Agent:** Expert in categorical prediction tasks.
    -   **Regression Agent:** Expert in numerical value prediction tasks.
    -   **Clustering Agent:** Expert in unsupervised pattern discovery.
    -   **Anomaly Agent:** Expert in outlier identification.
    -   **Time Series Agent:** Expert in temporal data forecasting.
2.  **End-to-End ML Pipeline:** Complete flow from initial data analysis and preprocessing to final cloud deployment.
3.  **Requirement Validation:** Automated validation of user-provided datasets and target variables using specialized tools.
4.  **Cloud Native Deployment:** Integration with major cloud platforms (AWS, Azure, GCP) to deploy models directly from the agent interface.
5.  **PyCaret Integration:** Seamlessly extends the existing PyCaret ecosystem with reasoning and tool-use capabilities.

## Workflow

-   **Phase 1: Validation & Analysis:** Root Agent uses tools (e.g., `check_csv_presence`) to validate inputs and perform initial data analysis.
-   **Phase 2: Modeling:** Root Agent delegates specific tasks to specialized sub-agents based on the identified task type (Classification, Regression, etc.) for model training and selection.
-   **Phase 3: Deployment:** Once a model is finalized, the agent handles the deployment process to the chosen cloud platform.
