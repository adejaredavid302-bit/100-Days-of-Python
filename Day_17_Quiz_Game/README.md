# Day 17 – The Quiz Project & Object-Oriented Programming (OOP)

## Overview

Day 17 focused on learning the fundamentals of **Object-Oriented Programming (OOP)** in Python by building a Quiz Game. This project introduced the concept of creating classes, instantiating objects, organizing code into multiple files, and allowing objects to communicate with one another.

The starter files provided by the course (`question_model.py`, `quiz_brain.py`, and `data.py`) were part of the course resources. My primary focus was understanding how these classes work together and how the main program controls the flow of the application.

---

## Topics Covered

- Object-Oriented Programming (OOP)
- Creating Classes
- Constructors (`__init__`)
- The `self` keyword
- Object Attributes
- Object Methods
- Creating Objects
- Importing Classes from Other Files
- Passing Objects Between Classes
- Working with Multiple Python Files
- Building a Quiz Game

---

## Project

**Quiz Game**

The application:
- Loads question data.
- Converts the data into `Question` objects.
- Stores all questions in a question bank.
- Uses the `QuizBrain` class to manage the quiz flow.
- Displays questions one at a time and prepares the structure for checking answers and tracking progress.

---

## What I Learned

- The difference between a **class** and an **object**.
- How the `__init__()` method initializes every new object.
- Why `self` refers to the current object being created or used.
- How attributes are created using `self.attribute`.
- How to access object attributes using the dot (`.`) notation.
- How objects created in one file can be passed into another class.
- How multiple Python files work together in one project.
- How starter classes provided by a library or project can be imported and used without rewriting them.

---

## Challenges

The biggest challenge was understanding Object-Oriented Programming.

I initially struggled with:
- The purpose of `self`.
- How constructors work.
- How attributes are stored inside objects.
- Why `QuizBrain` could access `current_question.text` without importing the `Question` class directly.
- How objects move between different files.

After breaking the code down line by line and understanding how the `Question` objects were created in `main.py` and passed into `QuizBrain`, the concepts became much clearer.

---

## Reflection

Day 17 was one of the most challenging days so far, but it also taught me one of the most important programming concepts. Understanding how classes and objects interact has given me a much stronger foundation for building larger Python applications.

---

## Course Progress

- **Course:** 100 Days of Code: The Complete Python Pro Bootcamp by Angela Yu
- **Day Completed:** 17 / 100
- **Project:** Quiz Game
- **Status:** ✅ Completed

---

## About Me

I'm documenting my progress through Angela Yu's **100 Days of Code** challenge while building a strong Python foundation for Artificial Intelligence and Machine Learning.

**GitHub:** *Add your GitHub profile link here.*