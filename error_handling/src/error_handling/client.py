import asyncio

from fastmcp import Client


async def main():
    client = Client("server.py")

    # async with client:
    #     try:
    #         divide = await client.call_tool("divide", {"a": 10, "b": 0})
    #         print(divide)
    #     except Exception as e:
    #         print("tool failed :", e)

    async with client:
        username = await client.call_tool(
            "create_user",
            {"user": {"name": "harsh", "email": "harsh@gmail.com", "age": 18}},
        )
        print(username)


if __name__ == "__main__":
    asyncio.run(main())
