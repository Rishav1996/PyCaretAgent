# Tech Stack: PyCaretAgent

## Core Technologies
- **Python 3.12+**: Primary programming language.
- **AutoML Core**: [PyCaret](https://pycaret.org/) for automated machine learning.
- **Agent Orchestration**: [Google Generative AI SDK (google-adk)](https://github.com/google-gemini/google-adk) using the `google.adk` package.
- **Experiment Tracking**: [MLflow](https://mlflow.org/) for logging metrics, parameters, and models.
- **Data Engine**: [Pandas](https://pandas.pydata.org/) for mandatory CSV data handling.

## Infrastructure & Tools
- **Model Layer**: Gemini 2.5 Flash (Default) and Gemini 3 Flash Preview (Performance).
- **Code Execution**: `UnsafeLocalCodeExecutor` for local Python execution.
- **Dependency Management**: `uv` and `pip`.
- **Project Management**: Conductor (this directory).
