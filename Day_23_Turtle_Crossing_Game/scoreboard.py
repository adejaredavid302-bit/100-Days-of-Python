from turtle import Turtle
FONT = ("Courier", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-200,250)
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.level}", align="left", font=FONT)
    def increase_level(self):
        self.score+=1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align="center", font=FONT)
