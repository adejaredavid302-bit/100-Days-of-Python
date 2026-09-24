# Day 45 – 100 Movies Web Scraping Project

## Overview

Day 45 focused on web scraping using Python.

In this project, I used the `requests` library to retrieve the HTML content of a webpage and BeautifulSoup to parse the HTML and extract movie titles.

The project collects the movie titles from Empire's list of the 100 greatest movies and saves the results into a text file in the correct ranking order.

## Topics Covered

* Web scraping
* HTTP requests
* The `requests` library
* BeautifulSoup
* HTML parsing
* Finding HTML elements
* CSS classes
* List comprehensions
* String manipulation
* List slicing
* File handling
* Writing data to a text file
* Character encoding with UTF-8

## What I Learned

I learned how Python can interact with webpages and extract useful information from HTML.

I used the `requests` library to send a request to a webpage and retrieve its HTML content.

I then used BeautifulSoup to parse the HTML and locate the `<h3>` elements containing the movie titles.

I also practiced using a list comprehension to extract the text from each HTML element.

Another important concept I learned was list slicing. I used:

`movies[::-1]`

to reverse the order of the movie titles.

Finally, I learned how to use Python's file-handling capabilities to save the scraped movie titles into a `movies.txt` file.

## Challenges

One challenge was understanding how HTML elements are identified when scraping a webpage.

I also had to understand how BeautifulSoup's `find_all()` method works with element names and CSS classes.

Another challenge was understanding why the movie list needed to be reversed before being saved to the text file.

## Reflection

Day 45 introduced me to web scraping, which is a different way of using Python compared to the previous projects I have built.

I learned that Python can retrieve information from webpages and transform that information into a useful format.

This project also helped me understand how libraries such as `requests` and BeautifulSoup can work together to automate the collection of information from websites.

## Course Progress

* Completed Day 45 of Angela Yu's 100 Days of Code: Python Bootcamp
* Built a 100 Movies Web Scraping Project
* Practiced using `requests`
* Practiced using BeautifulSoup
* Learned how to extract information from HTML
* Saved scraped data to a text file

## About Me

I am learning Python and web development while building my software development skills.

My goal is to become a strong software developer by consistently building projects, improving my problem-solving abilities, and gaining practical experience.
