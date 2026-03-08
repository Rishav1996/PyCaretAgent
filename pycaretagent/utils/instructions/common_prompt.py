"""
Common instruction components and shared data for all PyCaretAgent prompts.
"""

PYCARET_FUNCTIONS = [
    {
        "category": "initialization",
        "function": "setup",
        "description": "Mandatory. Prepares the environment, handles data preprocessing, and sets the target variable.",
        "optional": False,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"],
        "parameters": {
            "data": "A pandas DataFrame containing the dataset.",
            "target": "Name of the target column (for supervised tasks).",
            "session_id": "Integer to seed the random number generator for reproducibility.",
            "train_size": "Proportion of data to use for training (default 0.7).",
            "preprocess": "Boolean to enable/disable data preprocessing.",
            "categorical_features": "List of strings for features that should be treated as categorical.",
            "numeric_features": "List of strings for features that should be treated as numerical.",
            "ignore_features": "List of strings for columns to be ignored during training.",
            "normalize": "Boolean to scale the features to a specific range.",
            "transformation": "Boolean to apply power transformation to make data more Gaussian-like.",
            "remove_outliers": "Boolean to remove outliers from the training data.",
            "fix_imbalance": "Boolean to handle class imbalance (classification only).",
            "html": "Boolean to prevent printing the setup summary grid in certain IDEs."
        }
    },
    {
        "category": "initialization",
        "function": "eda",
        "description": "Generates an automated Exploratory Data Analysis report to visualize distributions and correlations.",
        "optional": False,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"],
        "parameters": {
            "display_format": "Option to specify the format of the output (e.g., 'svg' for high-quality images)."
        }
    },
    {
        "category": "model selection",
        "function": "models",
        "description": "Displays a table of all available algorithms in the library along with their shorthand IDs.",
        "optional": True,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"],
        "parameters": {
            "type": "Filter models by type (e.g., 'ensemble').",
            "internal": "Boolean to show internal models not typically exposed to the user."
        }
    },
    {
        "category": "model selection",
        "function": "compare_models",
        "description": "Trains all available models using cross-validation and ranks them based on performance.",
        "optional": False,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting"],
        "parameters": {
            "include": "List of model IDs to include in the comparison.",
            "exclude": "List of model IDs to ignore.",
            "fold": "Number of cross-validation folds (default 10).",
            "sort": "The metric used to rank the models (e.g., 'Accuracy', 'AUC', 'RMSE').",
            "n_select": "Number of top models to return as a list (default 1).",
            "errors": "Handle errors during training ('raise' or 'ignore').",
            "probability_threshold": "Threshold for converting probabilities to class labels (classification only)."
        }
    },
    {
        "category": "model selection",
        "function": "create_model",
        "description": "Trains and evaluates a specific model (using its ID) and returns a score grid.",
        "optional": True,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"],
        "parameters": {
            "estimator": "The ID of the model to be created (e.g., 'rf' for Random Forest).",
            "fold": "Number of folds for cross-validation.",
            "round": "Number of decimal places for score grid (default 4).",
            "cross_validation": "Boolean to determine if CV should be performed.",
            "fit_kwargs": "Dictionary of additional parameters to pass to the estimator's fit method."
        }
    },
    {
        "category": "analysis",
        "function": "evaluate_model",
        "description": "Provides an interactive UI to view and toggle between all available performance plots.",
        "optional": False,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting"],
        "parameters": {
            "estimator": "The trained model object.",
            "fold": "Number of folds used for the plots that require CV.",
            "fit_kwargs": "Additional arguments to pass to the model."
        }
    },
    {
        "category": "production",
        "function": "predict_model",
        "description": "Uses a trained model to generate predictions on new or unseen data.",
        "optional": False,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"],
        "parameters": {
            "estimator": "The trained model object.",
            "data": "Pandas DataFrame for new predictions (if None, predicts on the hold-out set).",
            "probability_threshold": "Threshold for classification (default 0.5).",
            "raw_score": "Boolean; if True, returns scores for all classes in classification.",
            "round": "Decimal places for predicted values."
        }
    },
    {
        "category": "production",
        "function": "finalize_model",
        "description": "Retrains the model on the entire dataset (including hold-out) for production.",
        "optional": False,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting"],
        "parameters": {
            "estimator": "The trained model object.",
            "fit_kwargs": "Additional arguments to pass to the underlying estimator.",
            "model_only": "Boolean; if True, only the model is finalized without the preprocessing pipeline."
        }
    },
    {
        "category": "production",
        "function": "save_model",
        "description": "Exports the transformation pipeline and final model into a .pkl file.",
        "optional": False,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"],
        "parameters": {
            "model": "The trained model object or pipeline.",
            "model_name": "String; the filename for the saved .pkl file.",
            "prep_pipe": "Boolean; whether to include the preprocessing pipeline in the file.",
            "verbose": "Boolean; whether to print the success message."
        }
    },
    {
        "category": "deployment",
        "function": "create_api",
        "description": "Creates a REST API for the model using FastAPI.",
        "optional": True,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"],
        "parameters": {
            "estimator": "The trained model object.",
            "api_name": "Name of the API (string)."
        }
    },
    {
        "category": "deployment",
        "function": "create_app",
        "description": "Creates a basic web application for the model using Streamlit.",
        "optional": True,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"],
        "parameters": {
            "estimator": "The trained model object.",
            "app_name": "Name of the app (string)."
        }
    },
    {
        "category": "deployment",
        "function": "create_docker",
        "description": "Creates a Dockerfile and requirements.txt for deploying the model API.",
        "optional": True,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"],
        "parameters": {
            "api_name": "Name of the API created with create_api."
        }
    }
]

# --- SHARED SEARCH INSTRUCTIONS ---
SHARED_SEARCH_INSTRUCTIONS = (
    "\n\n### RESEARCH CAPABILITIES:\n"
    "Access the `google_search_tool` for internet research. "
    "**MANDATORY: During the PLANNING PHASE, use this tool ONLY to research technical facts regarding PyCaret, MLflow, or Pandas.**\n"
    "Research constraints are strictly enforced:\n"
    "- **LIBRARIES ONLY**: Limit queries to official documentation for PyCaret, MLflow, and Pandas.\n"
    "- **NO DATASETS**: Do not research dataset schemas, descriptions, or sources.\n"
    "- **NO SUMMARIES**: Do not ask for summaries or general context; request only specific technical data.\n"
    "**CRITICAL**: The tool will return 'unable to find' for any query involving datasets, summarization, or unrelated libraries."
)
