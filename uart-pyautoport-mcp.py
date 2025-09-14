# /// script
# dependencies = [
#   "pyautoport",
#   "mcp[cli]",
# ]
# ///
#
import os
from mcp.server.fastmcp import FastMCP
import pyautoport.uart as pauto

# Create MCP server
mcp = FastMCP("UART‑pyAutoPort‑MCP", dependencies=["pyAutoPort"])


@mcp.tool(
    description="Set the baudrate and UART port to communicate on",
)
def set_uart_config(port: str, baudrate: int) -> str:
    os.environ["TESTER_UART_PORT"] = port
    os.environ["TESTER_UART_BAUDRATE"] = str(baudrate)
    return f"UART set to {port}@{baudrate}"

@mcp.tool(
    description="""
Writes text to the UART and reads all available lines until a timeout.

Args:
    cmd: The text to write to the UART.
    timeout: The timeout for UART operations.

Returns:
    A string containing the reply received from the UART.
""",
    )
def write_and_read_uart(cmd: str, timeout: float = None) -> str:
    # Ensure environment config is applied
    if timeout is None:
        timeout = 1
    return pauto.write_and_read_uart(cmd, timeout)

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
