# AI Notes App

This project is an AI-powered notes application using MCP (Model Context Protocol).

## Features

- Add notes via AI tools
- Store notes in a text file (`notes.txt`)
- Simple and extensible Python codebase

## Requirements

- Python 3.8+
- MCP (Model Context Protocol) and FastMCP

## Installation

1. Clone this repository.
2. Create a virtual environment:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install fastmcp
   ```

## Usage

1. Start the MCP server:
   ```sh
   python main.py
   ```
2. Use the provided tools to add notes. Notes are saved in `notes.txt`.

## Adding Notes

- Use the `add_to_note` tool to append a message to your notes file.

## MCP Configuration Example

Add the following to your `.vscode/mcp.json` file:

```json
{
  "servers": {
    "ai-notes": {
      "url": "http://127.0.0.1:8000/sse"
    },
    "ai-notes-stdio": {
      "type": "stdio",
      "command": "/Users/saminathan/Workspace/notes-mcp/.venv/bin/python3",
      "args": ["main.py"]
    }
  }
}
```
