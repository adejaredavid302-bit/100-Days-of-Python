# Day 26 – List Comprehension & Python Sequences

## Overview

Day 26 focused on making Python code shorter and cleaner using list comprehension.

I learned how to work with Python sequences and how to create new lists from existing lists using a simple one-line syntax.

## Topics Covered

* List comprehension
* Python lists
* Using `for` loops with list comprehension
* Using conditions with list comprehension
* Working with ranges
* Python sequences
* Strings
* Lists
* Tuples
* Basic data processing

## What I Learned

I learned that list comprehension can be used to create a new list from an existing sequence.

A normal loop can look like:

```python
numbers = [1, 2, 3, 4, 5]

new_numbers = []

for number in numbers:
    new_numbers.append(number * 2)
```

The same thing can be written using list comprehension:

```python
new_numbers = [number * 2 for number in numbers]
```

I also learned that conditions can be added:

```python
new_numbers = [number for number in numbers if number > 2]
```

This makes the code shorter while still being readable.

## Projects

During Day 26, I practiced using list comprehension and sequence operations through different exercises and challenges.

These exercises helped me understand how to create, filter, and modify lists more efficiently.

## Challenges

The main challenge was understanding the order of the parts inside a list comprehension.

I had to understand how the `for` part and the `if` condition work together to create the new list.

## Reflection

Day 26 helped me write Python code in a shorter and cleaner way.

I now understand how list comprehension can replace many simple `for` loops and how conditions can be used to filter data.

## Course Progress

**Day 26 of 100 Days of Code – Completed**

## About Me

I am currently learning Python and building my programming skills through the 100 Days of Code challenge.

My long-term goal is to develop strong programming and problem-solving skills and eventually move into AI and machine learning.
