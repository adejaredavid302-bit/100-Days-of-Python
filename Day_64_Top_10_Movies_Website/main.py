from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(250))
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String(250))
    img_url: Mapped[str] = mapped_column(String(250))


class RateMovieForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


with app.app_context():
    db.create_all()
    if not db.session.execute(db.select(Movie).where(Movie.title == "Phone Booth")).scalar():
        new_movie = Movie(
            title="Phone Booth",
            year=2002,
            description="Publicist Stuart Shepard finds himself trapped in a phone booth...",
            rating=7.3,
            ranking=10,
            review="My favourite character was the caller.",
            img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        )
        db.session.add(new_movie)
        db.session.commit()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
    all_movies = result.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = i + 1
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)

    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie, form=form)




TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_MOVIE_DETAILS_URL = "https://api.themoviedb.org/3/movie"


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        query = form.title.data
        response = requests.get(
            TMDB_SEARCH_URL,
            params={"api_key": TMDB_API_KEY, "query": query}
        )
        data = response.json().get("results")
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)
@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))
@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_url = f"{TMDB_MOVIE_DETAILS_URL}/{movie_api_id}"
        response = requests.get(movie_url, params={"api_key": TMDB_API_KEY, "language": "en-US"})
        data = response.json()

        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0] if data.get("release_date") else 0,
            description=data["overview"],
            rating=0.0,
            ranking=0,
            review="",
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}" if data.get("poster_path") else ""
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))
if __name__ == '__main__':
    app.run(debug=True)