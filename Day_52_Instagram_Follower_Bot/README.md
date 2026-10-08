# Day 52 – Instagram Follower Bot

## Overview

Day 52 focused on building an automated Instagram Follower Bot using Python and Selenium.

For this project, I used the Share-a-Naan mock service from the 100 Days of Python platform instead of the real Instagram website. The bot logs into the service, searches for a similar account, opens that account's followers list, scrolls through the follower modal to load more users, and then automatically follows the displayed followers.

The project brought together several Selenium concepts I have learned throughout the course, especially automated login, searching, scrolling, locating elements, and handling intercepted clicks.

## Topics Covered

* Python Classes and Objects
* Object-Oriented Programming
* Selenium WebDriver
* ChromeOptions
* Environment Variables with `python-dotenv`
* WebDriverWait
* Expected Conditions
* CSS Selectors
* Partial Link Text
* Keyboard actions with `Keys`
* JavaScript execution with Selenium
* Scrolling dynamic content
* Finding multiple elements
* Nested element searching
* Exception handling
* `ElementClickInterceptedException`
* Loops
* Automated browser interaction

## What I Learned

I learned how to structure another Selenium automation project using a Python class.

I practiced separating the automation into different methods for logging in, finding followers, and following users.

I also learned how to use environment variables for login credentials instead of placing sensitive information directly inside the Python code.

One of the most important parts of this project was learning how to work with dynamically generated follower lists. The bot scrolls the follower modal multiple times so that more followers can be loaded before attempting to follow them.

I also practiced finding elements inside another element, such as locating the follow button inside each individual follower row.

## Challenges

One of the main challenges was working with the dynamically loaded followers list.

The bot needed to scroll the follower modal repeatedly before collecting the follower elements.

Another challenge was handling cases where clicking the follow button was intercepted by another element. I used `ElementClickInterceptedException` to handle this situation and interact with the popup when necessary.

Finding the correct selectors for the search button, follower list, follower rows, and follow buttons was also an important part of the project.

## Reflection

Day 52 helped me understand that Selenium automation is not only about finding an element and clicking it.

The bot has to understand the structure of the webpage, wait for elements to become available, interact with dynamic content, scroll to generate more data, and handle situations where the browser prevents a click.

I am also becoming more comfortable organizing larger Selenium projects into classes and separate methods instead of putting everything into one block of code.

This project is another step forward in my Python and automation journey.

## Course Progress

100 Days of Code – Python
Day 52 completed.

## About Me

I am learning Python through Angela Yu's 100 Days of Code while building practical projects along the way.

My long-term goal is to become an AI engineer, and I am using these projects to strengthen my Python, automation, problem-solving, and software development skills.

One day at a time.
