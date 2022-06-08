import requests

owm_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "4488b09779e0ef760588e5ea994a5ff7"
weather_params = {
    "lat": 43.653225,
    "lon": -79.383186,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(owm_endpoint, params=weather_params)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    print("bring an umbrella")
