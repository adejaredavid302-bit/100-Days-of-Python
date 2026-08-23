from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head=self.segment[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            dav = Turtle("square")
            dav.color("white")
            dav.penup()
            dav.goto(position)
            self.segment.append(dav)

    def move_snake(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head[0].heading() != DOWN:
            self.head[0].seth(UP)
    def down(self):
        if self.head[0].heading() != UP:
            self.head[0].seth(DOWN)
    def left(self):
        if self.head[0].heading() != RIGHT:
            self.head[0].seth(LEFT)
    def right(self):
        if self.head[0].heading() != LEFT:
            self.head[0].seth(RIGHT)



