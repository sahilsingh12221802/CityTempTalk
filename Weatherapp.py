import requests
import json
import os

city = input("Enter the name of the city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=7a70f8de67d849339fd213034230109&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
l = wdic["location"]["region"]
lat = wdic["location"]["lat"]
lon = wdic["location"]["lon"]
time = wdic["location"]["localtime"]



os.system(f"say 'the location of {city} is {l} region'")
os.system(f"say 'the current weather in the {city} is {w} degrees'")
os.system(f"say '{city} lies in the latitude between {lat} and'")
os.system(f"say '{city} lies in the longitude between {lon}'")
os.system(f"say 'the current time in {city} is {time}'")