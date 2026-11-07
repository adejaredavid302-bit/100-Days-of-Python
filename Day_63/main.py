from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
app = Flask(__name__)
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-book-collection.db'
db=SQLAlchemy(model_class=Base)
db.init_app(app)
class Book(db.Model):
    __tablename__ = 'books'
    id:Mapped[int]=mapped_column(db.Integer, primary_key=True)
    title:Mapped[str]=mapped_column(String(250),unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

with app.app_context():
    db.create_all()
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

print("Database and record created successfully using SQLAlchemy!")

all_books = []

@app.route('/')
def home():
    return render_template('index.html',books=all_books)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form.get("book_name")
        author = request.form.get("book_author")
        rating = request.form.get("rating")
        book = {
            "title": name,
            "author": author,
            "rating": rating
        }
        all_books.append(book)
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)
