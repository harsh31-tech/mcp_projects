from fastmcp import FastMCP,Context
import asyncio

mcp = FastMCP(name="error handling server")

@mcp.tool
def divide(a: float, b: float) -> float:
    """Add two numbers"""
    return a / b