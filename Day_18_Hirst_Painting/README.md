# Day 18 – Turtle Graphics & Hirst Painting Project

## Overview

Day 18 introduced Python's **Turtle Graphics** module, where I learned how to create drawings using a turtle object. The main project for this day was recreating a simplified version of **Damien Hirst's Spot Painting** by generating a 10×10 grid of colored dots.

I also learned how to extract colors from an image using the **colorgram** library and use RGB color values with Turtle.

---

## Topics Covered

* Turtle Graphics
* Turtle Objects
* Screen Object
* RGB Colors
* `screen.colormode(255)`
* Random Module
* Drawing with `dot()`
* Turtle Movement
* `setheading()`
* `penup()`
* Nested Logic
* Loops
* Color Lists

---

## What I Learned

* How to create and control Turtle objects.
* How to use the Screen object.
* How Turtle uses methods such as:
  - `forward()`
  - `dot()`
  - `penup()`
  - `setheading()`
  - `hideturtle()`
* How RGB colors work in Turtle.
* Why `screen.colormode(255)` is necessary when using RGB values from 0–255.
* How to generate random colors using `random.choice()`.
* How to use loops to draw repetitive patterns.
* How to reposition the turtle after every 10 dots to create a grid.
* How to extract colors from an image using the **colorgram** package.

---

## Project

### Hirst Painting Generator

This project recreates a simplified version of Damien Hirst's famous dot paintings by drawing a 10×10 grid of randomly colored dots using Turtle Graphics.

---

## Challenges

* Understanding why Turtle could not use RGB tuples until `screen.colormode(255)` was set.
* Learning how Turtle coordinates and headings work.
* Positioning the turtle correctly before drawing.
* Resetting the turtle's position after every row.

---

## Reflection

Day 18 was my first experience creating graphical programs with Python. Although my long-term goal is AI Engineering, this project strengthened my understanding of objects, methods, loops, coordinates, and problem-solving through visual programming.

---

## Course Progress

* **Course:** 100 Days of Code – The Complete Python Pro Bootcamp
* **Day Completed:** 18 / 100

---

## Technologies Used

* Python
* Turtle Graphics
* colorgram.py
* random

---

## About Me

I am currently learning Python through Angela Yu's **100 Days of Code** course while preparing for a career in **Artificial Intelligence Engineering**. I upload each day's project to GitHub to document my progress and continuously improve my programming skills.