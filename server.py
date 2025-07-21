from fastmcp import FastMCP
import asyncio
import os

mcp = FastMCP("QuickCalc")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract second number from first number."""
    return a - b

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 9000))
    asyncio.run(mcp.run_async(transport="streamable-http", host="0.0.0.0", port=port))
