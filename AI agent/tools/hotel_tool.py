from langchain.tools import tool


@tool
def search_hotels(city: str):

    hotels = {

        "Goa":[
            "Taj Resort",
            "Novotel",
            "Holiday Inn"
        ],

        "Manali":[
            "Snow Peak",
            "Hill View"
        ]
    }

    return hotels.get(city, [])