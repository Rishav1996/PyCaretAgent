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
        "category": "optimization",
        "function": "tune_model",
        "description": "Automatically tunes hyperparameters to find the best performing version of a model.",
        "optional": True,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting"],
        "parameters": {
            "estimator": "The model object to be tuned.",
            "fold": "Number of folds for cross-validation.",
            "n_iter": "Number of iterations for hyperparameter search (default 10).",
            "optimize": "Metric to optimize (e.g., 'Accuracy', 'F1').",
            "search_library": "Library used for tuning ('scikit-learn', 'optuna', 'tune-sklearn', etc.).",
            "search_algorithm": "Specific algorithm (e.g., 'random', 'grid', 'bayesian').",
            "custom_grid": "Dictionary of specific hyperparameter values to search.",
            "choose_better": "Boolean; if True, returns the original model if tuning doesn't improve it."
        }
    },
    {
        "category": "optimization",
        "function": "ensemble_model",
        "description": "Enhances a model's performance using meta-learning techniques like Bagging or Boosting.",
        "optional": True,
        "supported_tasks": ["classification", "regression"],
        "parameters": {
            "estimator": "The trained model object to ensemble.",
            "method": "Ensembling method: 'Bagging' or 'Boosting'.",
            "fold": "Number of folds for cross-validation.",
            "n_estimators": "Number of base estimators in the ensemble (default 10).",
            "choose_better": "Boolean; returns the original model if ensemble performance is lower."
        }
    },
    {
        "category": "optimization",
        "function": "blend_models",
        "description": "Combines multiple models by averaging their predictions (Voting) to improve accuracy.",
        "optional": True,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting"],
        "parameters": {
            "estimator_list": "List of trained model objects to blend.",
            "fold": "Number of folds for cross-validation.",
            "method": "Voting method: 'hard' or 'soft' (classification only).",
            "weights": "List of weights for each model in the blend.",
            "optimize": "Metric used to determine the best model if choose_better is True."
        }
    },
    {
        "category": "optimization",
        "function": "stack_models",
        "description": "Layers models so a meta-model learns how to best combine base model predictions.",
        "optional": True,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting"],
        "parameters": {
            "estimator_list": "List of base models to be stacked.",
            "meta_model": "The model that learns to combine predictions (default 'lr' for LogReg/LinearReg).",
            "fold": "Number of folds for cross-validation.",
            "method": "How predictions are passed to meta-model ('predict' or 'predict_proba').",
            "restack": "Boolean; if True, base models are trained on both original features and predictions."
        }
    },
    {
        "category": "analysis",
        "function": "plot_model",
        "description": "Generates static visualizations like AUC-ROC, Confusion Matrix, or Feature Importance.",
        "optional": True,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"],
        "parameters": {
            "estimator": "The trained model object.",
            "plot": "Type of plot (e.g., 'auc', 'confusion_matrix', 'feature', 'error').",
            "scale": "Resolution scale for the plot.",
            "save": "Boolean or path; if True, saves the plot as a file.",
            "use_train_data": "Boolean; if True, generates the plot using training data instead of test data."
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
        "category": "analysis",
        "function": "dashboard",
        "description": "Launches an interactive ExplainerDashboard for deep diagnostic analysis and SHAP values.",
        "optional": True,
        "supported_tasks": ["classification", "regression"],
        "parameters": {
            "estimator": "The trained model object.",
            "display_format": "Format of the dashboard ('inline' for notebooks or 'external' for a browser tab)."
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
        "category": "production",
        "function": "deploy_model",
        "description": "Transmits the saved model pipeline to a cloud provider (AWS, GCP, or Azure).",
        "optional": False,
        "supported_tasks": ["classification", "regression", "timeseries_forecasting", "clustering", "anomaly_detection"],
        "parameters": {
            "model": "The trained model object.",
            "model_name": "Name of the model on the cloud platform.",
            "platform": "Cloud service provider ('aws', 'gcp', or 'azure').",
            "authentication": "Dictionary containing cloud credentials (e.g., bucket name, access keys)."
        }
    }
]