from fastmcp import FastMCP
import os

mcp = FastMCP("AI notes app")

NOTES_FILE = os.path.join(os.path.dirname(__file__),'notes.txt')

def ensure_file_exist():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'w') as f:
            f.write('')


@mcp.tool()
def add_to_note(message: str) -> str:
    """
    Updates the given message to the Note file
    Args:
        message(str): Note content to be add in the note file
    Returns:
        Returns the status of the note addition
    """
    ensure_file_exist()
    with open(NOTES_FILE, 'a') as f:
        f.write(message+ '\n')
    return 'Notes saved!'

if __name__ == "__main__":
    mcp.run()