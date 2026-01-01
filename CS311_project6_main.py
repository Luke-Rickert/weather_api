#  CS311 Project 6  -- Luke Rickert
#  An API project that pulls weather data. 
#  The api key is a limited trial so it may no longer work

import requests

def get_weather_json(url):
    return requests.get(url).json()

def extract_current_temp(currJSON):
    return currJSON[0]["Temperature"]["Imperial"]["Value"]

def extract_min(forcastJSON):
    return forcastJSON["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]

def extract_max(forcastJSON):
    forcastJSON["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]


forcastUrl = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/347810?apikey=MZF3xXs00cPTzGGvYofyDxo2d6Y9pmm4"
currentUrl = "http://dataservice.accuweather.com/currentconditions/v1/347810?apikey=MZF3xXs00cPTzGGvYofyDxo2d6Y9pmm4"


print("Temperature Forcast Denver, CO:")
print("Current:", extract_current_temp(get_weather_json()))
print("High:", extract_max(get_weather_json()))
print("Low:", extract_min(get_weather_json()))

