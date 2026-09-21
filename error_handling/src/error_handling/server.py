from fastmcp import FastMCP, Context
from fastmcp.server.middleware import Middleware
from pydantic import BaseModel, EmailStr
from enum import Enum
from contextlib import asynccontextmanager
import asyncio

mcp = FastMCP(name="error-handling-server")


async def middleware(context, call_next): #basic structure of creating middleware 
    print("before")

    result = await call_next(context)

    print("after")

    return result


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
