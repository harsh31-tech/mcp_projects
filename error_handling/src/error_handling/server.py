from fastmcp import FastMCP, Context
import asyncio

mcp = FastMCP(name="error handling server")


@mcp.tool
def divide(a: float, b: float) -> float:
    """divide two numbers"""
    if b==0:
        raise ValueError("cannot divide by zero")
    
    return a / b


if __name__ == "__main__":
    mcp.run()
