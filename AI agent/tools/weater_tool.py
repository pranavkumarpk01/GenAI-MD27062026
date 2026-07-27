from langchain.tools import tool
import requests


@tool
def get_weather(city: str) -> str:
    """Returns real, current weather for a given city (Open-Meteo API, no key needed)."""
    try:
        geo = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city, "count": 1},
            timeout=10,
        ).json()

        if not geo.get("results"):
            return f"Could not find location: {city}"

        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]

        data = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": lat, "longitude": lon, "current_weather": True},
            timeout=10,
        ).json()

        cw = data.get("current_weather", {})
        return f"{city}: {cw.get('temperature')}°C, wind {cw.get('windspeed')} km/h"
    except Exception as e:
        return f"weather unavailable ({e})"
