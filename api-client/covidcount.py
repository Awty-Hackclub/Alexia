import requests


def count(country):
    response = requests.get(
        f'https://api.covid19api.com/total/country/{country}')
    data = response.json()

    recent = data[-1]
    return {
        'confirmed': recent['Confirmed'],
        'deaths': recent['deaths'],
        'recovered': recent['recovered']
    }
