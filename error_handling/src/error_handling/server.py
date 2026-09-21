from fastmcp import FastMCP, Context
from fastmcp.server.middleware import Middleware

from pydantic import BaseModel, EmailStr
from enum import Enum
from contextlib import asynccontextmanager
import asyncio
import time

mcp = FastMCP(name="error-handling-server")


# async def middleware(context, call_next): #basic structure of creating middleware
#     print("before")

#     result = await call_next(context)

#     print("after")

#     return result


# class TimingMiddleware(Middleware): # this middle ware will apply in every tool
#     async def on_call_tool(self, context, call_next):
#         start = time.time()

#         result = await call_next(context)

#         elapsed = time.time() - start

#         await context.fastmcp_context.info(f"Tool took {elapsed:.2f} seconds")

#         return result


# mcp.add_middleware(TimingMiddleware())


class TimingMiddleware(
    Middleware
):  # this middle ware will apply only on selected tools only
    def __init__(self, target_tools):
        self.target_tools = target_tools

    async def on_call_tool(self, context, call_next):

        if context.message.name not in self.target_tools:
            return await call_next(context)

        start = time.time()

        result = await call_next(context)

        elapsed = time.time() - start

        await context.fastmcp_context.info(f"Tool took {elapsed:.2f} seconds")

        return result


mcp.add_middleware(TimingMiddleware(target_tools={"add"}))


@mcp.tool
async def add(a: int, b: int):
    await asyncio.sleep(5)
    return a + b


# @asynccontextmanager
# async def lifespan(server):
#     print("Server starting...")

#     yield

#     print("server is shutting down...")


# @asynccontextmanager
# async def lifespan(
#     server,
# ):  # lifespan context is used to define and satrt thing before running the server which will not create lag or missing data

#     db = await connect_to_db()

#     http_client = create_http_client()

#     cache = {}

#     yield {"db": db, "http": http_client, "cache": cache}

#     await db.close()
#     await http_client.close()


# @mcp.tool
# async def get_user(username: str, ctx: Context):
#     state = ctx.lifespan_context

#     db = state["db"]

#     print(db)


# mcp = FastMCP(name="error handling server", lifespan=lifespan)
# class Database(str, Enum):
#     POSTGRES = "postgres"
#     MYSQL = "mysql"
#     MONGODB = "mongodb"


# class User(BaseModel):
#     name: str
#     database: Database
#     email: EmailStr


# @mcp.tool
# def divide(a: float, b: float) -> float:
#     """divide two numbers"""
#     if b == 0:
#         raise ValueError("cannot divide by zero")

#     return a / b


# @mcp.tool
# def create_user(user: User) -> str:
#     """create a user"""
#     return f"user {user.email} of  {user.database} is created successfully"


# @mcp.tool
# async def slow_task() -> str:
#     """a slow asyncrohnous task"""
#     await asyncio.sleep(5)
#     return "slow task completed"


# @mcp.tool
# async def fast_task() -> str:
#     """a slow asyncrohnous task"""
#     await asyncio.sleep(5)
#     return "fast task completed"


# # @mcp.resource("server://status")
# # def server_status() -> str:
# #     """status of the server"""
# #     return """
# #     environment = development
# #     version = 1.0
# #     status = healthy
# #     """


# @mcp.resource("server://status")
# def server_status() -> dict:
#     """status of the server"""
#     return {"environment": "development", "version": "1.0", "status": "healthy"}


# @mcp.resource("user://{username}")
# def user_profile(username: str) -> str:
#     return f"server status asked by {username}"


# @mcp.prompt
# def analyze():
#     return """analyze the code which is given by the user"""


if __name__ == "__main__":
    mcp.run()
