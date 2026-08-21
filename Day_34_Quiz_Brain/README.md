# Day 34 – Quiz Brain

## Overview

Day 34 was a modified version of the **Day 17 Quiz Project**.

In Day 17, I built a quiz game using Python and Turtle. On Day 34, I revisited the quiz project and improved its structure by creating a `QuizBrain` class to handle the main quiz logic.

The `QuizBrain` class is responsible for keeping track of the current question, displaying questions, checking answers, and keeping track of the user's score.

## Topics Covered

* Object-Oriented Programming (OOP)
* Classes and objects
* Constructors with `__init__()`
* Instance attributes
* Instance methods
* Lists and list indexing
* `self`
* `input()`
* Conditional statements
* String methods
* `.lower()`
* `len()`
* Score tracking
* Calling methods from other methods
* Working with objects and their attributes

## What I Learned

I learned how to take an existing project and improve its structure instead of always starting from scratch.

I created a `QuizBrain` class with attributes such as:

```python
self.question_number = 0
self.question_list = question_list
self.score = 0
```

These attributes allow the quiz to keep track of its state while the program is running.

I also learned how different methods inside the same class can work together. For example, `next_question()` gets the current question and then calls `check_answer()` to determine whether the user's answer is correct.

I also became more comfortable accessing attributes from other objects:

```python
current_question.text
current_question.answer
```

## Challenges

One challenge was understanding how the question number relates to the list index.

Python lists start counting from `0`, so the first question is at index `0`. I had to understand when to access the question and when to increase `question_number`.

Another challenge was understanding how the different methods inside `QuizBrain` work together to control the quiz.

## Reflection

Day 34 was useful because I returned to a project I had already built and improved it using concepts I had learned later in the course.

This showed me that learning to code is not only about creating new projects. It is also about being able to look at older code and restructure it using better programming techniques.

The Day 17 project introduced me to building a quiz, while Day 34 helped me understand how Object-Oriented Programming can be used to organize the same type of project more effectively.

## Course Progress

**Angela Yu – 100 Days of Code: Python**

**Day 34 completed.**

Day 34 revisited the Day 17 Quiz Project and introduced a more structured approach using a `QuizBrain` class.

## About Me

I am learning Python through Angela Yu's 100 Days of Code course and building projects to strengthen my programming fundamentals.

My goal is to continue improving from basic Python projects toward more advanced software and AI engineering projects.
