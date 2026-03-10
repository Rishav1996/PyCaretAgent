import pandas as pd
import io
from typing import Dict, Any

def csv_analytics_tool(file_path: str) -> str:
    """
    Analyzes a CSV file and returns technical metadata including info() and describe() output.
    
    Args:
        file_path: The absolute or relative path to the CSV file.
        
    Returns:
        A string containing the technical summary of the dataset.
    """
    try:
        df = pd.read_csv(file_path)
        
        # Capture df.info() output
        buffer = io.StringIO()
        df.info(buf=buffer)
        info_str = buffer.getvalue()
        
        # Get df.describe() output
        describe_str = df.describe(include='all').to_string()
        
        return (
            f"### DATASET INFO ###\n{info_str}\n\n"
            f"### DATASET DESCRIPTION ###\n{describe_str}"
        )
    except Exception as e:
        return f"Error analyzing CSV: {str(e)}"
