# Day 15 – Coffee Machine

## Overview

For **Day 15** of the **100 Days of Code: The Complete Python Pro Bootcamp**, I built a **Coffee Machine** application that simulates the operation of a real coffee vending machine. The program manages available resources, processes coin payments, checks if there are sufficient ingredients to prepare a selected drink, updates inventory after each purchase, and generates reports of the machine's remaining resources.

This project introduced me to writing larger Python programs by organizing logic into multiple reusable functions and separating different responsibilities within the application.

---

## Features

* Displays a menu of available drinks.
* Checks if there are enough ingredients to prepare the selected drink.
* Processes coin input from the user.
* Calculates the total amount of money inserted.
* Verifies successful payment before serving the drink.
* Returns change when necessary.
* Deducts ingredients from available resources.
* Displays a report of remaining ingredients and profit.
* Continues running until the machine is turned off.

---

## Topics Covered

* Functions
* Function parameters and return values
* Nested dictionaries
* Global constants
* Conditional statements
* While loops
* Resource management
* Basic financial calculations
* Program decomposition
* Code organization

---

## What I Learned

### Breaking a Large Problem into Smaller Functions

Instead of placing all the logic inside one large block of code, I learned how to divide the program into smaller functions, each responsible for a specific task.

### Working with Nested Dictionaries

This project strengthened my understanding of accessing values stored inside nested dictionaries.

Example:

```python
MENU["espresso"]["ingredients"]["water"]
```

### Returning Values from Functions

I learned that functions should return data instead of relying heavily on global variables. This makes code easier to understand, test, and reuse.

### Managing Program State

The coffee machine constantly updates its available resources after every successful purchase, helping me understand how programs maintain and modify data while running.

---

## Challenges I Faced

* Understanding how to pass information between multiple functions.
* Avoiding unnecessary use of global variables.
* Accessing values from nested dictionaries.
* Organizing the program into logical sections.
* Managing resources after serving each drink.
* Following the flow of a larger project with many interconnected parts.

---

## Final Outcome

The completed Coffee Machine program can:

* Accept drink orders.
* Check ingredient availability.
* Process user payments.
* Calculate and return change.
* Update available resources.
* Keep running until the machine is switched off.

This project was my first experience building a program that closely resembles a real-world application.

---

## Reflection

Day 15 showed me that writing software is more than knowing Python syntax. The biggest lesson was learning how to organize code into smaller, reusable functions that work together to solve a larger problem.

This project improved my confidence in reading larger programs, understanding program flow, and designing solutions by dividing problems into manageable pieces.

---

## Course Progress

* **Course:** 100 Days of Code: The Complete Python Pro Bootcamp
* **Day Completed:** Day 15
* **Project:** Coffee Machine

---

## About Me

I am an aspiring **AI Engineer** currently learning Python through the **100 Days of Code** bootcamp. I am documenting each day's progress on GitHub as I build a strong foundation in programming, software engineering, and artificial intelligence.
