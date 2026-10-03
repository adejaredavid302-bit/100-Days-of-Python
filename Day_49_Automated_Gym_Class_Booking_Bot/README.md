# Day 49 – Automated Gym Class Booking Bot

## Overview

On Day 49 of Angela Yu’s 100 Days of Code, I built a resilient Selenium automation bot that logs into a gym website, finds eligible Tuesday and Thursday 6:00 PM classes, and automatically handles class bookings and waitlists.

The bot also checks whether a class has already been booked or waitlisted before taking any action. After processing the classes, it navigates to the My Bookings page to verify that the expected bookings were successfully recorded.

## Topics Covered

* Selenium WebDriver
* ChromeOptions
* Persistent Chrome user profiles
* Environment variables with `.env`
* Automated login
* WebDriverWait and Expected Conditions
* CSS selectors
* XPath ancestor navigation
* Finding and processing multiple elements
* Conditional logic
* Functions and reusable code
* Exception handling
* Retry logic
* Lambda functions
* Data structures with dictionaries and lists
* Automated verification
* Web automation workflows

## What I Learned

I learned how to build a more complete Selenium automation workflow instead of simply finding and clicking individual elements.

I practiced navigating through related elements using XPath, such as finding the day group containing a particular class card. I also learned how to inspect button text and use it to decide whether a class should be booked, skipped because it was already booked, or joined through the waitlist.

I also learned how to create reusable functions for different parts of an automation workflow and how to use a dictionary to keep track of booking statistics.

Another important lesson was building more resilient automation. I created a retry function that attempts an action multiple times when Selenium or browser-related errors occur.

Finally, I learned how to verify the result of an automation task by navigating to the My Bookings page and comparing the bookings found with the expected number.

## Challenges

One of the main challenges was working with the structure of the class cards and connecting the class time to the correct day group.

I also had to handle different button states such as `Booked`, `Waitlisted`, and available booking actions.

Another challenge was making the automation more reliable when browser or WebDriver errors occur. This led me to create a retry mechanism instead of allowing the entire program to immediately fail.

The final verification step also required navigating to another page and extracting booking information to confirm that the automation had worked correctly.

## Reflection

Day 49 was a major step forward in my Selenium learning. Instead of writing a simple script that performs one action, I built a complete automation pipeline with login, class filtering, decision-making, error handling, statistics, and verification.

This project helped me understand how real-world browser automation requires more than just locating elements. The program needs to make decisions based on the current state of the website and verify that the intended action actually happened.

## Course Progress

**Angela Yu – 100 Days of Code: The Complete Python Pro Bootcamp**

* Day 49 completed
* Current focus: Selenium and web automation
* Progress: 49 / 100 days

## About Me

I’m learning Python through Angela Yu’s 100 Days of Code challenge and documenting my progress by building projects along the way.

My goal is to develop strong programming fundamentals and gradually progress into AI engineering, machine learning, and real-world software projects.
