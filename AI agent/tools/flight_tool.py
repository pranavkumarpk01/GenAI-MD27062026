from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

_tavily = TavilySearchResults(max_results=3)


@tool
def search_flights(destination: str) -> str:
    """Searches the live web for current flight options/prices to the destination."""
    return str(_tavily.invoke(f"flight tickets and prices to {destination}"))
