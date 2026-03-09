# PyCaretAgent Workflow

The following defines the end-to-end operational lifecycle of the PyCaretAgent system.

## 1. Requirement Validation (Root Agent)
- **Tool**: `check_csv_presence`
- **Action**: Validates local file paths.
- **Outcome**: Confirms CSV existence and task type (Classification, Regression, etc.).

## 2. Planning (Specialized Planner)
- **Role**: Lead ML Architect.
- **Logic**:
    - Defines model selection strategy.
    - Specifies required PyCaret parameters (target, fold, session_id).
    - Generates a unique 6-character alphanumeric **Session ID**.
- **Isolation**: Creates a `runs/{session_id}/` directory for isolation.

## 3. Execution (Specialized Executor)
- **Role**: ML Automation Engineer.
- **Logic**:
    - Generates and executes Python code using `UnsafeLocalCodeExecutor`.
    - **Persistence**: Models and plots saved to the session directory.
- **Finality**: Provides a summary and concludes the task.
