# Product Guidelines: PyCaretAgent

## Engineering Standards
- **Hierarchical Structure**: Maintain the distinction between the Root Router and the Specialized Sequential Sub-Agents.
- **Explicit Imports**: Always use `google.adk` for ADK-related code.
- **Sequential Flows**: Sub-agents MUST follow the `Planner -> Executor` sequence.
- **Alphanumeric IDs**: Session IDs must be exactly 6 characters and include both letters and numbers.

## Data & Artifacts
- **Isolated Storage**: ALL session-specific generated files (CSV, plots, models) MUST be saved inside `runs/{session_id}/`.
- **DataFrame Preference**: Planners must plan to read CSVs using `pd.read_csv()` and pass the DataFrame to `setup()`.

## Reliability & Tracking
- **Error Resilience**: Executors use `error_retry_attempts=10` to automatically rerun and fix code on failure. 
- **Task Finality**: Executors must provide a final summary and conclude the task upon successful completion to exit the control loop.
- **State Persistence**: Utilize `callback_context.state` to pass data between sub-agents in a sequential pipeline.
