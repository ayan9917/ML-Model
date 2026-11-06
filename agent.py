# # import asyncio
# # from openai import OpenAI
# # from dotenv import load_dotenv
# # import os

# # load_dotenv()

# # base_url = os.getenv("BASE_URL")
# # api_key = os.getenv("API_KEY")

# # print(base_url)
# # # print(api_key)  # Avoid printing API keys

# # client = OpenAI(
# #     base_url=base_url,
# #     api_key=api_key
# # )

# # print("client created")

# # from mcp_client import *

# # def build_tool_description(tools):
# #     descriptions = ""

# #     for tool in tools:
# #         descriptions = descriptions + f"""
# #     Tools:
# #     {tool.name}
# #     Descriptions:
# #     {tool.description}
# #     ==============================================
# # """
# #     return descriptions
# #  def planner(user_request,tool):
# #     user_request:
# #     {user_request}
# #     {tool_descriptions}
# #     Instrucrions


# # async def main():
# #     client = await connect()

# #     tools = await discover_tool(client)

# #     result = build_tool_description(tools)

# #     print(result)

# #     await disconnect(client)


# # if __name__ == "__main__":
# #     asyncio.run(main())
# from openai import OpenAI
# import asyncio
# from dotenv import load_dotenv
# import os
# load_dotenv()
# baseUrl= os.getenv("BASE_URL");
# print(baseUrl)
# apiKey = os.getenv("API_KEY");
# print(apiKey)
# model = os.getenv("MODEL");
# print(model)
# client = OpenAI(
#     base_url = baseUrl,
#     api_key = apiKey
# )
# print("client creared...")
# from mcp_client import *
# def bulid_tool_description(tools):
#     description=""
#     for tool in tools:
#         description=description+f"""
#     Tool:
#     {tool.name}
#     Description:
#     {tool.description}
#     ==================="""
#     return description
# def planner(user_request,tools):
#     tool_description=bulid_tool_description(tools)
#     prompt=f"""
# You are a ai planner
# available tools:
# {tool_description}
# intructions
# 1.select the best tool 
# 2.reply only with the tools name 
# 3.Do not explain
# User request:
# {user_request}
# """
#     response=client.chat.completions.create(
#         model=os.getenv("Model"),
#         messages=[{
#             "role":"user",
#             "content":prompt
#         }]
#     )
    
    
# async def main():
#     client=await connect()
#     tools=await discover_tool(client)
#     print("--------")
#     result=bulid_tool_description(tools)
#     print(result)
#     await disconnect(client)
# if __name__=="__main__":
#     asyncio.run(main())
import asyncio
from mcp_client import *
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)
print("Client connected to server..")

def build_tool_description(tools):
    descriptions =''
    for tool in tools:
        descriptions += f'''
        Tool:
        {tool.name}

        Description:
        {tool.description}
        ======================================
    '''
    return descriptions

def planner(user_request,tools):
    tools_discription = build_tool_description(tools)
    prompt = f"""
    you are an AI planner that can use the following tools to help the user with their request.
    {tools_discription}
    instructions
    1) Select he best tool
    2)Reply only with the tool name
    3)Do not explain

    User request:
    {user_request}"""

    response = client.chat.completions.create(
        model = os.getenv("MODEL"),
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    tool_name = response.choices[0].message.content
    return tool_name
def generate_response(user_request,result):
    prompt = f"""
The user asked:

{user_request}

The tool returned:

{result}

Respond directly to the user in a natural, conversational way.

Use the tool result as the factual source.
Transform raw tool output into a human-friendly answer.
Do not simply copy raw values when a natural sentence would be better.
Do not add information that is not needed to answer the request.
Do not mention tools, internal processing, planning, or reasoning.
Keep the response concise.
"""
    
    response = client.chat.completions.create(
            model = os.getenv("MODEL"),
            messages = [{
                "role": "user",
                "content": prompt
            }]
        )
    return response.choices[0].message.content
    

async def main():
    client = await connect()
    tools = await discover_tool(client)
    user_request = input("You :")
    tool_name = planner(user_request, tools)
    print('tool_name',tool_name)
    
    result = await execute_tool(client,tool_name)
    print(result)
    final_result=generate_response(user_request,result)
    print(final_result)
    await disconnect(client)

if __name__ == "__main__":
    asyncio.run(main())