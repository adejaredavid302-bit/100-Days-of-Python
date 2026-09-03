import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()
SHEETY_ENDPOINT="https://api.sheety.co/4d63f7a01b054dff58eff9d8fa749af9/flightWork/sheet1"
class DataManager:
    def __init__(self):
        self.username = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.auth = HTTPBasicAuth(self.username, self.password)
        self.destination_data={}
    def get_destination_data(self):
        response=requests.get(SHEETY_ENDPOINT, auth=self.auth)
        data=response.json()
        self.destination_data=data["sheet1"]
        return self.destination_data

    def update_lowest_price(self, destination_id, new_price):
        update_endpoint = f"{SHEETY_ENDPOINT}/{destination_id}"

        body = {
            "sheet1": {
                "lowestPrice": new_price
            }
        }

        response = requests.put(
            update_endpoint,
            json=body,
            auth=self.auth
        )
        print(response.text)