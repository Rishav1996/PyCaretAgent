# Product Guidelines: PyCaretAgent

## Engineering Standards
- **Hierarchical Structure**: Maintain the distinction between the Root Router and the Specialized Sequential Sub-Agents.
- **Explicit Imports**: Always use `google.adk` for Google Generative AI SDK imports.
- **Surgical Updates**: Prefer targeted edits to files rather than full overwrites where possible.

## Data Handling Rules (MANDATORY)
- **Pandas Core**: ALL planning agents MUST plan to read CSV files using `pd.read_csv()`.
- **Explicit Dataframe passing**: The resulting DataFrame must be passed directly to PyCaret's `setup()` function.
- **No Memory Rule**: Avoid reading entire datasets into the agent's internal memory; use localized file paths and DataFrames.

## Reliability & Tracking
- **Traceback Awareness**: Mandatory `try-except` blocks in generated code to capture and log tracebacks to `error.txt`.
- **MLflow Naming**: Experiments must be named using the `[task]_{session_id}` convention.
- **Artifact Isolation**: All generated files MUST reside in `temp/{session_id}/`.
