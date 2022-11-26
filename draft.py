# Trying to figure out where to begin or what api I want to utilize for this project. May use a weather api, maybe music, maybe add ML capabilities if I get that far
# using this file to understand how to load and use apis for my project
# import numpy as np
# import pandas as pd
import json
import requests

# going to use operweathermap.org api,
# free account lets us call current weather and 3hr 5 day forecasts with 60 calls/minute
api_key = 'bd4cd26c3163150080ad612f6ee5eb36' # api key from openweathermap.org
base_url = 'https://api.openweathermap.org/data/2.5/weather?' # base url for later use
city = input('To check the weather, please type the city you would like to see: ') # city for which you want to extract the data of
url = base_url+ 'q=' + city +  "&appid=" + api_key # allows us to pull a json from 

# Testing response and then going to proceed if =200
response = requests.get(url) # Should output 200 if the city is correct
if response.status_code==200
    data = response.json()
    main = data['main']
