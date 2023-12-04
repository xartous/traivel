# app/services/map_integration.py
import requests
from urllib.parse import urlencode
from core.config import settings

def get_map_details(location: str):
    """
    Fetch map details for a given location using the Google Maps API.

    Args:
        location (str): The location for which to fetch map details.

    Returns:
        dict: A dictionary containing the map details as returned by the Google Maps API.

    Raises:
        Exception: If the request to the Google Maps API fails.
    """
    # Ensure the location is properly URL encoded
    encoded_location = urlencode({"address": location})

    # Construct the full URL with the API key
    maps_url = f"https://maps.googleapis.com/maps/api/geocode/json?{encoded_location}&key={settings.GOOGLE_MAPS_API_KEY}"

    # Make the request to the Google Maps API
    response = requests.get(maps_url)

    # Check for a successful response
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching map details: HTTP {response.status_code}")

# Example usage:
# map_details = get_map_details("1600 Amphitheatre Parkway, Mountain View, CA")
