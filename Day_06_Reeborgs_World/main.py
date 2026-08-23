def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_right()

while at_goal()==False:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()