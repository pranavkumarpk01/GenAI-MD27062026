from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory

from utils.llm import llm
from tools.weater_tool import get_weather
from tools.hotel_tool import search_hotels
from tools.flight_tool import search_flights
from tools.search_tool import web_search
from prompts.system_prompt import SYSTEM_PROMPT
from memory.memory import get_session_history

tools = [
    get_weather,
    search_hotels,
    search_flights,
    web_search,
]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

agent = create_tool_calling_agent(llm, tools, prompt)

base_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
)

# Wraps the executor so chat history is loaded/saved from SQLite per session_id.
executor = RunnableWithMessageHistory(
    base_executor,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)
