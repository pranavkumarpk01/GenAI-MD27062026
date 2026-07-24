from langchain.tools import tool


@tool
def search_flights(destination: str):

    flights = {

        "Goa":"Indigo ₹5200",

        "Manali":"Delhi Flight + Cab"

    }

    return flights.get(destination, "No flights found")