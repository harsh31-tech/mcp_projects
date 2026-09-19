from fastmcp import FastMCP, Context
from pydantic import BaseModel, EmailStr
from enum import Enum
import asyncio

mcp = FastMCP(name="error handling server")


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


@mcp.tool
async def slow_task() -> str:
    """a slow asyncrohnous task"""
    await asyncio.sleep(5)
    return "slow task completed"


@mcp.tool
async def fast_task() -> str:
    """a slow asyncrohnous task"""
    await asyncio.sleep(5)
    return "fast task completed"


# @mcp.resource("server://status")
# def server_status() -> str:
#     """status of the server"""
#     return """
#     environment = development
#     version = 1.0
#     status = healthy
#     """


@mcp.resource("server://status")
def server_status() -> dict:
    """status of the server"""
    return {"environment": "development", "version": "1.0", "status": "healthy"}


@mcp.resource("user://{username}")
def user_profile(username: str) -> str:
    return f"server status asked by {username}"


@mcp.prompt
def analyze():
    return """analyze the code which is given by the user"""

if __name__ == "__main__":
    mcp.run()
