import asyncio

from fastmcp import Client


async def main():
    client = Client("src/error_handling/server.py")

    # async with client:
    #     try:
    #         divide = await client.call_tool("divide", {"a": 10, "b": 0})
    #         print(divide)
    #     except Exception as e:
    #         print("tool failed :", e)

    # async with client:
    #     username = await client.call_tool(
    #         "create_user",
    #         {
    #             "user": {
    #                 "name": "harsh",
    #                 "email": "harsh@gmail.com",
    #                 "database": "mongodb",
    #             }
    #         },
    #     )
    #     print(username)

    # async with client:
    #     slow = await client.call_tool("slow_task")
    #     fast = await client.call_tool("fast_task")
    #     print(slow)
    #     print(fast)
    # result = await asyncio.gather(slow,fast)
    # print(result)
    async with client:
        server = await client.read_resource("server://status")
        print(server)


if __name__ == "__main__":
    asyncio.run(main())
