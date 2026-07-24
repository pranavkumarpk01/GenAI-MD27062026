from langchain.tools import tool

@tool
def get_weather(city:str) -> str:
    """
    Returns weather information.
    """

    weather = {
        "Goa": "Sunny 31C",
        "Manali": "14 C Snowy",
        "Banglore": "25 C Cloudy"
    }

    return weather.get(city, "weather unavailable")