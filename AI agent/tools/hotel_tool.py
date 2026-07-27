from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

_tavily = TavilySearchResults(max_results=3)


@tool
def search_hotels(city: str) -> str:
    """Searches the live web for current hotel options in the given city."""
    return str(_tavily.invoke(f"best hotels to stay in {city}"))
