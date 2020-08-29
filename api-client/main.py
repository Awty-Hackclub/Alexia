import time
import requests
import json
import csv

with open('key.json') as f:
    key = json.load(f)

configuration = {
    "key": key["openweather"],
    "city": key["city"],
    "country": key["country"],
    "filename": "data.csv"
}

response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={configuration['city']}&appid={configuration['key']}")

fields = ['temp', 'humidity', 'pressure', 'weather']

if response.status_code == 200:
    try:
        with open(configuration["filename"], "w+") as c:
            csvwriter = csv.writer(c)
            csvwriter.writerow(fields)
            data = response.json()
            main = data['main']
            rows = [
                [main['temp'], main['humidity'], main['pressure'], data['weather']]
            ]
            csvwriter.writerows(rows)
    except ValueError as e:
        print(f"Error: {e}")
