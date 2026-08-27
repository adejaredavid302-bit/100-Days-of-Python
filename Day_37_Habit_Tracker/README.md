# Day 37 – Habit Tracker with Pixela API

## Overview

On Day 37 of the 100 Days of Code challenge, I built a **Habit Tracker** using Python and the Pixela API.

The program connects to Pixela and uses HTTP POST requests to create and update data on a graph. In this project, I recorded a cycling activity of 8.29 km for the current day.

## Topics Covered

* `requests` library
* HTTP requests
* POST requests
* API endpoints
* API parameters
* JSON data
* HTTP headers
* Authentication tokens
* Python `datetime`
* `strftime()`
* F-strings
* Pixela API
* Creating API users
* Creating graphs
* Adding data to graphs

## What I Learned

* How to use `requests.post()` to send information to an API.
* How API endpoints are constructed using variables and f-strings.
* How to send information using JSON.
* How HTTP headers can be used to provide authentication information.
* How to generate today's date using Python's `datetime`.
* How `strftime("%Y%m%d")` converts a date into the format required by the API.
* How APIs can use tokens to authenticate requests.
* How to send numerical data to an API and record it on a graph.

## Challenges

One of the challenges was understanding the difference between the API endpoint, parameters, and headers.

I also had to understand how the Pixela API uses the username and graph ID to identify where the new data should be stored.

## Reflection

Day 37 helped me understand POST requests more clearly.

Instead of only retrieving information from an API using `requests.get()`, I learned how to **send information to an API using `requests.post()`**.

The project also helped me understand how different pieces of information such as the endpoint, headers, and JSON data work together when communicating with an API.

## Course Progress

**Day 37 / 100**

37 days completed.

## About Me

I am learning Python through Angela Yu's 100 Days of Code challenge as part of my journey toward becoming an AI Engineer.

I am continuing to improve my Python skills by building practical projects and learning how APIs, HTTP requests, authentication, and external services work.
