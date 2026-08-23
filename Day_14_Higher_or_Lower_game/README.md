# Day 14 – Higher Lower Game

## Overview

For Day 14 of the **100 Days of Code: The Complete Python Pro Bootcamp**, I built a **Higher Lower Game** inspired by the popular social media guessing game. The player is shown two accounts and must guess which one has more followers. The game continues until the player makes an incorrect guess.

This project focused heavily on **functions, dictionaries, boolean logic, loops, and game state management**.

---

## Features

* Randomly selects accounts from a dataset.
* Displays formatted account information.
* Accepts user guesses (`A` or `B`).
* Compares follower counts.
* Tracks the player's score.
* Carries the winning account into the next round.
* Ends the game when the player guesses incorrectly.

---

## Topics Covered

* Python functions
* Function parameters and return values
* Boolean expressions
* Dictionaries and nested data
* Random module
* While loops
* Game loops and state management
* Input handling
* String formatting with f-strings

---

## What I Learned

This project helped me understand several important programming concepts:

### Boolean-returning functions

I learned that a function can return `True` or `False` and that an `if` statement can directly use that result.

```python
def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'
```

### Separation of concerns

I separated the program into different functions:

* `format_data()` → handles display formatting.
* `check_answer()` → handles comparison logic.
* The main game loop → handles score updates and game flow.

### Game state management

The biggest lesson was understanding how the winning account becomes the next **A**:

```python
account_A = account_B
account_B = random.choice(data)
```

This keeps the winner in the game and introduces a new challenger each round.

---

## Challenges I Faced

* Understanding why `if is_correct:` works.
* Managing the game loop without creating infinite loops.
* Updating the correct account after each round.
* Preventing duplicate accounts from appearing as both A and B.
* Organizing the code into reusable functions.

---

## Final Outcome

The final version of the game includes:

* Clean function-based structure.
* Proper score tracking.
* Correct Higher Lower game mechanics.
* Improved readability and maintainability.

---

## Reflection

Day 14 was a major step forward in my Python journey. Earlier projects focused mostly on syntax, but this project required **actual problem-solving and program design**. I learned how to think about **state, flow, and function responsibilities**, which made the code much cleaner and easier to understand.

This is one of the first projects where I felt like I was building a complete application rather than just writing isolated Python exercises.

---

## Course Progress

* **Course:** 100 Days of Code: The Complete Python Pro Bootcamp
* **Day Completed:** Day 14
* **Project:** Higher Lower Game

---

## About Me

I am an aspiring **AI Engineer** currently learning Python through the **100 Days of Code** bootcamp. I am documenting each day of my learning journey on GitHub as I build a strong foundation in programming, software development, and artificial intelligence.
