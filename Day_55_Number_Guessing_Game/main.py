from flask import Flask
import random
random_num=random.randint(0,9)
app = Flask(__name__)
@app.route('/')
def number_start():
    return """ 
    <h1 >Guess a number between 0 and 9</h1>
    <img src="https://giphy.com/gifs/reaction-thinking-lara-croft-D94a6xlwwsujwzUQGd">
    
    """
@app.route('/<int:number>')
def guess_number(number):
    if number==random_num:
        return (f"{number}"
                f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")
    elif number>random_num:
        return (f"Number is higher than the number {number}"
                f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
    elif number<random_num:
        return (f"Number is lower than the number {number}"
                f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")

if __name__ == '__main__':
    app.run(debug=True)



