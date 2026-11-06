from fastmcp import FastMCP
from datetime import datetime
import random
import secrets
import string

mcp = FastMCP("Time Sever")

@mcp.tool() 

def curent_time():
    """  Return curent time from server"""
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

@mcp.tool() 

def generate_dice() :
    """ Roll a dice"""
    return random.randint(1,6)


@mcp.tool()

def generate_password() :
    """ Generate a sceure password"""
    aplhabet = (string.ascii_letters + string.digits + string.punctuation)
    return "".join(
        secrets.choice(aplhabet)
        for _ in range(12)
    )

if __name__ == "__main__":
    print("MCP server started..")
    mcp.run()
