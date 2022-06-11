import requests
from datetime import datetime

APP_ID = "04667e47"
API_KEY = "1ef57d87d50af03682d66aeb0f96cbb8"
USERNAME = "rebja"
TOKEN = "sldkjfsljeiosoef"

nutrix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/af1353de28e70f53f46272ad2e933293/rebecca'sWorkout/workouts"
text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": text,
    "gender": "female",
    "weight_kg": 60,
    "height_cm": 167,
    "age": 19
}

response = requests.post(nutrix_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)

    sheet_response = requests.post(
        sheety_endpoint,
        json=sheet_inputs,
        auth=(
            USERNAME,
            USERNAME,
        )
    )

