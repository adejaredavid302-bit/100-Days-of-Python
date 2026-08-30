import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
load_dotenv()

tomorrow=datetime.now()+timedelta(days=1)
six_month_later=datetime.now()+timedelta(days=6 * 30)
flight_api_endpoint=f"https://app.100daysofpython.dev/v1/flights/search"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flights_api = os.getenv("FLIGHT_API_KEY")

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        parameter = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self.flights_api,

        }
        response= requests.get(url=flight_api_endpoint,params=parameter)
        response.raise_for_status()


        data = response.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data

