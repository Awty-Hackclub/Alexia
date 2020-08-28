import time
import requests
import json
import csv

with open('key.json') as f:
    bot_settings = json.load(f)

key = bot_settings["openweather"]

city = "Houston"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    main = data['main']
    # temperatureK = main['temp']
    # temperatureC = temperatureK - 273.15
    # temperatureF = temperatureC*(9/5) + 32
    # humidity = main['humidity']
    # pressure = main['pressure']
    # report = data['weather']
else:
    print("Error in the HTTP request")
