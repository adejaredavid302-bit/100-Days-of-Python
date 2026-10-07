# Day 51 – Internet Speed Twitter Bot

## Overview

Day 51 focused on building an automated Internet Speed Twitter Bot using Python and Selenium.

The project measures my actual internet download and upload speeds using Speedtest. It then compares those results against my promised internet speeds. If my connection is slower than what I am paying for, the bot automatically logs into the Twitter/X account and posts a complaint message to the internet provider.

This project combined Selenium automation, environment variables, web scraping, conditional logic, and automated social media interaction.

## Topics Covered

* Python Classes and Objects
* Object-Oriented Programming
* Selenium WebDriver
* ChromeOptions
* WebDriverWait
* Expected Conditions
* CSS Selectors
* Environment Variables with `python-dotenv`
* Automating Speedtest
* Extracting data from webpages
* Converting strings to floating-point numbers
* Conditional statements
* Automated Twitter/X login
* Automated post creation
* JavaScript execution through Selenium
* Exception-aware waiting and dynamic webpages

## What I Learned

I learned how to organize a Selenium automation project inside a Python class.

I practiced storing the browser, waits, and measured speed values as attributes of the `InternetSpeedTwitterBot` object.

I also learned how to use environment variables to keep login credentials outside of my Python code.

A major part of the project was learning how to wait for dynamic webpage elements before interacting with them. I used `WebDriverWait` and Expected Conditions to make the automation more reliable.

The project also taught me how to extract the download and upload speeds from Speedtest, convert the values to numbers, and use them in a condition to decide whether a complaint should be posted.

## Challenges

One of the main challenges was working with dynamic websites where elements and results do not appear immediately.

Handling the Speedtest cookie popup and waiting for the final download and upload results required careful use of Selenium waits.

Another challenge was automating the login and post creation process while making sure the correct elements were available before interacting with them.

## Reflection

Day 51 was another important step in understanding how Python can interact with real websites.

Instead of simply automating clicks, this project made the program collect information, make a decision based on that information, and then take an action.

The project connected several concepts I have learned throughout the course: Python classes, environment variables, Selenium, web elements, waits, conditions, and automation.

It feels good to see how far I have come since the beginning of the course. Each project is becoming more practical and closer to the kind of automation and software engineering work I want to build in the future.

## Course Progress

100 Days of Code – Python
Day 51 completed.

## About Me

I am learning Python through Angela Yu's 100 Days of Code while building practical projects along the way.

My long-term goal is to become an AI engineer, and I am using these projects to strengthen my Python, automation, problem-solving, and software development skills.

One day at a time.
