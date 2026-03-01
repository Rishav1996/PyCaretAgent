"""
This module provides tool-based validation for dataset files.
It ensures that the provided paths point to valid CSV files before further processing.
"""

import os


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
