# PyCaretAgent Workflow

The following defines the end-to-end operational lifecycle of the PyCaretAgent system.

## 1. Requirement Validation (Supervisor Agent)
- **Tool**: `check_csv_presence`
- **Action**: Validates local file paths and identifies task type.

## 2. Data Intelligence & Execution (Specialized Architect)
- **Role**: Senior ML Automation Architect.
- **Tools**: `csv_analytics_tool`, `session_id_generator_tool`.
- **Logic**:
    - Analyzes dataset schema and distributions.
    - Generates a unique 6-character alphanumeric **Session ID**.
    - Implements the pipeline using PyCaret (Setup, Compare, Finalize).
    - **Persistence**: Models, plots, and metrics saved to `runs/{session_id}/`.
- **Handoff**: Calls `transfer_to_agent` to trigger the `deploy_agent`.

## 3. Verification & Deployment (Deployment Architect)
- **Role**: Deployment & Integrity Architect.
- **Tools**: `find_file_tool`, `file_copy_tool`, `file_writer_tool`, `csv_analytics_tool`.
- **Engine**: Tool-based execution (No Python interpreter).
- **Logic**:
    - Locates training artifacts (`.pkl`, `data_snapshot.csv`).
    - Creates a production-ready package under `runs/{session_id}/deploy/`.
    - **Artifacts**: `deploy.py` (FastAPI API on port 5000), `test.py`, `requirements.txt`, `dockerfile` (python:3.11-slim + libgomp1), and multiple guides (`local-instructions.md`, `aws-instructions.md`, `gcp-instructions.md`, `azure-instructions.md`).
- **Finality**: Provides a summary and concludes the run.
