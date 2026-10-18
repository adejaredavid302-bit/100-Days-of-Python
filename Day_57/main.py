from flask import Flask, render_template
import requests

app = Flask(__name__)
BLOG_API_URL = "https://api.npoint.io/c790b4d5cab58020d391"

@app.route("/")
def home():
    response = requests.get(BLOG_API_URL)
    response.raise_for_status()
    posts = response.json()
    return render_template("index.html", posts=posts)

@app.route("/post/<int:blog_id>")
def show_post(blog_id):
    response = requests.get(BLOG_API_URL)
    response.raise_for_status()
    posts = response.json()

    for post in posts:
        if post.get("id") == blog_id:
            return render_template("post.html", post=post)

    return "Blog post not found", 404

if __name__ == "__main__":
    app.run(debug=True)
