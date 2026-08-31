from fastmcp import FastMCP, Context
from fastmcp.prompts import Message
import asyncio


mcp = FastMCP(name="first_server")


# learning tools
@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b


@mcp.tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers and return the result."""
    return a * b


@mcp.tool
def greet(name: str) -> str:
    """greet by name"""
    return f"hello {name} what can i do for you today"


# @mcp.tool
# def get_server_status ()->str:
#     """get the current status of my mcp server"""
#     return "server is running normally"

# learning resources


@mcp.resource("server://status")
def server_status() -> str:
    """current status of mcp server"""
    return "server is running normally"


# dynamic resources


@mcp.resource("user://status/{username}")
def user_info(username: str) -> str:
    """get information about user"""
    return f"user : {username}"


# mcp prompts


@mcp.prompt
def debug_code(code: str) -> str:
    """create a prompt to debug the code"""
    return f""" you are the python developer
                analyze the following python code 
                {code}
 
                resolve the logical , syntax and other mistakes

            """


# myltiple inputs in prompt
@mcp.prompt
def code_review(code: str, language: str, focus: str) -> str:
    """create a prompt to review the code"""
    return f""" you are a senior developer 
                review the following code
                {code}
                it is based on the lanaguage {language} 
                and output is foused on {focus}"""


# using python message object to parse the message
@mcp.prompt
def structured_prompt(code: str) -> list[Message]:
    """create a structured prompt"""
    return [
        Message(
            role="system",
            content="you are a expert python devloper ",
        ),
        Message(role="user", content=f"analyze the code of python {code}"),
    ]


# learning context


@mcp.tool
async def process_data(data: str, ctx: Context) -> str:
    """process data and demonstrate mcp context"""
    await ctx.info(f"processing {data}")

    return f"proccessed {data}"


@mcp.tool
async def generate_code(project_name: str, ctx: Context) -> str:
    """generate the backend project"""

    await ctx.info("validation project structure")

    await ctx.info("Creating project structure")

    await ctx.info("Generating API routes")

    await ctx.info("Generating database layer")

    await ctx.info("Generating authentication")

    return f"the backend project is created {project_name}"


@mcp.tool
async def generation_progress(project_name: str, ctx: Context) -> str:
    """generate project step by step"""
    await ctx.info("Creating project structure")
    await ctx.report_progress(0, 5)

    await asyncio.sleep(2)

    await ctx.info("Generating API routes")
    await ctx.report_progress(1, 5)

    await asyncio.sleep(2)

    await ctx.info("Generating database layer")
    await ctx.report_progress(3, 5)

    await asyncio.sleep(2)

    await ctx.info("Generating authentication")
    await ctx.report_progress(4, 5)

    await asyncio.sleep(2)

    await ctx.info("Project generation complete")
    await ctx.report_progress(5, 5)

    return f"the backend project is generated{project_name}"


if __name__ == "__main__":
    mcp.run()
