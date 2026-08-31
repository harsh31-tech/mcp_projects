import asyncio

from fastmcp import Client


async def main():
    client = Client("src/first_mcp/server.py")

    async with client:
        result = await client.call_tool(
            "generate_code", {"project_name": "express js backend"}
        )
        print(result)

    async with client:
        progress = await client.call_tool(
            "generation_progress", {"project_name": "express js backend"}
        )
        print(progress)


if __name__ == "__main__":
    asyncio.run(main())
