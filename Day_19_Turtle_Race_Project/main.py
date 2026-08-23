from turtle import Turtle,Screen
import random
is_race_on = False
screen=Screen()
screen.setup(width=800,height=600)
user_bet= screen.textinput(title="Make your bet",prompt="Which turtle will win the race?")
colors=["red","yellow","green","blue","purple"]
y_position=[-100,-60,-20,20,60]
all_turtles=[]

for turtle_index in range(0,5):
        dav = Turtle(shape="turtle")
        dav.penup()
        dav.goto(-300, y_position[turtle_index])
        dav.color(colors[turtle_index])
        all_turtles.append(dav)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 350:
            is_race_on = False
            winning_color=turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! the {winning_color} turtle is the winner!")
            else:
                print(f"You lose! the {winning_color} turtle is the winner")

        random_number = random.randint(0,10)
        turtle.forward(random_number)

screen.exitonclick()


