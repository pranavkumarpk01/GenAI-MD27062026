from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

_tavily = TavilySearchResults(max_results=3)


@tool
def web_search(query: str) -> str:
    """Search the live web for up-to-date travel info: events, visa rules,
    prices, news, anything not covered by the other tools."""
    return str(_tavily.invoke(query))
