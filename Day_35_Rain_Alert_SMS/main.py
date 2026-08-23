import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv()
api_key=os.environ.get("API_KEY")
account_sid=os.environ.get("ACCOUNT_SID")
auth_token=os.environ.get("AUTH_TOKEN")


parameter={
    "lat":6.3350,
    "lon": 5.6037,
     "appid":api_key,
     "cnt":4
}
response=requests.get(url="http://api.openweathermap.org/data/2.5/forecast",params=parameter)
response.raise_for_status()

weather_data=response.json()

will_rain=False
for forcast in weather_data["list"]:
    for weather in forcast["weather"]:
        if weather["id"]<700:
            will_rain=True
if will_rain:
    twilio_client = Client(account_sid, auth_token)
    message = twilio_client.messages.create(
        to="+2348085221944",
        from_="+17372508034",
        body="sms_appointment_reminders")
    print(message.status)
