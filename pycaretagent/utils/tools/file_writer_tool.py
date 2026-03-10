import os

def file_writer_tool(file_path: str, content: str) -> str:
    """
    Writes the provided content to a specified file path.
    Automatically creates parent directories if they don't exist.
    
    Args:
        file_path: The absolute or relative path to the file.
        content: The string content to write to the file.
        
    Returns:
        A success message or an error message.
    """
    try:
        # Create directories if they don't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return f"Successfully wrote to {file_path}"
    except Exception as e:
        return f"Error writing to file {file_path}: {str(e)}"
