"""
Common instruction components and shared data for all PyCaretAgent prompts.
"""

PYCARET_FUNCTIONS = [
    {
        "category": "initialization",
        "function": "setup",
        "description": "Mandatory. Prepares the environment, handles data preprocessing, and sets the target variable.",
        "optional": False,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"]
    },
    {
        "category": "initialization",
        "function": "eda",
        "description": "Generates an automated Exploratory Data Analysis report to visualize distributions and correlations.",
        "optional": False,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"]
    },
    {
        "category": "model selection",
        "function": "models",
        "description": "Displays a table of all available algorithms in the library along with their shorthand IDs.",
        "optional": True,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"]
    },
    {
        "category": "model selection",
        "function": "compare_models",
        "description": "Trains all available models using cross-validation and ranks them based on performance.",
        "optional": False,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting"]
    },
    {
        "category": "model selection",
        "function": "create_model",
        "description": "Trains and evaluates a specific model (using its ID) and returns a score grid.",
        "optional": True,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"]
    },
    {
        "category": "optimization",
        "function": "tune_model",
        "description": "Automatically tunes hyperparameters to find the best performing version of a model.",
        "optional": True,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting"]
    },
    {
        "category": "optimization",
        "function": "ensemble_model",
        "description": "Enhances a model's performance using meta-learning techniques like Bagging or Boosting.",
        "optional": True,
        "supported_tasks": ["classification", "regression"]
    },
    {
        "category": "optimization",
        "function": "blend_models",
        "description": "Combines multiple models by averaging their predictions (Voting) to improve accuracy.",
        "optional": True,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting"]
    },
    {
        "category": "optimization",
        "function": "stack_models",
        "description": "Layers models so a meta-model learns how to best combine base model predictions.",
        "optional": True,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting"]
    },
    {
        "category": "analysis",
        "function": "plot_model",
        "description": "Generates static visualizations like AUC-ROC, Confusion Matrix, or Feature Importance.",
        "optional": True,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"]
    },
    {
        "category": "analysis",
        "function": "evaluate_model",
        "description": "Provides an interactive UI to view and toggle between all available performance plots.",
        "optional": False,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting"]
    },
    {
        "category": "analysis",
        "function": "dashboard",
        "description": "Launches an interactive ExplainerDashboard for deep diagnostic analysis and SHAP values.",
        "optional": True,
        "supported_tasks": ["classification", "regression"]
    },
    {
        "category": "production",
        "function": "predict_model",
        "description": "Uses a trained model to generate predictions on new or unseen data.",
        "optional": False,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"]
    },
    {
        "category": "production",
        "function": "finalize_model",
        "description": "Retrains the model on the entire dataset (including hold-out) for production.",
        "optional": False,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting"]
    },
    {
        "category": "production",
        "function": "save_model",
        "description": "Exports the transformation pipeline and final model into a .pkl file.",
        "optional": False,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"]
    },
    {
        "category": "production",
        "function": "deploy_model",
        "description": "Transmits the saved model pipeline to a cloud provider (AWS, GCP, or Azure).",
        "optional": False,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"]
    }
]
