import datetime as dt
import requests
from dotenv import load_dotenv
import os

load_dotenv()

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = round(kelvin - 273.15, 1)
    fahrenheit = round(celsius * (9/5) + 32, 1)
    return celsius, fahrenheit

BASE_URL='https://api.openweathermap.org/data/2.5/weather?'
API_KEY = os.getenv("API_KEY")
CITY="Brno"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url=url).json()

temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(response["main"]["temp"])
print(f"Weather data for: {CITY}")
print(f"Temperature: {temp_celsius}°C ({temp_fahrenheit}°F)")

humidity = response["main"]["humidity"]
wind_speed = response["wind"]["speed"]
description = response["weather"][0]["description"]
print(f"Humidity: {humidity}%")
print(f"Wind speed: {wind_speed} km/h")
print(f"Description: {description}")