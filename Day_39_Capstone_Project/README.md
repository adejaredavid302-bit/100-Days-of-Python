# Day 39 – Flight Deal Finder

## Overview

Today, I built a **Flight Deal Finder** that searches for cheap flights and compares them with target prices stored in a Google Sheet.

The project uses several classes and APIs working together. It retrieves destination information from a spreadsheet, searches for available flights, finds the cheapest flight, compares its price with the target price, updates the spreadsheet when a cheaper flight is found, and sends a notification.

This project helped me understand how larger Python applications can be separated into different classes and modules.

## Topics Covered

* Object-Oriented Programming
* Classes and objects
* APIs
* Sheety API
* Flight Search API
* Twilio
* Environment variables
* `.env` files
* `python-dotenv`
* `requests`
* `requests-cache`
* API authentication
* JSON data
* IATA airport codes
* `datetime`
* `timedelta`
* Python modules
* Importing custom classes
* Comparing values
* Automated notifications

## What I Learned

I learned how to organize a larger Python project by separating different responsibilities into different classes.

The project uses:

* `DataManager` to communicate with the spreadsheet.
* `FlightSearch` to search for flights.
* `FlightData` to process flight information and find the cheapest flight.
* `NotificationManager` to send notifications when a cheaper flight is found.

I also learned how to use `requests_cache` to cache API requests:

```python
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600
    }
)
```

This helps reduce unnecessary API requests while making sure that requests to Sheety are not cached.

I also used `datetime` and `timedelta` to calculate the flight-search period:

```python
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = tomorrow + timedelta(days=6 * 30)
```

The program then loops through each destination in the spreadsheet and searches for flights:

```python
for destination in sheet_data:
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
```

Finally, the program compares the cheapest flight price with the target price in the spreadsheet. If the flight is cheaper, the spreadsheet is updated and a notification is sent.

## Challenges

One challenge was understanding how several classes work together in a single project.

Instead of putting all the code in one file, I had to understand how `DataManager`, `FlightSearch`, `FlightData`, and `NotificationManager` communicate with the main program.

Another challenge was understanding how API data is passed between different parts of the program.

I also learned that API credentials should be stored in environment variables instead of being written directly into the source code.

## Reflection

Day 39 was an important project because it felt much closer to a real-world application than many of my earlier projects.

I was able to combine APIs, object-oriented programming, external data, caching, a spreadsheet, and notifications into one application.

The project showed me how different components can work together to automate a useful task.

It also reinforced the importance of writing modular code instead of putting everything into one large Python file.

## Course Progress

I am continuing through Angela Yu's **100 Days of Code: The Complete Python Pro Bootcamp**.

Day 39 focused on building a flight deal finder using APIs, object-oriented programming, data management, and automated notifications.

## About Me

I am learning Python through the 100 Days of Code challenge and building projects to improve my programming and problem-solving skills.

My long-term goal is to become an **AI Engineer**, while developing strong foundations in Python, APIs, automation, software engineering, and real-world application development.

