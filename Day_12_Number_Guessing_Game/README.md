# Day 12 – Number Guessing Game

## Overview

This project is a command-line Number Guessing Game built with Python. The computer randomly selects a number between 1 and 100, and the player must guess the correct number within a limited number of attempts based on the selected difficulty level.

The project reinforces the use of functions, loops, conditionals, and program organization by separating different responsibilities into reusable functions.

## Topics Covered

* Functions and function calls
* Parameters and return values
* Random number generation
* Constants
* While loops
* Conditional statements (`if`, `elif`, `else`)
* User input
* Game logic and flow control
* Code organization

## What I Learned

* How to generate random numbers using the `random` module.
* How to separate different parts of a program into dedicated functions.
* How to use constants to manage configuration values such as difficulty levels.
* How to return values from functions to update the game state.
* How to reduce duplicate code by reusing functions.
* How to build a game loop that continues until the player wins or runs out of attempts.
* How to organize a complete program into smaller, manageable components.

## Project Features

* Random number generation between 1 and 100.
* Easy and Hard difficulty levels.
* Limited number of attempts based on difficulty.
* Feedback after each guess ("Too High", "Too Low", or "Correct").
* Automatic game over when attempts reach zero.
* Displays the correct answer when the player loses.

## Challenges

One of the biggest challenges was deciding how to structure the game without repeating code.

Initially, I created separate logic for Easy and Hard mode. Later, I learned that both modes shared the same game logic, with only the number of attempts changing. By creating separate functions like `set_difficulty()` and `check_answer()`, I was able to simplify the program and make it more organized.

Another important lesson was understanding how functions can return values that update variables in the main game loop.

## Reflection

This project helped me become more comfortable breaking a problem into smaller functions instead of writing everything in one large block of code.

I also gained a better understanding of how return values, loops, and conditionals work together to control the flow of a complete application.

Compared to previous projects, I spent more time thinking about code organization instead of only focusing on making the program work. This was an important step toward writing cleaner and more maintainable Python programs.

## Course Progress

Angela Yu – 100 Days of Code: The Complete Python Pro Bootcamp

Day 12 Completed ✅

Project: Number Guessing Game

## About Me

I am currently learning Python by building projects every day through the 100 Days of Code Bootcamp. My goal is to develop a strong programming foundation before moving into machine learning, deep learning, and artificial intelligence engineering.
