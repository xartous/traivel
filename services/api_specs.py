apiSpec_weather = """
Weather API Documentation
-------------------------
- Base URL: http://127.0.0.1:5000/api
- Endpoint: /weather/forecast
- Example API call: http://127.0.0.1:5000/api/weather/forecast?location=Paris

Purpose:
    Retrieve weather information based on a given location.

Request Format:
    GET request with location name (city)

Response Instructions:
    - Respond with the FIRST result - only the temperature value.
    - If temperature is in Kelvin, convert to Celsius by subtracting 273.15.
    - If no data is returned, apologize and indicate no results found.
"""

apiSpec_attractions = """
Attractions API Documentation
-----------------------------
- Base URL: http://127.0.0.1:5000/api
- Endpoint: /attractions/search
- Example API call: http://127.0.0.1:5000/api/attractions/search?location=Paris

Purpose:
    Retrieve local attractions information based on a given location.

Request Format:
    GET request with location name (city)

Response Instructions:
    - Respond with the TOP THREE results best suited for the current weather.
    - If no data is returned, apologize and indicate no results found.
"""

apiSpec_hotels = """
Hotels API Documentation
------------------------
- Base URL: http://127.0.0.1:5000/api
- Endpoint: /hotels/search
- Example API call: http://127.0.0.1:5000/api/hotels/search?location=Paris

Purpose:
    Retrieve a list of hotels based on a given location.

Request Format:
    GET request with location name (city)

Response Instructions:
    - Respond with the FIRST result.
    - If no data is returned, apologize and indicate no results found.
"""

apiSpec_flights = """
Flights API Documentation
-------------------------
- Base URL: http://127.0.0.1:5000/api
- Endpoint: /flights/search
- Example API call: http://127.0.0.1:5000/api/flights/search?location=Paris

Purpose:
    Retrieve flights information based on a given location.

Request Format:
    GET request with location name (city)

Response Instructions:
    - Respond with the TOP THREE results.
    - If no data is returned, apologize and indicate no results found.
"""
