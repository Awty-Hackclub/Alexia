import requests


def count():
    response = requests.get(
        'https://api.covid19api.com/total/country/united-states')
    data = response.json()

    recent = data[-1]
    return {
        'confirmed': recent['Confirmed'],
        'deaths': recent['deaths'],
        'recovered': recent['recovered']
    }
