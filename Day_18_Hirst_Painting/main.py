from turtle import Turtle,Screen
import random
screen=Screen()
screen.colormode(255)
dav=Turtle()


color_list=[(253, 253, 252), (245, 252, 249), (252, 245, 249), (237, 245, 250), (218, 150, 106), (239, 102, 178),
            (154, 80, 47), (159, 56, 92), (114, 174, 213),
     (240, 225, 99)]
dav.speed("fastest")
dav.penup()
dav.setheading(225)
dav.forward(250)
dav.setheading(0)
number_of_dots=100
dav.hideturtle()
for dot_count in range(1,number_of_dots+1):
    dav.dot(20,random.choice(color_list))
    dav.forward(50)

    if dot_count%10==0:
        dav.setheading(90)
        dav.forward(50)
        dav.setheading(180)
        dav.forward(500)
        dav.setheading(0)
screen.exitonclick()




