# Workflow: PyCaretAgent Agentic Lifecycle

The PyCaretAgent operates through a hierarchical and sequential pipeline:

## 1. Requirement Validation (Root Agent)
- User provides a prompt (e.g., "Classify heart.csv with target 'target'").
- Root Agent validates existence of the CSV using `file_validator_tool`.
- Root Agent identifies the task type and delegates to the appropriate specialized sub-agent.

## 2. Planning (Sub-Agent: Planner)
- Uses `BuiltInPlanner` for native reasoning.
- Analyzes dataset schema and task goals.
- Generates a `SESSION_ID`.
- Produces a concise ML plan (under 150 words) using task-specific PyCaret functions.

## 3. Execution (Sub-Agent: Executor)
- Uses `BuiltInPlanner` to formulate an implementation strategy.
- Creates a `temp/{session_id}/` directory for isolation.
- Generates and runs Python code within a `try-except` block.
- **Self-Correction**: Up to 10 retry attempts if code fails.
- **Logging**:
    - Metrics logged via `mlflow.log_metric()`.
    - Custom params logged via `mlflow.log_param()`.
    - Tracebacks saved to `temp/{session_id}/error.txt` and logged as artifacts.
- **Persistence**: Models and plots saved to the session directory and MLflow.

## 4. Final Verification
- Executor signals `task_completed = True` upon success.
- System exits the loop and provides the final summary to the user.
