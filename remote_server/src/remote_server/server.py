from fastmcp import FastMCP

mcp = FastMCP("Http-demo")


@mcp.tool
async def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=3000)
