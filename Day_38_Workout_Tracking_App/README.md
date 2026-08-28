# Day 38 – Workout Tracking App

## Overview

Today, I built a **Workout Tracking App** that uses APIs to analyze the exercise I enter and automatically records the workout information in a Google Sheet through Sheety.

The program asks me what exercise I did, sends that information to the Nutritionix exercise API, and receives details such as the exercise duration and estimated calories burned. It then sends that information to my Sheety API, which adds the workout to my spreadsheet.

This project helped me understand how multiple APIs can work together in one Python application.

## Topics Covered

* Environment variables with `python-dotenv`
* Working with `.env` files
* Using `os.getenv()`
* Making POST requests with the `requests` library
* Sending JSON data to an API
* HTTP request headers
* Reading JSON responses
* Working with nested dictionaries
* Using `datetime`
* Formatting dates and times with `strftime()`
* Getting user input with `input()`
* Nutritionix Exercise API
* Sheety API
* Bearer token authentication
* Connecting Python to Google Sheets
* Automating data entry
* Combining multiple APIs in one project

## What I Learned

I learned how to use environment variables to keep API credentials outside my Python source code. I loaded my `.env` file using `load_dotenv()` and retrieved my credentials with `os.getenv()`.

I also learned how to send a POST request using `requests.post()` and provide information through JSON:

```python
response = requests.post(url, headers=headers, json=data)
```

The Nutritionix API takes information such as gender, weight, height, age, and the exercise I entered. It then returns information about the exercise.

I learned how to access specific information from the API response:

```python
user_data = result["exercises"][0]
duration = user_data["duration_min"]
calories = user_data["nf_calories"]
```

I also learned how to work with Sheety to send the workout information to a spreadsheet. I created a dictionary containing the date, time, exercise, duration, and calories and sent it using another POST request.

Finally, I learned how Bearer token authentication works with API requests:

```python
sheety_headers = {
    "Authorization": f"Bearer {sheety_token}"
}
```

## Challenges

One of the main challenges was understanding how to connect multiple APIs together.

The program does not simply make one API request. It first sends my exercise information to the Nutritionix API, receives the calculated workout information, and then uses that information to make another request to Sheety.

I also had to understand the structure of the JSON response so that I could correctly extract the exercise duration and calories.

Another important challenge was handling API credentials securely instead of placing them directly inside the Python code.

## Reflection

Day 38 was a major step forward because I started building applications that communicate with multiple external services.

Instead of only writing Python programs that work locally, I am now creating programs that can send and receive real data from APIs and automatically store that data somewhere else.

This project also showed me how useful APIs are when building real-world applications. Python can act as the connection between different services, allowing information to move automatically from one system to another.

## Course Progress

I am continuing through Angela Yu's **100 Days of Code: The Complete Python Pro Bootcamp**.

Day 38 focused on working with APIs and building a workout tracking application using Python, Nutritionix, and Sheety.

My progress is continuing toward becoming more comfortable with Python, APIs, automation, and backend-style projects.

## About Me

I am learning Python through the 100 Days of Code challenge and building projects to strengthen my programming skills.

My goal is to become a strong programmer and eventually work toward **AI Engineering**, while also developing practical skills in APIs, automation, backend development, and software engineering.

Each project is helping me move from simply learning Python syntax to building applications that interact with real-world services.
