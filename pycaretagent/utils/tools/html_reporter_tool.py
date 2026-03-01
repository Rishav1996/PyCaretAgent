"""
Tool for saving HTML reports for PyCaretAgent.
"""

from pathlib import Path
from google.adk.tools import FunctionTool
from google.adk.tools.tool_context import ToolContext
from pycaretagent.utils.config import RESULTS_DIR

def save_html_report(html_content: str, session_id: str, tool_context: ToolContext) -> str:
    """
    Saves the generated HTML report to the results/session_id directory.
    """
    try:
        # Create the session-specific results directory
        session_dir = Path(RESULTS_DIR) / session_id
        session_dir.mkdir(parents=True, exist_ok=True)
        
        file_path = session_dir / "report.html"
        
        # Save the HTML content
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        return f"HTML report successfully saved to {file_path}"
    except Exception as e:
        return f"Failed to save HTML report: {str(e)}"

# Define the HTML report tool
save_html_report_tool = FunctionTool(func=save_html_report)
