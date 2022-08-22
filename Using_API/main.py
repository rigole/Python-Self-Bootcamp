from time import time
import requests
from datetime import datetime


MY_LAT = 	7.369722
MY_LONG = 12.354722


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()



iss_longitude = float(data["iss_position"]["longitude"])

iss_latitude = float(data["iss_position"]["latitude"])

#iss_position = (longitude, latitude)

#print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted":0,
}

reponse = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()