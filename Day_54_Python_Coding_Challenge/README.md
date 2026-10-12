# Day 54 – Python Coding Challenge

## Overview
This challenge focused on using a Python decorator to measure and display the execution time of functions.

## Topics Covered
- Python decorators
- Nested functions
- Function arguments with `*args` and `**kwargs`
- `time.time()`
- `return` statements
- Function attributes using `__name__`

## What I Learned
- How a decorator wraps an existing function.
- How the wrapper measures execution time before and after a function runs.
- How `func(*args, **kwargs)` forwards arguments to the original function.
- Why `return wrapper` is necessary to give back the wrapped function.
- How `func.__name__` identifies the original function being timed.

## Challenges
Understanding how the decorator receives a function, returns a wrapper, and executes the original function through that wrapper.

## Reflection
This challenge helped me understand how decorators can add functionality to existing functions without changing their original code. I also learned why flexible argument forwarding makes a decorator reusable.

## Course Progress
100 Days of Code: The Complete Python Pro Bootcamp — Day 54.


