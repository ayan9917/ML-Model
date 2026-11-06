import asyncio
from mcp_client import *

async def main():
    client  = await connect()
    tools = await discover_tool(client)
    print("----------------------------")
    print("Tools available on server..")
    for tool in tools:
        print(tool.name)

    result = await execute_tool(client, "generate_dice")
    print("Result = ", result.content[0].text)    
    await disconnect(client)

asyncio.run(main())    