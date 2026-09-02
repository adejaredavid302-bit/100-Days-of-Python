# This file will need to use the DataManager, FlightSearch,
# FlightData, NotificationManager classes to achieve the program requirements.

import requests_cache
from pprint import pprint
from Day_39_Capstone_Project.data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager


requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600
    }
)

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
customer_data=data_manager.get_customer_emails
customer_email_list=[row["whatIsYourEmail?"] for row in customer_data]
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = tomorrow + timedelta(days=6 * 30)

flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LHR"


for destination in sheet_data:

    pprint(f"Getting direct flights for {destination['city']}...")

    # Search for direct flights first
    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iata"],
        from_time=tomorrow,
        to_time=six_months_from_today,
        is_direct=True
    )

    cheapest_flight = find_cheapest_flight(
        flights,
        return_date=six_months_from_today.strftime("%Y-%m-%d")
    )

    # If there is no direct flight, search for indirect flights
    if cheapest_flight.price == "N/A":

        print(
            f"No direct flight to {destination['city']}. "
            f"Looking for indirect flights..."
        )

        flights = flight_search.check_flights(
            origin_city_code=ORIGIN_CITY_IATA,
            destination_city_code=destination["iata"],
            from_time=tomorrow,
            to_time=six_months_from_today,
            is_direct=False
        )

        cheapest_flight = find_cheapest_flight(
            flights,
            six_months_from_today.strftime("%Y-%m-%d")
        )

    # Print the final cheapest flight found
    pprint(f"{destination['city']}: GBP {cheapest_flight.price}")

    # Check whether the flight is cheaper than the saved price
    if (cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]
    ):

        pprint(f"Lower price flight found to {destination['city']}!")

        data_manager.update_lowest_price(
            destination["id"],cheapest_flight.price)

        message = (
            f"Low price alert!\n"
            f"From: {cheapest_flight.origin_airport}\n"
            f"To: {cheapest_flight.destination_airport}\n"
            f"Price: GBP {cheapest_flight.price}\n"
            f"Departure: {cheapest_flight.out_date}\n"
            f"Return: {cheapest_flight.return_date}"
        )

        if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
            if cheapest_flight.stops == 0:
                message = f"Low price alert! Only GBP {cheapest_flight.price} to fly direct " \
                          f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                          f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
            else:
                message = f"Low price alert! Only GBP {cheapest_flight.price} to fly " \
                          f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                          f"with {cheapest_flight.stops} stop(s) " \
                          f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."

            print(f"Check your email. Lower price flight found to {destination['city']}!")

        notification_manager.send_whatsapp(message)
        notification_manager.send_emails(customer_email_list,message)