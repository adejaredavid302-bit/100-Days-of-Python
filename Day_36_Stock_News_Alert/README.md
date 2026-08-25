# Day 36 – Stock News Alert

## Overview

On Day 36 of the 100 Days of Code challenge, I built a **Stock News Alert** project using Python.

The program checks the daily stock price of Tesla using the Alpha Vantage API. It compares the closing prices from two different days and calculates the percentage difference.

If the stock price changes by more than 5%, the program uses the NewsAPI to retrieve the latest relevant Tesla news. Twilio is then used to send the news articles through SMS.

## Topics Covered

* Working with APIs
* API parameters
* `requests`
* JSON data
* Alpha Vantage API
* NewsAPI
* Twilio API
* Environment variables
* `.env` files
* `python-dotenv`
* `os.getenv()`
* Percentage calculations
* Lists
* List comprehension
* F-strings
* Conditional statements
* Sending SMS messages

## What I Learned

* How to retrieve stock market data from an API.
* How to compare stock prices from different dates.
* How to calculate the percentage difference between two values.
* How to use a condition to determine when additional action should be taken.
* How to use NewsAPI to search for relevant company news.
* How to extract article titles and descriptions from JSON data.
* How to use environment variables to keep API credentials outside the Python source code.
* How multiple APIs can be combined to create a useful automated application.
* How Twilio can be used to send information through SMS.

## Challenges

One challenge was understanding the structure of the stock market data returned by Alpha Vantage.

Another challenge was working with nested JSON data from NewsAPI and extracting the information needed from each article.

I also had to understand how environment variables and `.env` files can be used to protect API credentials.

## Reflection

Day 36 was an important project because it combined several concepts I had previously learned.

Instead of working with only one API, I connected **Alpha Vantage, NewsAPI, and Twilio** together to create an automated stock notification system.

This project helped me understand how different APIs can work together to build a more practical application.

## Course Progress

**Day 36 / 100**

36 days completed.

## About Me

I am learning Python through Angela Yu's 100 Days of Code challenge as part of my journey toward becoming an AI Engineer.

I am continuing to improve my Python skills by building practical projects and learning how to work with APIs, automation, environment variables, and external services.
