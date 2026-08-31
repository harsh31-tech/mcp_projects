from fastmcp import FastMCP, Context
from pydantic import BaseModel
import asyncio

mcp = FastMCP(name="error handling server")


class User(BaseModel):
    name: str
    age: int
    email: str


# @mcp.tool
# def divide(a: float, b: float) -> float:
#     """divide two numbers"""
#     if b == 0:
#         raise ValueError("cannot divide by zero")

#     return a / b


@mcp.tool
def create_user(user: User) -> str:
    """create a user"""
    return f"user {user.email} of age {user.age} is created successfully"


if __name__ == "__main__":
    mcp.run()
