# Day 33 – ISS Overhead Notification

## Overview

On Day 33 of the 100 Days of Code challenge, I built an **ISS Overhead Notification System** using Python.

The program uses APIs to determine the current position of the International Space Station and the sunrise/sunset times for a specific location. It checks whether the ISS is close to my location and whether it is currently nighttime. If both conditions are true, the program sends an email notification telling me to look up and see the ISS.

## Topics Covered

* Making API requests with `requests`
* Working with APIs
* Using JSON data
* Getting data from API responses
* Using API parameters
* HTTP status codes and `raise_for_status()`
* Creating and using functions
* Conditional statements
* Boolean values
* `while` loops
* `time.sleep()`
* Working with `datetime`
* Sending emails with `smtplib`
* Combining multiple Python concepts into one project

## What I Learned

* How to send requests to an API using `requests.get()`.
* How to use `response.json()` to convert API data into Python data.
* How to access information inside nested dictionaries.
* How API parameters can be sent using the `params` argument.
* How `raise_for_status()` helps detect unsuccessful HTTP requests.
* How to create functions that return `True` or `False`.
* How to use latitude and longitude to determine whether the ISS is nearby.
* How to use sunrise and sunset information to determine whether it is nighttime.
* How to combine API data with conditions and automation.
* How to send an automated email using Gmail's SMTP server.

## Challenges

The biggest challenge was understanding how different APIs return different types of data.

I also had to understand how to access nested JSON data and how to combine the ISS position with sunrise/sunset information.

Another challenge was connecting several concepts together: API requests, functions, conditions, loops, and email automation.

## Reflection

Day 33 was a major step because I started working with **real-world data from APIs** instead of only using data created inside my program.

I also learned that understanding the structure of the data returned by an API is just as important as knowing how to make the request.

This project showed me how Python can be used to create programs that continuously monitor information and automatically perform an action when certain conditions are met.

## Course Progress

**Day 33 / 100**

33 days completed.

## About Me

I am learning Python through Angela Yu's 100 Days of Code challenge as part of my journey toward becoming an AI Engineer.

I am currently building my programming fundamentals and learning how to combine different Python concepts into practical projects.
