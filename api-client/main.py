import time
import requests, json


with open('key.json') as f:
        bot_settings = json.load(f)

key = bot_settings["openweather"]

city = "Houston"

URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
   # getting temperature
   temperatureK = main['temp']
   temperatureC = temperatureK - 273.15
   temperatureF = temperatureC*(9/5) + 32
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   # weather report
   report = data['weather']
   print(f"{city}:-^30}")
   print(f"Temperature: {temperatureK} K")
   print(f"Temperature: {round(temperatureC, 2)} C")
   print(f"Temperature: {round(temperatureF, 2)} F")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
else:
   # showing the error message
   print("Error in the HTTP request")

   