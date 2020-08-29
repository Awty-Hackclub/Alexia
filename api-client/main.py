import time
import requests
import json
import csv
from covidcount import count

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

fields = ['temp', 'humidity', 'pressure',
          'weather', 'confirmed', 'deaths', 'recovered']
while True:
    if response.status_code == 200:
        try:
            with open(configuration["filename"], "w+") as c:
                covid_data = count(key["country"])
                csvwriter = csv.writer(c)
                csvwriter.writerow(fields)
                data = response.json()
                main = data['main']
                rows = [
                    [main['temp'], main['humidity'],
                        main['pressure'], data['weather'], covid_data['confirmed'], covid_data['deaths'], covid_data['recovered']]
                ]
                csvwriter.writerows(rows)
        except ValueError as e:
            print(f"Error: {e}")
            break
    time.sleep(600)  # every 10 minutes
