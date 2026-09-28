# Day 48 – Cookie Clicker Bot

## Overview

On Day 48 of the 100 Days of Code: Python course, I built a Cookie Clicker Bot using Selenium. The program automates the Cookie Clicker game by clicking the big cookie, monitoring the available cookies, and purchasing affordable upgrades from the store.

The bot is designed to run for five minutes, check the store every five seconds, purchase the most expensive affordable upgrade, and display the final cookies-per-second (CPS).

## Topics Covered

* Browser automation with Selenium
* Finding web elements using IDs, class names, and CSS selectors
* Using `find_element()` and `find_elements()`
* Clicking web elements
* Using `WebDriverWait` and expected conditions
* Loops and conditional statements
* Working with `time()` and `sleep()`
* Extracting text using `.text`
* String manipulation with `.split()` and `.replace()`
* Converting strings to integers using `int()`
* Reversing elements using `reversed()`
* Exception handling with `try` and `except`
* Working with dynamic webpages
* Git and GitHub

## What I Learned

* How to automate browser interactions using Selenium.
* How to locate and click elements on a webpage using different selectors.
* How to use `WebDriverWait` and expected conditions to wait for elements to become clickable.
* How to use `find_elements()` to locate multiple products on a webpage.
* How to extract cookie counts and upgrade prices from webpage elements.
* How to use `time()` to create a five-minute stopping condition and schedule periodic store checks.
* How to use `reversed()` to inspect store products in reverse order.
* How to compare upgrade prices with the available cookie balance.
* How to use `try` and `except` to handle errors when locating elements or converting values.
* How to automate repetitive clicking and purchasing tasks with Python.

## Challenges

One of the main challenges was identifying the correct HTML elements on the Cookie Clicker webpage and understanding how to select them using Selenium.

I also had to troubleshoot the language-selection element and learn that clickable webpage elements are not necessarily HTML `<button>` elements.

Another challenge was locating the store products, accessing their prices, and determining which upgrades were enabled and affordable.

Implementing the five-minute timer and scheduling store checks every five seconds also required careful use of `time()` and conditional statements.

## Reflection

Day 48 helped me gain practical experience with Selenium and browser automation. I learned how to interact with webpage elements, retrieve information from a dynamic webpage, and automate repetitive tasks.

The project also improved my understanding of CSS selectors, loops, conditional statements, exception handling, and time-based execution.

One important lesson was the value of inspecting webpage elements and troubleshooting errors instead of relying only on assumptions about how a website is structured.

## Course Progress

Day 48 of 100 Days of Code: Python

## About Me

I am currently learning Python and building projects through Angela Yu's 100 Days of Code course as part of my journey toward becoming an AI engineer.

