# Day 28 – Project

## Overview

Day 28 focused on building a **Pomodoro Timer** using Python and Tkinter.

The Pomodoro Technique is a time-management method that divides work into focused study sessions followed by short breaks. In this project, I created a graphical timer that automatically switches between work sessions, short breaks, and longer breaks.

This project combined the Tkinter GUI concepts I learned on Day 27 with timers, functions, and program logic.

## Topics Covered

* Tkinter
* Graphical User Interfaces (GUI)
* Canvas
* Images in Tkinter
* Buttons
* Labels
* `after()`
* Functions
* Global variables
* Constants
* Timer countdowns
* String formatting
* Program state
* User interaction

## What I Learned

One of the most important things I learned was how to create a countdown timer using Tkinter.

I learned how to use the `after()` method to repeatedly call a function after a specific amount of time.

For example:

```python
window.after(1000, count_down)
```

The `1000` represents 1000 milliseconds, which is equal to one second.

I also learned how to use a Canvas widget to display elements such as text and images inside the GUI.

Another important concept was using variables to keep track of the number of completed work sessions.

The timer follows a specific sequence:

```text
Work → Short Break → Work → Short Break → Work → Short Break → Work → Long Break
```

I also learned how to use different timer lengths depending on the current session.

## Challenges

The main challenge was understanding how the countdown should continue every second without freezing the entire application.

I also had to understand how the `after()` method works and how it repeatedly calls the countdown function.

Another challenge was keeping track of which session the user was currently on and changing the timer appropriately between work periods and breaks.

Making the timer reset correctly when the reset button was pressed also required careful use of variables and functions.

## Reflection

Day 28 was a major improvement from Day 27 because I was able to combine several Tkinter concepts into a more interactive application.

I learned that building a GUI application is not only about creating buttons and labels. I also need to think about how the program behaves over time and how different functions interact with each other.

The Pomodoro Timer helped me understand how timers, GUI elements, functions, and program logic can work together to create a useful application.

## Course Progress

I am continuing through Angela Yu's **100 Days of Code: The Complete Python Pro Bootcamp**.

Day 28 helped me strengthen my understanding of Tkinter while introducing timers and more advanced GUI programming concepts.

## About Me

I am learning Python with the goal of developing strong programming, software development, and AI engineering skills.

I am documenting my progress through the 100 Days of Code challenge and uploading my projects to GitHub to track my growth and build my programming portfolio.
