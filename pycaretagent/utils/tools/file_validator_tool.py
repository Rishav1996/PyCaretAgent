"""
This module provides tool-based validation for dataset files.
It ensures that the provided paths point to valid CSV files before further processing.
"""

import os
from google.adk.tools.function_tool import FunctionTool


def check_csv_presence(file_path: str) -> dict:
    """
    Checks if the provided file path points to a CSV file.
    
    Use this tool to verify if a file exists and has a .csv extension.
    
    Args:
        file_path: The path to the file to check.
        
    Returns:
        A dictionary with 'status' ('success' or 'error'), 'exists' (bool), and diagnostic messages.
    """
    # Check if the file physically exists on the disk
    if not os.path.exists(file_path):
        return {
            "status": "error",
            "exists": False,
            "message": f"File '{file_path}' does not exist."
        }
    
    # Verify the file extension is .csv
    is_csv = file_path.lower().endswith('.csv')
    if is_csv:
        return {
            "status": "success",
            "exists": True,
            "is_csv": True,
            "message": f"File '{file_path}' is a valid CSV file."
        }
    else:
        # File exists but is not a CSV
        return {
            "status": "error",
            "exists": True,
            "is_csv": False,
            "message": f"File '{file_path}' is not a CSV file."
        }

def check_file_exists(file_path: str) -> dict:
    """
    Checks if a file exists at the specified path.
    """
    exists = os.path.exists(file_path)
    return {
        "exists": exists,
        "message": f"File '{file_path}' exists." if exists else f"File '{file_path}' does not exist."
    }

# Export the functions as ADK tools
csv_validator_tool = FunctionTool(func=check_csv_presence)
file_presence_tool = FunctionTool(func=check_file_exists)
