import requests

# Base URL for the local Flask application
FLASK_BASE_URL = "http://localhost:5000"

def get_geocode(location):
    """
    Retrieve geocoding information (latitude and longitude) for a given location.

    Args:
        location (str): The location for which to find geocoding information.

    Returns:
        tuple: A tuple containing the latitude and longitude of the location.

    Raises:
        ValueError: If no results are found for the specified location.
        ConnectionError: If there is a failure in connecting to the geocoding service.
    """
    location_query = location.replace(' ', '+')
    response = requests.get(f"https://nominatim.openstreetmap.org/search?format=json&q={location_query}")

    if response.status_code == 200:
        results = response.json()
        if results:
            return results[0]['lat'], results[0]['lon']
        else:
            raise ValueError("No results found for the specified location.")
    else:
        raise ConnectionError(f"Failed to connect to geocoding service: HTTP {response.status_code}")

def get_weather_forecast(location):
    """
    Get the weather forecast for a specified location.

    Args:
        location (str): The location for which to retrieve the weather forecast.

    Returns:
        dict: A dictionary containing weather forecast information.
    """
    response = requests.get(f"{FLASK_BASE_URL}/api/weather/forecast", params={"location": location})
    return response.json()

def get_flights(location, date):
    """
    Retrieve flight information based on location and date.

    Args:
        location (str): The city for the flight search.
        date (str): The date for the flight search.

    Returns:
        dict: A dictionary containing flight information.
    """
    response = requests.get(f"{FLASK_BASE_URL}/api/flights/search", params={"city": location, "date": date})
    return response.json()

def get_attractions(location):
    """
    Get attractions for a specified location.

    Args:
        location (str): The location for which to retrieve attractions.

    Returns:
        dict: A dictionary containing information about attractions.
    """
    response = requests.get(f"{FLASK_BASE_URL}/api/attractions/search", params={"location": location})
    return response.json()

def get_hotels(location, check_in, check_out, guests):
    """
    Retrieve hotel information based on location, check-in and check-out dates, and number of guests.

    Args:
        location (str): The location for hotel search.
        check_in (str): The check-in date.
        check_out (str): The check-out date.
        guests (int): The number of guests.

    Returns:
        dict: A dictionary containing hotel information.
    """
    response = requests.get(f"{FLASK_BASE_URL}/api/hotels/search",
                            params={"location": location, "check_in": check_in, "check_out": check_out, "guests": guests})
    return response.json()
