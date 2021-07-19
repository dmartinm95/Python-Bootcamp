# Day 35: Keys, Authentication and Environment Variables
import requests

api_key = "0f037a272652469d272332ba9fd9b71a"

parameters = {
    "lat": 49.171720,
    "lon": -122.638780,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()

hourly_data_list = weather_data["hourly"]

will_rain = False

for i in range(0, 12):
    weather_code = hourly_data_list[i]["weather"][0]["id"]
    if int(weather_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
