# Project: PyCaretAgent

## Project Overview

This project, `pycaretagent`, appears to be a Python-based framework for agentic machine learning tasks, primarily focusing on classification and regression. It leverages `crewai` for agent orchestration and `pycaret` for streamlined machine learning workflows. The project is structured with separate modules for classification and regression, each intended to house `crewai` agents, their prompts, and associated tools. Currently, some core implementation files (like `README.md`, `agents.py`, `tools.py` in both `classification` and `regression` directories) appear to be placeholders, suggesting it might be a template or an early-stage project.

## Building and Running

*   **Prerequisites:** Python 3.12 or higher.

*   **Installation:**
    The project's dependencies are listed in `requirements.txt` and `pyproject.toml`. You can install them using `pip` or `uv`.

    ```bash
    # Using pip
    pip install -r requirements.txt
    # or using uv (if installed)
    uv pip install -r requirements.txt
    ```
    Alternatively, using `pyproject.toml` with a modern Python dependency manager:
    ```bash
    # Using uv (recommended)
    uv pip install .
    # Using pip (requires setuptools in some cases)
    pip install .
    ```

*   **Running the project:**
    (TODO: Determine the main entry point or execution flow. The current agent and tool files are empty. This section will need to be updated once the core logic is implemented.)

## Development Conventions

*   **Python Version:** Python 3.12 is the target development environment, as indicated by `.python-version` and `pyproject.toml`.
*   **Dependency Management:** Dependencies are managed via `requirements.txt` for direct dependencies and `pyproject.toml` for project metadata and more comprehensive dependency management.
*   **Agentic Architecture:** The project utilizes `crewai` for building intelligent agents, with clear separation of concerns for agents, prompts, and tools within `classification` and `regression` modules.
*   **Machine Learning Framework:** `pycaret` is integrated for simplified machine learning model development and deployment.
