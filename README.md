# TrAIvel Mate!

## Overview
TrAIvel Mate is a comprehensive solution for travelers, providing essential information like hotel bookings, flight details, weather forecasts, and local attractions. This API serves as a one-stop portal for all travel-related inquiries, leveraging various external APIs and internal logic to deliver accurate and up-to-date information.

## Features
- **Hotel Search**: Find hotels based on location, check-in/check-out dates, and number of guests.
- **Flight Information**: Get flight details for specific dates and destinations.
- **Weather Forecast**: Access up-to-date weather information for any location.
- **Attractions Lookup**: Discover local attractions in your travel destination.

## Installation
Clone the repository and install dependencies:

git clone https://github.com/xartous/traivel.git
cd traivel
pip install -r requirements.txt

## Configuration
Set up your environment variables in a `.env` file:
DATABASE_URL="your_database_url"
GOOGLE_MAPS_API_KEY="your_api_key"
RAPIDAPI_KEY="your_rapidapi_key"

## Usage
Run the application:
python app.py

Access the API at `http://{server}:{port}/api`.

## Endpoints
- `/api/hotels/search`: Search for hotels.
- `/api/flights/search`: Fetch flight information.
- `/api/weather/forecast`: Get weather forecasts.
- `/api/attractions/search`: Find local attractions.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License
This project is licensed under the [MIT License](LICENSE.md).

## Contact
For any inquiries or issues, please open an issue in the GitHub repository.

## Acknowledgments
Special thanks to all contributors and users of the TrAIvel Mate.
