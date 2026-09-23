from fastmcp import Client
import asyncio


async def main():
    client = Client("http://127.0.0.1:3000/mcp")

    async with client:
        result = await client.call_tool("add", {"a": 10, "b": 20})
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
