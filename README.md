# PyCaretAgent

`PyCaretAgent` is an autonomous AI agent framework that extends **PyCaret** with advanced reasoning and tool-use capabilities using the **Google Generative AI SDK**.

## Overview

`PyCaretAgent` implements a hierarchical agent system featuring a **Root Agent** that orchestrates specialized **Sub-Agents** (Classification, Regression, etc.) to perform complex machine learning workflows.

## Key Features

-   **Agentic PyCaret Extension:** Natural language interface to trigger automated ML pipelines.
-   **Hierarchical Orchestration:** Root Agent delegates tasks to specialized Sub-Agents.
-   **End-to-End Pipeline:** Automated data analysis, preprocessing, training, tuning, and deployment.
-   **Cloud Deployment:** Deploy models directly to cloud platforms (AWS, Azure, GCP).
-   **Experiment Tracking:** Integrated MLflow for monitoring experiments and models.

## Architecture

-   **Root Agent:** The primary entry point for user interaction and task planning.
-   **Classification Agent:** Specialized sub-agent for automated classification tasks.
-   **Regression Agent:** Specialized sub-agent for automated regression tasks.

## Getting Started

### Prerequisites

-   Python 3.12 or higher.
-   `uv` (recommended) or `pip`.

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/PyCaretAgent.git
cd PyCaretAgent

# Install dependencies
uv pip install .
```

## Usage

(Implementation in progress. Follow the step-by-step setup as guided by the documentation.)

## License

[MIT License](LICENSE)
