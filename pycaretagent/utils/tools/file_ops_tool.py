"""
File operation tools for PyCaretAgent.
Provides safe mechanisms for writing and copying files without direct code execution.
"""

import os
import shutil
from google.adk.tools.function_tool import FunctionTool

def write_file(file_path: str, content: str) -> str:
    """
    Writes the provided content to a specified file path.
    Automatically creates parent directories if they don't exist.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Successfully wrote to {file_path}"
    except Exception as e:
        return f"Error writing to file {file_path}: {str(e)}"

def copy_file(source_path: str, destination_path: str) -> str:
    """
    Copies a file from source_path to destination_path.
    Automatically creates parent directories for the destination if they don't exist.
    """
    try:
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        shutil.copy2(source_path, destination_path)
        return f"Successfully copied {source_path} to {destination_path}"
    except Exception as e:
        return f"Error copying file: {str(e)}"

def find_file(directory: str, filename_pattern: str) -> dict:
    """
    Searches for a file matching the pattern within the specified directory and its subdirectories.
    Returns the full path if found.
    """
    import fnmatch
    found_files = []
    try:
        for root, dirs, files in os.walk(directory):
            for name in files:
                if fnmatch.fnmatch(name, filename_pattern):
                    found_files.append(os.path.join(root, name))
        
        return {
            "directory": directory,
            "pattern": filename_pattern,
            "matches": found_files,
            "count": len(found_files)
        }
    except Exception as e:
        return {"error": str(e)}

# Export as ADK tools
file_writer_tool = FunctionTool(func=write_file)
file_copy_tool = FunctionTool(func=copy_file)
find_file_tool = FunctionTool(func=find_file)
