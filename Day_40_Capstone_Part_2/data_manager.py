import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()
sheety_endpoint=os.getenv("SHEETY_ENDPOINT")
sheety_user=os.getenv("USER_ENDPOINT")
class DataManager:
    def __init__(self):
        self.username = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.auth = HTTPBasicAuth(self.username, self.password)
        self.destination_data={}
        self.customer_data={}

    def get_destination_data(self):
        response=requests.get(sheety_endpoint, auth=self.auth)
        data=response.json()
        self.destination_data=data["sheet1"]
        return self.destination_data

    def update_lowest_price(self, destination_id, new_price):
        update_endpoint = f"{sheety_endpoint}/{destination_id}"

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
    def get_customer_emails(self):
        response=requests.get(sheety_user, auth=self.auth)
        data=response.json()
        self.customer_data=data["users"]
        return self.customer_data