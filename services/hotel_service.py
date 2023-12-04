# app/services/hotel_service.py

def search_hotels(location, checkin, checkout, guests):
    """
    Mock function to simulate searching for hotels based on given criteria.

    Args:
        location (str): The location where the user wants to find hotels.
        checkin (str): The check-in date for the hotel stay.
        checkout (str): The check-out date for the hotel stay.
        guests (int): The number of guests for the hotel stay.

    Returns:
        list: A list of dictionaries, each representing a hotel with its details.

    Note:
        In a real application, this would query a database or an external API.
        The current implementation uses hard-coded data for demonstration purposes.
    """

    # Simulated hotel data
    mock_hotels = [
        {"name": "Hotel Sunrise", "location": location, "price": 100, "rating": 4.5},
        {"name": "Mountain View Inn", "location": location, "price": 80, "rating": 4.0},
        {"name": "City Center Lodge", "location": location, "price": 120, "rating": 4.8}
    ]

    # TODO: Add logic to filter hotels based on check-in/check-out dates and number of guests
    # This could involve checking the availability of rooms and adjusting prices based on demand

    # For now, simply return the mock data
    return mock_hotels

# Example usage:
# hotels = search_hotels("New York", "2023-07-10", "2023-07-15", 2)
