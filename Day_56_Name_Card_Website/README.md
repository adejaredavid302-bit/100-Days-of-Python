# Day 56 — Name Card Website

## Overview
For Day 56 of the 100 Days of Code: Python Bootcamp, I built a personal name card website using Flask, HTML, and CSS.

The website displays my name, learning journey, short bio, and social media links in a clean, dark-themed design.

## Features
- Personal name card layout
- Dark gradient background
- Custom initials avatar
- Personal introduction and bio
- GitHub, LinkedIn, and X links
- Responsive styling for smaller screens
- Flask route to render the HTML template

## Technologies Used
- Python
- Flask
- HTML5
- CSS3

## Project Structure
```text
Day_56/
├── main.py
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── images/
```

## How It Works
- `main.py` creates the Flask application and defines the homepage route.
- `templates/index.html` contains the structure and content of the name card.
- `static/css/style.css` controls the website's appearance, including its background, card layout, typography, colors, and links.
- Flask's `render_template()` function loads the HTML template when the homepage is visited.

## What I Learned
- Creating a basic Flask application
- Defining routes with `@app.route()`
- Rendering HTML templates with `render_template()`
- Connecting CSS files to HTML using Flask's `url_for()`
- Organising templates and static files in a Flask project
- Styling a responsive webpage with CSS

## Challenges
One challenge was connecting the CSS file correctly. I learned that the file path used in `url_for()` must match the actual location of the stylesheet inside the `static` folder.

## Reflection
This project helped me understand how Flask, HTML, and CSS work together to create a functional website. It was also an opportunity to practise organising a Flask project and customising a webpage.

## Day 56 Completed
