import os
import requests
import datetime
from dotenv import load_dotenv
current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, ".env")
load_dotenv(dotenv_path=env_path)
app_id = os.getenv("APP_ID")
api_key = os.getenv("API_KEY")
sheety_token = os.getenv("SHEETY_TOKEN")
url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
GENDER = "male"
WEIGHT_KG = 54
HEIGHT_CM = 180
AGE = 17

exercise_text=input("Tell me which exercise you did: ").title()
today=datetime.datetime.now()
date=today.strftime("%d-%m-%Y")
time=today.strftime("%H:%M:%S")

data = {
    "query": exercise_text,
    "gender": GENDER,
    "weight": WEIGHT_KG,
    "height": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id":app_id,
    "x-app-key": api_key
}
response = requests.post(url, headers=headers, json=data)
result = response.json()
user_data=result["exercises"][0]
duration=user_data["duration_min"]
calories=user_data["nf_calories"]

sheety_api = "https://api.sheety.co/4d63f7a01b054dff58eff9d8fa749af9/myWorkouts/sheet1"


information = {
    "sheet1": {
        "date": date,
        "time": time,
        "exercise": exercise_text,
        "duration":duration,
        "calories":calories
    }
}
sheety_headers = {

    "Authorization": f"Bearer {sheety_token}"
}

sheety_response= requests.post(
    url=sheety_api,json=information,headers=sheety_headers
)
sheety_result = sheety_response.json()

print(sheety_result)

