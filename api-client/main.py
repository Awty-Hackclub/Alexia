import time
import requests, json


with open('key.json') as f:
        bot_settings = json.load(f)

key = bot_settings["openweather"]

city = "Houston"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
# HTTP request
response = requests.get(url)
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
else:
   # showing the error message
   print("Error in the HTTP request")

   