import time
import requests
import json
from covidcount import count
import serial

with open('key.json') as f:
    key = json.load(f)

configuration = {
    "key": key["openweather"],
    "city": key["city"],
    "country": key["country"],
}

response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={configuration['city']}&appid={configuration['key']}")

arduino = serial.Serial('/dev/ttyACM0', 9600)

while True:
    if response.status_code == 200:
        try:
            covid_data = count(key["country"])
            data = response.json()
            main = data['main']
            data_string = f"{main['temp']},{main['humidity']},{main['pressure']},{main['weather']},{covid_data['confirmed']},{covid_data['deaths']},{covid_data['recovered']}"
            arduino.write(bytes(data_string))
        except ValueError as e:
            print(f"Error: {e}")
            break
    time.sleep(600)  # every 10 minutes
