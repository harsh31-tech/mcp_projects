import asyncio

from fastmcp import Client


async def main():
    client = Client("src/error_handling/server.py")

    async with client:
        try:
            divide = await client.call_tool("divide", {"a": 10, "b": 0})
            print(divide)
        except Exception as e:
            print("tool failed :" , e)
        

if __name__ == "__main__":
    asyncio.run(main())
