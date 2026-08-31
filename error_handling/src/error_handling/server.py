from fastmcp import FastMCP, Context
import asyncio

mcp = FastMCP(name="error handling server")


@mcp.tool
def divide(a: float, b: float) -> float:
    """divide two numbers"""
    return a / b


if __name__ == "__main__":
    mcp.run()
