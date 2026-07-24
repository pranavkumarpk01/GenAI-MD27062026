from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from utils.llm import llm
from tools.weater_tool import get_weather
from tools.hotel_tool import search_hotels
from tools.flight_tool import search_flights
from prompts.system_prompt import SYSTEM_PROMPT
from memory.memory import memory

tools = [
    get_weather,
    search_hotels,
    search_flights
]

prompt = ChatPromptTemplate.from_messages(

[

("system", SYSTEM_PROMPT),

("placeholder","{chat_history}"),

("human","{input}"),

("placeholder","{agent_scratchpad}")

]

)

agent = create_tool_calling_agent(
    llm,
    tools,
    prompt
)

executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True
)