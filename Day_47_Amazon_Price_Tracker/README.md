# Day 47 – Amazon Price Tracker

## Overview

Day 47 focused on web scraping, HTTP request headers, environment variables, and email automation using Python.

In this project, I built an Amazon Price Tracker that checks the price of a product and sends an email alert when the price falls below a preset target price.

I first practiced scraping the product price and title from a static practice webpage before adding request headers and the email notification functionality.

## Topics Covered

* Web scraping
* HTTP requests
* The `requests` library
* BeautifulSoup
* HTML parsing
* Finding HTML elements
* Extracting text from HTML
* String manipulation
* `split()`
* Type conversion with `float()`
* HTTP request headers
* User-Agent
* Accept-Language
* Environment variables
* `.env` files
* `python-dotenv`
* `os.getenv()`
* SMTP
* The `smtplib` library
* Sending emails with Python
* Conditional statements
* String formatting
* Character encoding
* Debugging

## What I Learned

I learned how Python can be used to monitor information from a webpage and automatically perform an action when a certain condition is met.

I used the `requests` library to retrieve the webpage and BeautifulSoup to parse the HTML.

I used BeautifulSoup's `find()` method to locate the HTML element containing the product price and converted the extracted price from a string into a floating-point number using `float()`.

I also learned how to scrape the product title and use it together with the current price and product URL in an email notification.

Another important concept I learned was HTTP request headers. I used `User-Agent` and `Accept-Language` headers and passed them into the `requests.get()` method so that additional information could be included with the request.

I also practiced using environment variables to keep sensitive information such as my email address and password outside of my Python source code.

I used `python-dotenv` and `os.getenv()` to load these values from a `.env` file.

Finally, I learned how to use Python's `smtplib` library to connect to Gmail's SMTP server and send an automated email when the product price was below my target price.

## Challenges

One challenge was understanding how to extract the numerical price from the text returned by BeautifulSoup.

I also had to understand how request headers work and remember that creating a `HEADERS` dictionary is not enough. The dictionary must actually be passed into the `requests.get()` function.

Another challenge was setting up the email functionality using SMTP and environment variables.

While testing the project, I encountered a `UnicodeEncodeError` when the product title contained a special character that could not be encoded using ASCII.

I had to investigate the traceback and modify the email message so that it could be sent successfully.

## Reflection

Day 47 was an important project because it combined several Python concepts I had learned throughout the course.

Instead of simply scraping information from a webpage, I used the scraped information to trigger an automated action.

This project also gave me more experience working with real-world problems such as HTTP headers, environment variables, SMTP authentication, and character encoding.

The debugging process was also valuable because it taught me to read the traceback carefully and identify exactly where an error occurs.

## Course Progress

* Completed Day 47 of Angela Yu's 100 Days of Code: Python Bootcamp
* Built an Amazon Price Tracker
* Practiced using `requests`
* Practiced using BeautifulSoup
* Learned how to extract and convert price data
* Learned how to use HTTP request headers
* Practiced using environment variables
* Learned how to send automated emails with SMTP
* Debugged a Unicode encoding error

## About Me

I am learning Python and web development while building my software development skills.

My goal is to become a strong software developer by consistently building projects, improving my problem-solving abilities, and gaining practical experience.
