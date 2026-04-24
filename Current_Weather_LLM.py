import requests
import json
import aisuite as ai
from dotenv import load_dotenv
from datetime import datetime
_ = load_dotenv()
# Create an instance of the AISuite client
client = ai.Client()

def get_weather_from_ip()->str:
    """
    Gets the current, high, and low temperature in Fahrenheit for the user's
    location and returns it to the user.
    """
    # Get location coordinates from the IP address
    lat, lon = requests.get('https://ipinfo.io/json').json()['loc'].split(',')
    # Set parameters for the weather API call
    params = {
    "latitude": lat,
    "longitude": lon,
    "current": "temperature_2m",
    "daily": "temperature_2m_max,temperature_2m_min",
    "temperature_unit": "fahrenheit",
    "timezone": "auto"
    }
    # Get weather data
    weather_data = requests.get("https://api.open-meteo.com/v1/forecast", params).json()
    # Format and return the simplified string
    return (
    f"Current: {weather_data['current']['temperature_2m']}°F, "
    f"High: {weather_data['daily']['temperature_2m_max'][0]}°F, "
    f"Low: {weather_data['daily']['temperature_2m_min'][0]}°F"
    )

prompt = "Can you get the weather for my location?"
response = client.chat.completions.create(
model="openai:o4-mini",
messages=[{"role": "user", "content": (
prompt
)}],
tools=[get_weather_from_ip],
max_turns=5
)
print(response)