# Day 38: Workout Tracking Using Google Sheets
from datetime import datetime
import requests

APP_ID = "d948de71"
API_KEY = "e43dff83a303cfc95a58e162493cccce"

user_input = str(input("Tell me which exercies you did: "))

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    # "x-remote-user-id": "dmartinm",
}


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

params = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 77,
    "height_cm": 170,
    "age": 26,
}
response = requests.post(url=exercise_endpoint, json=params, headers=headers)
response.raise_for_status()

sheets_endpoint = "https://api.sheety.co/3f56e49384411eb75ae1a48efce2f50f/workoutTracking/workouts"

exercies_list = response.json()["exercises"]

# response = requests.get(
#     url="https://api.sheety.co/3f56e49384411eb75ae1a48efce2f50f/workoutTracking/workouts")
# print(response.json())

sheets_header = {
    "Authorization": "Basic ZGllZ286b3Nqc2FzYWxuZ2xza2RuZw==",
}

for exercise in exercies_list:
    exercise_type = str(exercise["name"]).title()
    exercise_duration = str(exercise["duration_min"])
    exercise_calories = str(exercise["nf_calories"])
    todays_date = datetime.now()
    date = todays_date.strftime("%d/%m/%Y")
    time = todays_date.strftime("%H:%M:%S")

    exercise_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_type,
            "duration": exercise_duration,
            "calories": exercise_calories,
        }
    }

    response = requests.post(
        url=sheets_endpoint, json=exercise_params, headers=sheets_header)
    response.raise_for_status()
    print(response.text)
