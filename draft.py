# Trying to figure out where to begin or what api I want to utilize for this project. May use a weather api, maybe music, maybe add ML capabilities if I get that far
# using this file to understand how to load and use apis for my project
# import numpy as np
# import pandas as pd
import json
import requests

# going to use operweathermap.org api,
# free account lets us call current weather and 3hr 5 day forecasts with 60 calls/minute
api_key = 'bd4cd26c3163150080ad612f6ee5eb36' # api key from openweathermap.org
base_url = 'https://api.openweathermap.org/data/2.5/weather?'
city = input('To check the weather, please type the city you would like to see: ')
print('You have typed ' + city)
