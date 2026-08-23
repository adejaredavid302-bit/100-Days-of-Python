# Day 27 – Tkinter GUI & Mile to Km Converter

## Overview

Day 27 focused on creating graphical user interfaces (GUIs) in Python using Tkinter.

For the project, I created a Mile to Kilometer Converter that allows the user to enter a number of miles and calculate the equivalent distance in kilometers.

## Topics Covered

* Tkinter
* Creating windows with `Tk()`
* Labels
* Buttons
* Entry widgets
* Functions
* Button commands
* Getting input with `.get()`
* Changing widget text with `.config()`
* Using `.grid()` to position widgets
* Window configuration
* Basic GUI design

## What I Learned

I learned how to create a basic GUI application using Tkinter.

I learned how to create a window:

```python
window = Tk()
```

I learned how to create an Entry widget for user input:

```python
inp = Entry(width=10)
```

I also learned how to connect a button to a function:

```python
button = Button(text="Calculate", command=button_clicked)
```

I used `.get()` to retrieve the value entered by the user and `.config()` to update the result displayed on the screen.

## Project – Mile to Km Converter

The application allows the user to enter a distance in miles and convert it to kilometers.

The basic calculation used is:

```text
kilometers = miles × 1.6
```

The result is then displayed in the GUI.

## Challenges

One of the main challenges was understanding how the different Tkinter widgets work together.

I also learned the difference between creating a widget and placing it in the window using `.grid()`.

## Reflection

Day 27 was an important step because I moved from programs that mainly run in the console to creating a program with a graphical interface.

I also built the Mile to Km Converter myself using what I learned from the lesson.

## Course Progress

**Day 27 of 100 Days of Code – Completed**

## About Me

I am currently learning Python and building my programming skills through the 100 Days of Code challenge.

My long-term goal is to develop strong programming and problem-solving skills and eventually move into AI and machine learning.
