# Day 57 — Blog Capstone Project (Part 1: Templating)

## Overview
For Day 57 of the 100 Days of Code: Python Bootcamp, I built a blog website using Flask, HTML, CSS, and Jinja templating.

The website fetches blog posts from an API and displays their titles and subtitles on the homepage. Each post has a Read link that opens a separate page containing the full article.

## Features
- Displays blog posts dynamically from an API
- Shows each post's title and subtitle on the homepage
- Provides a Read link for every blog post
- Displays the full title, subtitle, and body on individual post pages
- Uses dynamic URL routes to identify blog posts
- Applies CSS styling to the homepage and article pages

## Technologies Used
- Python
- Flask
- HTML5
- CSS3
- Jinja Templating
- Requests
- n:point API

## Project Structure
```text
Day_57_Blog_Capstone/
├── main.py
├── templates/
│   ├── index.html
│   └── post.html
└── static/
    └── css/
        └── style.css
```

## How It Works
- `main.py` creates the Flask application and defines the website routes.
- The homepage route fetches blog posts from the n:point API and passes them to the HTML template.
- `index.html` uses a Jinja loop to display each blog post's title, subtitle, and Read link.
- The `/post/<blog_id>` route identifies the selected post and renders its full content.
- `post.html` displays the selected post's title, subtitle, and body.
- `style.css` controls the website's layout, colors, typography, and responsive appearance.

## What I Learned
- Fetching data from an API using Requests
- Working with JSON data in Python
- Passing Python data into HTML templates
- Using Jinja loops to render dynamic content
- Creating dynamic Flask routes with URL parameters
- Connecting multiple pages through links
- Separating HTML templates from CSS styling

## Challenges
One important part of this project was connecting the API data to the HTML templates and ensuring that each Read link opened the correct blog post.

## Reflection
This project helped me understand how Flask, APIs, and Jinja templating work together to build dynamic websites. I also practised handling external data and displaying it across multiple pages.

## Day 57 Completed
