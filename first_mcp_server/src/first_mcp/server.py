from fastmcp import FastMCP

mcp = FastMCP(name="first_server")


# learning tools
@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b


@mcp.tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers and return the result."""
    return a * b


@mcp.tool
def greet(name: str) -> str:
    """greet by name"""
    return f"hello {name} what can i do for you today"


# @mcp.tool
# def get_server_status ()->str:
#     """get the current status of my mcp server"""
#     return "server is running normally"

# learning resources


@mcp.resource("server://status")
def server_status() -> str:
    """current status of mcp server"""
    return "server is running normally"


if __name__ == "__main__":
    mcp.run()
