from fastmcp import FastMCP
mcp = FastMCP(name="first server")

@mcp.tool
def add(a:float , b:float)-> float:
    """Add two numbers"""
    return a+b

if __name__ == "__main__":
    mcp.run()