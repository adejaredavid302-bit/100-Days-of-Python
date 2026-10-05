# Day 50 – TinDog Automation Bot

## Overview

On Day 50, I built a Selenium automation bot for the TinDog practice website. The project automates the login process, handles multiple browser windows, interacts with the TinDog interface, reads each dog's distance, and decides whether to swipe right or left based on the distance.

## Topics Covered

* Selenium WebDriver
* ChromeOptions
* WebDriverWait
* Expected Conditions
* CSS selectors
* Browser window handles
* Switching between browser windows
* Form interaction with `send_keys()`
* Clicking web elements
* Exception handling
* `try` / `except`
* Infinite `while` loops
* String cleaning with `replace()` and `strip()`
* Converting strings to integers with `int()`
* Conditional logic
* Automating repeated browser actions

## What I Learned

I learned how Selenium can interact with a dynamic website and perform actions based on information it reads from the page.

I practiced using `WebDriverWait` with expected conditions instead of relying only on fixed delays. I also learned how to save the current browser window handle and switch between the main TinDog window and the login window.

Another important part of the project was extracting text from the webpage, cleaning it, converting it into an integer, and using that value to make a decision.

I also learned how to handle common Selenium problems such as missing elements, intercepted clicks, and timeouts using exception handling.

## Challenges

One of the main challenges was understanding how multiple browser windows work and how to switch back to the original TinDog window after logging in.

Another challenge was dealing with the distance text returned by the webpage. I had to remove `"km"` and `"away"` before converting the remaining text into an integer.

Handling dynamic webpage behavior was also challenging because elements may not always be immediately available or clickable.

## Reflection

Day 50 helped me understand Selenium beyond simply finding and clicking elements. I learned how to make the automation interact with information on a webpage and make decisions based on that information.

The project also gave me more practice connecting different Selenium concepts together, especially waiting for elements, switching windows, handling exceptions, and repeatedly interacting with changing webpage content.

## Course Progress

**100 Days of Code – Python**

Day 50 completed.

## About Me

I am learning Python and building practical projects through the 100 Days of Code challenge. My goal is to strengthen my programming fundamentals and develop the skills needed to eventually work in AI engineering.

I am documenting my progress one project at a time and focusing on understanding the code rather than simply copying solutions.
