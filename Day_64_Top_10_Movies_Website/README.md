# Day 64 – Top 10 Movies Website

## Project Overview

For Day 64 of the 100 Days of Code: The Complete Python Pro Bootcamp, I built a **Top 10 Movies Website** using Flask, Flask-SQLAlchemy, Flask-WTF, and The Movie Database (TMDB) API.

The application allows users to search for movies, add them to a personal collection, rate movies, write reviews, and automatically rank movies based on their ratings.

## What I Built

- A homepage displaying movies ranked by their ratings.
- A movie search feature using the TMDB API.
- A movie selection page showing search results.
- A feature for adding selected movies to the database.
- A movie rating and review form.
- A delete feature for removing movies.
- Automatic movie ranking based on ratings.
- A SQLite database for storing movie information.

## Concepts Practised

- Flask routing and HTTP methods.
- Flask-SQLAlchemy and SQLAlchemy ORM.
- Database models and CRUD operations.
- Flask-WTF form handling.
- WTForms fields and validators.
- Bootstrap 5 integration.
- Working with external APIs using the Requests library.
- Sending API requests and handling JSON responses.
- Querying and sorting database records.
- Dynamic ranking using Python loops.
- Jinja2 templates.
- URL parameters and redirects.
- Updating and deleting database records.

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- SQLAlchemy
- WTForms
- Bootstrap 5
- SQLite
- TMDB API
- Requests
- HTML
- Jinja2

## How It Works

1. The homepage displays movies stored in the database, sorted by rating.
2. Users can search for a movie by entering its title.
3. The application retrieves matching movies from the TMDB API.
4. Users select a movie to add to their collection.
5. Movie details are saved to the SQLite database.
6. Users can rate movies and write reviews.
7. Movie rankings are automatically updated based on ratings.
8. Users can delete movies from their collection.

## What I Learned

This project helped me understand how to integrate external APIs into Flask applications and combine API data with a database.

I also gained more experience working with Flask-WTF forms, validating user input, querying database records, and building dynamic web applications.

**Day 64 completed.**