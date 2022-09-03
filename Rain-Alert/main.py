import requests
API_KEY = "8ed4e9412e2b8e447572ddb968492e1b"

URL = "https://api.openweathermap.org/data/2.5/weather"

URL_params = {
    "lat": 4.0511,
    "lon": 9.7679,
    "appid":API_KEY,
    "exclude":"current, minutely,daily"
}

response = requests.get(URL, params=URL_params)

response.raise_for_status()
weather_data = response.json()
weather_data_main = weather_data["weather"][:12]
print(weather_data_main["weather"][0]["main"]) 
#https://api.openweathermap.org/data/2.5/weather?lat=4.0511&lon=9.7679&appid=66bab36dd34033c4eb91655f7c653ab3
