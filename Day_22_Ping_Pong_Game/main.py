from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

scoreboard=Scoreboard()
ball = Ball()


right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up,"W")
screen.onkey(left_paddle.down,"S")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset_ball()
        scoreboard.left_point()
    if ball.xcor()<-380:
        ball.reset_ball()
        scoreboard.right_point()



screen.exitonclick()
