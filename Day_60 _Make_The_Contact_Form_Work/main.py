from flask import Flask, render_template,request
import requests
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
user=os.getenv("USER")
password=os.getenv("PASSWORD")
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)
@app.route("/form-entry", methods=["POST"])
def form_entry():
    if request.method == "POST":
        global name,email,phone,message
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        print(f"{name}, {email}, {phone}, {message}")
        return "<h1>Successfully sent your message”. </h1>"

message=(f"SUBJECT:\n\n"
         f"name={name}"
        f"email={email}"
        f"phone={phone}"
        f"email={message}"
         )
def send_mail():
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(user, password)
        server.sendmail(user,user,message)
        server.quit()
if __name__ == "__main__":
    app.run(debug=True, port=5001)
