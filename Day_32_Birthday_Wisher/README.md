# Day 32 – Automated Birthday Wisher

## Overview

On Day 32 of the 100 Days of Code Python course, I built an **Automated Birthday Wisher** using Python.

The program reads birthday information from a CSV file, checks whether someone has a birthday today, randomly selects one of several birthday letter templates, replaces the `[NAME]` placeholder with the person's name, and sends the personalized birthday message through Gmail using SMTP.

This project combined several concepts I had already learned, including dictionaries, file handling, CSV data, datetime, randomization, and email automation.

## Topics Covered

* Reading CSV files with Pandas
* Creating dictionaries with dictionary comprehensions
* Working with `datetime`
* Extracting the current month and day
* Checking dictionary keys
* Reading text files
* Using `open()` with file modes
* String replacement with `.replace()`
* Random number generation with `random.randint()`
* Sending emails with `smtplib`
* Using Gmail's SMTP server
* Using `with` statements for resource management
* Working with nested dictionaries
* Automating tasks with Python

## What I Learned

One of the most important things I learned today was how to use a CSV file to create a dictionary that can be searched using a `(month, day)` tuple.

```python
birthday_dict = {
    (row["month"], row["day"]): row.to_dict()
    for (index, row) in read_file.iterrows()
}
```

I also learned how to get today's month and day using the `datetime` module:

```python
date = datetime.datetime.now()
month = date.month
day = date.day
today = (month, day)
```

This allowed me to check whether today's date exists in my birthday dictionary:

```python
if today in birthday_dict:
```

I learned how to retrieve the birthday person's information from the dictionary:

```python
birthday_person = birthday_dict[today]
```

I also practiced reading text files and modifying their contents:

```python
with open(f"./letter_templates/letter_{random_letter}.txt", "r") as letter_file:
    content = letter_file.read()

birthday_letter = content.replace("[NAME]", birthday_person["name"])
```

Finally, I learned how Python can interact with an email server using `smtplib` to automatically send the personalized birthday message.

## Challenges

One of the challenges I faced was understanding how to correctly match today's date with the information stored in the CSV file.

I also had to understand the difference between reading and writing files. For the birthday templates, I only needed to read the existing template rather than overwrite it.

Another important lesson was understanding that `.write()` returns the number of characters written rather than the actual text. This helped me understand why the email should use the `birthday_letter` variable instead.

Working with dictionaries created from Pandas rows also helped me become more comfortable accessing nested data such as:

```python
birthday_person["name"]
birthday_person["email"]
```

## Reflection

Day 32 was a useful project because it showed me how Python can be used for real-world automation.

Instead of simply practicing individual Python concepts, I combined multiple concepts into one working program. The project also helped me understand how data from a CSV file can control an automated process.

The biggest takeaway for me was learning how different Python modules and concepts can work together to create something practical.

## Course Progress

**Day 32 of 100 Days of Code – Completed**

I am continuing to build my Python foundation by moving from individual programming concepts toward practical automation projects.

## About Me

I am learning Python as part of my journey toward becoming an AI Engineer.

My goal is to build a strong foundation in Python, data structures, algorithms, machine learning, deep learning, and AI development.

This project is another step toward becoming comfortable with using Python to solve real-world problems and automate repetitive tasks.
