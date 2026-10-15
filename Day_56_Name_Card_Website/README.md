# Day 56 – Name Card Website

## Overview
Built a sleek, modern personal digital name card website using Flask. The application serves a fully styled, responsive landing page that introduces myself, showcases my career path, and provides quick navigation links to my professional profiles.

## Topics Covered
- Flask server initialization
- Serving static assets in Flask
- Integrating HTML templates with Flask
- Advanced CSS styling (Gradients, Flexbox/Grid layouts, and borders)
- Flask template tags (`url_for`)
- Cross-origin security attributes (`target="_blank"`, `rel="noopener noreferrer"`)

## What I Learned
- How to structure a Flask project using separate `templates` and `static` folders.
- How to dynamically link CSS stylesheets to HTML templates using `url_for('static', filename='...')`.
- How to utilize modern CSS properties like `radial-gradient` and `linear-gradient` to create a beautiful glowing background.
- How to apply fluid layouts using `min(100%, 540px)` for perfect responsiveness on both mobile and desktop screens.
- How to style aesthetic pill buttons and circular text icons for an interactive user interface.

## Challenges
- Troubleshooting broken CSS paths caused by incorrect directory routing inside the Flask template syntax.
- Clearing browser cache to force immediate layout updates during development.
- Aligning and spacing multiple elements neatly inside a centralized card structure.

## Reflection
This challenge shifted my focus from purely programmatic web logic to visual design and front-end engineering. Understanding how Flask handles static assets is a foundational step toward building production-ready web applications that look as good as they function.

## Course Progress
Day 56 of Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp.
