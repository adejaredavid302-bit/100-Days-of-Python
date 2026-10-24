# Day 59 — Blog Website Upgrade with Bootstrap

## Overview
On Day 59 of the **100 Days of Code: The Complete Python Pro Bootcamp**, I continued upgrading my Flask blog website using Bootstrap and Jinja templating. The project focuses on reusing HTML components and fetching blog post data from an API instead of writing every post manually.

##  Features
- Responsive blog layout using Bootstrap.
- Reusable navigation bar and footer with Jinja includes.
- Separate Home, About, Contact, and blog post pages.
- Flask routes for navigating between pages.
- Background images and static assets served through Flask.
- Blog posts retrieved from an npoint JSON API.
- Dynamic rendering of post titles, subtitles, authors, and dates using Jinja templates.

##  Technologies Used
- Python
- Flask
- HTML5
- CSS3
- Bootstrap
- Jinja2
- JSON and REST API concepts

##  Project Structure
```text
Day_59/
├── main.py
├── templates/
│   ├── header.html
│   ├── footer.html
│   ├── index.html
│   ├── post.html
│   ├── about.html
│   └── contact.html
└── static/
    └── assets/
        ├── css/
        ├── js/
        └── img/
```

##  What I Learned
- How to reuse HTML components with Jinja `{% include %}`.
- How Flask routes connect URLs to HTML templates.
- How to generate navigation links using Flask's `url_for()`.
- How to organize and serve CSS, JavaScript, and image assets.
- How JSON APIs can provide data to a Flask application.
- How Jinja variables and loops can display dynamic content.

##  Challenges
- Fixing static file paths for CSS and background images.
- Removing duplicate navigation bars after introducing reusable templates.
- Connecting navigation links to the correct Flask routes.
- Preparing the blog to display posts dynamically from an API.

##  Reflection
Day 59 helped me understand how to make a Flask website more maintainable by reusing templates and separating content from presentation. It also introduced the idea of fetching external data and displaying it dynamically instead of hardcoding everything into HTML.

##  Course Progress
**100 Days of Code: Day 59**

Continuing to build my Python foundation and develop practical web application skills as part of my journey toward becoming an AI engineer.
