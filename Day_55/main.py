from flask import Flask
app = Flask(__name__)
def make_bold(func):
    def wrapper():
        return f"<b>{func}</b>"
    return wrapper
def make_emphasis(func):
    def wrapper():
        return f"<em>{func}</em>"
    return wrapper
def make_underline(func):
    def wrapper():
        return f"<u>{func}</u>"
    return wrapper


@app.route("/")
@make_bold
def hello_world():
    return "Hello World"

@app.route("/bye")
def bye():
    return "Bye!"
@app.route("/username/<name>")
def greeting(name):
    return f"Hello World {name}"

if __name__ == "__main__":
    app.run(debug=True)


