import random
import string

def session_id_generator_tool() -> str:
    """
    Generates a random 6-character alphanumeric Session ID.
    
    Returns:
        A string in the format 'SESSION_ID: <6-char-ID>'
    """
    session_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"SESSION_ID: {session_id}"
