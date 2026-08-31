import asyncio

from fastmcp import Client


async def main():
    client = Client("src/error_handling/server.py")

    async with client:
        divide = await client.call_tool("divide")
        print(divide)


if __name__ == "__main__":
    asyncio.run(main())
