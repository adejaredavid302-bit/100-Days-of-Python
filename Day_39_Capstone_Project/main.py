#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests_cache
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600}
)

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)
tomorrow = datetime.now()+ timedelta(days=1)
six_months_from_today = tomorrow + timedelta(days=6*30)

flight_search = FlightSearch()
flights=flight_search.check_flights(
    origin_city_code="LHR",
    destination_city_code="CDG",
    from_time=tomorrow,
    to_time=six_months_from_today,
)
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LHR"

for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
    cheapest_flight = find_cheapest_flight(flights, return_date=six_months_from_today.strftime("%Y-%m-%d"))
    pprint(f"{destination['city']}: GBP {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        pprint(f"Lower price flight found to {destination['city']}!")
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)

    message = (
        f"Low price alert!\n" f"From: {cheapest_flight.origin_city}\n" f"To: {cheapest_flight.destination_city}\n"
        f"" f"Price: GBP {cheapest_flight.price}\n" f"Departure: {cheapest_flight.out_date}\n"
        f"Return: {cheapest_flight.return_date}")
    notification_manager.send_whatsapp(message)