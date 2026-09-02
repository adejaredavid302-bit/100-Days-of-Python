# Day 40 – Flight Deal Finder

## Overview

On Day 40, I continued building the Flight Deal Finder project. The program searches for flights from a selected origin airport to multiple destinations stored in a Google Sheet.

The project first searches for direct flights. If no direct flight is available, it automatically searches again for indirect flights with stopovers.

The program finds the cheapest available flight, compares the price with the lowest price stored in the spreadsheet, updates the spreadsheet when a cheaper flight is found, and sends a notification.

## Topics Covered

* API requests with `requests`
* Request caching with `requests-cache`
* Working with JSON data
* Parsing nested JSON structures
* Object-oriented programming
* Classes and objects
* `__init__()` methods
* Creating custom objects
* Direct and indirect flight searches
* Conditional statements
* Exception handling with `try` and `except`
* Working with lists and dictionaries
* Finding the lowest value
* Calculating flight stopovers
* Google Sheets integration using Sheety
* Updating spreadsheet data with API requests
* Sending notifications with Twilio
* Environment variables with `.env`
* API authentication

## What I Learned

I learned how to parse complex flight data returned from an API and convert the important information into a `FlightData` object.

I also learned how to combine `best_flights` and `other_flights` into one list and search through all available flights to find the cheapest option.

Another important concept I learned was implementing a fallback system. The program first searches for direct flights, and if no direct flight is available, it searches again for indirect flights.

I also learned how to calculate the number of stops in a flight using the number of flight segments:

`number of stops = number of flight segments - 1`

The project also helped me understand how multiple classes can work together in a larger program.

## Challenges

One of the main challenges was understanding the complex nested JSON structure returned by the flight API.

I also had to carefully handle situations where:

* No flight data was returned.
* A direct flight was unavailable.
* A flight was missing a price.
* An indirect flight needed to be searched for.
* The cheapest flight needed to be compared with the price stored in the spreadsheet.

Understanding when to use separate `if` statements instead of `if` and `elif` was also an important part of the project.

## Reflection

Day 40 helped me understand how larger Python programs are structured using multiple classes and files.

The Flight Deal Finder project combines several concepts I have learned previously, including APIs, environment variables, JSON data, classes, exception handling, spreadsheets, caching, and notifications.

The project also showed me how a program can make decisions based on data. Instead of simply making one API request, the program can first search for direct flights and automatically fall back to indirect flights when necessary.

This was a challenging project, but completing it improved my understanding of how real-world Python automation programs can work.

## Course Progress

Completed Day 40 of the 100 Days of Code Python Bootcamp.

## About Me

I am learning Python and working towards becoming an AI Engineer while studying Electrical/Electronics Engineering.

I am building projects throughout the 100 Days of Code challenge to strengthen my programming, problem-solving, and software development skills.
