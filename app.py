# app.py (Flask Application)

from flask import Flask, jsonify, request, render_template
import requests
import xml.etree.ElementTree as ET
import xmltodict
import json

from core.config import settings
from core.utils import remove_nonprintable_chars
from services import hotel_service, ai_orchestrator

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index page of the Travel Companion API.
    """
    return render_template('index.html', title='TrAIvel Mate!')

@app.route('/api/process_request', methods=['POST'])
def process_request():
    """
    Process a user input request and return AI-generated response.
    """
    data = request.json
    user_input = data.get('user_input')

    response = ai_orchestrator.ask(user_input)
    print(response)
    return jsonify(response)

@app.route('/api/weather/forecast', methods=['GET'])
def get_weather_forecast():
    """
    Retrieve weather forecast for a specified location.
    """
    location = request.args.get('location')
    api_key = settings.WEATHER_API_KEY
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}")
    return jsonify(response.json())

@app.route('/api/flights/search', methods=['GET'])
def search_flights():
    """
    Search for flights based on city and date.
    """
    city = request.args.get('city')
    date = request.args.get('date')  # Format: YYYYMMDD

    iata_response = requests.get('https://timetable-lookup.p.rapidapi.com/airports/metros/',
                                 headers={'X-RapidAPI-Key': settings.RAPIDAPI_KEY,
                                          'X-RapidAPI-Host': 'timetable-lookup.p.rapidapi.com'})

    try:
        root = ET.fromstring(iata_response.content)
    except ET.ParseError:
        return jsonify({'error': 'Error parsing XML'}), 500

    to_airport = next((metro.attrib['IATACode'] for metro in root.findall('Metro')
                       if metro.attrib['Name'].lower() == remove_nonprintable_chars(city.lower())), None)

    if not to_airport:
        return jsonify({'error': 'IATA code not found for the specified city'}), 404

    timetable_response = requests.get(f'https://timetable-lookup.p.rapidapi.com/TimeTable/WAW/{to_airport}/{date}/',
                                      headers={'X-RapidAPI-Key': settings.RAPIDAPI_KEY,
                                               'X-RapidAPI-Host': 'timetable-lookup.p.rapidapi.com'})

    json_data = json.dumps(xmltodict.parse(timetable_response.content), indent=4)
    return jsonify(json_data)

@app.route('/api/attractions/search', methods=['GET'])
def search_attractions():
    """
    Search for attractions near a specified location.
    """
    location = request.args.get('location', default='Unknown Location')
    api_key = settings.ATTRACTIONS_API_KEY
    geocode_response = requests.get(f"https://api.opentripmap.com/0.1/en/places/geoname",
                                    params={"name": location, "apikey": api_key})
    lat, lon = geocode_response.json().get('lat'), geocode_response.json().get('lon')
    radius = 50

    response = requests.get(f"https://api.opentripmap.com/0.1/en/places/radius",
                            params={"radius": radius, "lon": lon, "lat": lat, "apikey": api_key})

    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data from OpenTripMap"}), response.status_code

@app.route('/api/hotels/search', methods=['GET'])
def search_hotels():
    """
    Search for hotels based on location, check-in, check-out dates, and number of guests.
    """
    location = request.args.get('location', 'Unknown Location')
    check_in = request.args.get('check_in')
    check_out = request.args.get('check_out')
    guests = request.args.get('guests', type=int, default=1)

    results = hotel_service.search_hotels(location, check_in, check_out, guests)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
