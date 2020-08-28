import time
import requests, json


with open('API_KEY.json') as f:
        bot_settings = json.load(f)

API_KEY = bot_settings["openweather"]

# importing requests and json

# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Houston"
# API key API_KEY = "Your API Key"
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
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
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperatureK} K")
   print(f"Temperature: {round(temperatureC, 2)} C")
   print(f"Temperature: {round(temperatureF, 2)} F")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
else:
   # showing the error message
   print("Error in the HTTP request")

   