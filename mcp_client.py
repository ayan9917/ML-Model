from fastmcp import Client

async def connect():
    """ Conect to MCP Server"""
    client = Client("server.py")

    await client.__aenter__()
    print("Conected to server")
    return client

async def disconnect(client):
    """ disconect from  server"""
    await client.__aexit__(
        None,
        None,
        None
    )

async def discover_tool(client):
    """ Find all the tools available on server"""    
    tools = await client.list_tools()
    return tools

async def execute_tool(client, tool_name, arguments = None):
    """ Execute the specified tool"""
    if arguments is None:
        arguments = {}
    result= await client.call_tool(tool_name, arguments)    
    return result