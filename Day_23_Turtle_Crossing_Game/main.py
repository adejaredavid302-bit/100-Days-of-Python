import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.clear()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Cars")
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard=Scoreboard()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()







