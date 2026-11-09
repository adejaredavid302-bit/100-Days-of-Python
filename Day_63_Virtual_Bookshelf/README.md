# Day 63 – Virtual Bookshelf

## Project Overview

For Day 63 of the 100 Days of Code: The Complete Python Pro Bootcamp, I built a **Virtual Bookshelf** using Flask, Flask-SQLAlchemy, and SQLite.

The project allows users to manage a personal book collection by adding books, viewing saved books, updating their ratings, and deleting books.

## What I Built

- A homepage displaying all books in the collection.
- A form for adding new books.
- An edit feature for updating book ratings.
- A delete feature for removing books.
- A SQLite database for storing book information.

## Concepts Practised

- Flask routing and HTTP methods (GET and POST).
- Flask-SQLAlchemy.
- SQLite database integration.
- Creating database models.
- SQLAlchemy ORM.
- Database relationships between Python classes and database tables.
- Adding, querying, updating, and deleting database records (CRUD).
- Using `db.session.add()`, `db.session.commit()`, and `db.session.delete()`.
- Retrieving database records with `db.select()` and `.scalars().all()`.
- Using `db.get_or_404()` to retrieve records or return a 404 error.
- Dynamic HTML templates with Jinja2.
- Handling HTML form submissions.

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- SQLite
- HTML
- Jinja2

## How It Works

1. The homepage retrieves and displays all books stored in the database.
2. Users can navigate to the Add Book page and submit a book's title, author, and rating.
3. The submitted information is saved to the SQLite database.
4. Users can edit a book's rating.
5. Users can delete books from their collection.
6. The homepage updates to reflect changes in the database.

## What I Learned

This project helped me understand how to connect a Flask application to a database using Flask-SQLAlchemy.

I also learned how to use SQLAlchemy models to represent database tables and perform CRUD operations without writing raw SQL queries for every database operation.

**Day 63 completed.**