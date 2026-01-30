import requests
import os
from dotenv import load_dotenv


# get our API key from env
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

def pull(location):
    params = {
    "location" : location, 
    "key" : API_KEY,
    "unitGroup" : "metric",
    "include" : "current"
    }
    response = requests.get(BASE_URL, params, timeout = 10)
    data = response.json()
    current = data.get("currentConditions")
    print(current)


location = input("Hello! Name a location \n")

if location:
    pull(location)

