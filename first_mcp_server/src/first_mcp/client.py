import asyncio

from fastmcp import Client

async def main():
    client = Client("src/first_mcp/server.py")
    
    async with client:
        result = await client.call_tool(
            "generate_code",
            {"project_name": "express js backend"}
        )
        print(result)
    
if __name__ == "__main__":
    asyncio.run(main())
    