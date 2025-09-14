# UART‑pyAutoPort‑MCP Server

This is an MCP (Model Context Protocol) server for UART communication using the `pyautoport` library.

## Features
- Set UART port and baudrate via MCP tool
- Write commands to UART and read responses with timeout
- Easily integrate with automation workflows

## Requirements
- Python 3.8+
- `pyautoport` package
- `mcp[cli]` package

## Installation
Install dependencies if necessary:
```sh
pip install pyautoport mcp[cli]
```

## Usage

### Connect in Zed

1. **Download the script:**  
  `uart-pyautoport-mcp.py`

2. **Install `uv`:**  
  [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/)

3. **Add MCP server in VS Code or Zed:**  
  Use the following template in your configuration:

  ```json
  {
    // The name of your MCP server
    "uart-mcp-server": {
     "command": {
      // The path to the executable
      "path": "uv",
      // The arguments to pass to the executable
      "args": ["run", "path/to/uart-pyautoport-mcp"],
      // The environment variables to set for the executable
      "env": {}
     }
    }
  }
  ```

> **Reminder:** Replace `"path/to/uart-pyautoport-mcp"` in the configuration above with the actual path to your `uart-pyautoport-mcp.py` script.

### Direct MCP Server

Run the server:
```sh
python uart-pyautoport-mcp.py
```

## License
MIT
