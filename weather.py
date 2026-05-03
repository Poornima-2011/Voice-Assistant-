# weather.py
import requests

def get_weather(city: str):
    # Example API request to get weather data (using OpenWeatherMap API)
    api_key = '8a9f68245b9eb2e30de5ed29536e4666'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    data = response.json()
    
    if data['cod'] == 200:
        temperature = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        return f"The weather in {city} is {weather_desc} with a temperature of {temperature}°C."
    else:
        return f"Could not retrieve weather for {city}."
