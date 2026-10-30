# Day 60 – Make the Contact Form Work

## Overview
On Day 60 of the 100 Days of Code: The Complete Python Pro Bootcamp, I made the contact form on my Flask blog website functional. Instead of simply displaying a contact page, the website can now receive visitors' information and prepare an email containing their submitted details.

## Features
- Functional contact form.
- Collects the visitor's name, email address, phone number, and message.
- Handles form submissions using Flask POST requests.
- Displays a success message after submission.
- Sends contact-form information through Gmail SMTP using Python's `smtplib`.
- Loads email credentials from environment variables using `python-dotenv`.

## Technologies Used
- Python
- Flask
- HTML
- Bootstrap
- Jinja2
- Requests
- smtplib
- python-dotenv
- SMTP

## Project Structure
```text
Day_60_Make_The_Contact_Form_Work/
│
├── main.py
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   └── post.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── assets/
│
├── .env
└── .gitignore
```

## What I Learned
- How HTML forms submit information to a Flask application.
- How to handle POST requests using Flask.
- How to retrieve submitted form values using `request.form`.
- How to use Python's `smtplib` to send emails.
- How to establish a secure SMTP connection using `starttls()`.
- How to load sensitive credentials from environment variables.
- How to pass information between functions using parameters.

## Challenges
- Understanding how HTML form submissions connect to Flask routes.
- Retrieving individual form fields correctly.
- Understanding the difference between defining a function and calling it.
- Organising submitted information into an email message.
- Handling SMTP configuration and email credentials.

## Reflection
Day 60 helped me understand how the frontend and backend communicate through HTML forms and Flask. I also gained practical experience connecting a web application to an email service.

I'm gradually becoming more comfortable building functional web applications rather than just creating pages that look good.

## Progress
**Day 60/100 – Completed**

One day closer to becoming a better Python developer!