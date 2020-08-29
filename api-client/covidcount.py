import requests

response = requests.get('https://api.covid19api.com/total/country/united-states')
data = response.json()

recent = data[-1]
fields = ['Date', 'Confirmed', 'Deaths', 'Recovered']

for i in fields:
    print(i, recent[i])