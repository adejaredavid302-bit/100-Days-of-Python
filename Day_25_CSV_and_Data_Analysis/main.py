import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data=pandas.read_csv("./50_states.csv")
all_states=data["state"].to_list()
guessed_state=[]
while len(guessed_state)<len(all_states):
    answer_state=screen.textinput(f"{len(guessed_state)}/50","What another state's name?").title()
    if answer_state == "Exit":
        not_guessed_state = []
        for state in guessed_state:
            if state not in all_states:
                not_guessed_state.append(state)
        print(not_guessed_state)
        new_data = pandas.DataFrame(not_guessed_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        dav = turtle.Turtle()
        dav.color("red")
        dav.hideturtle()
        dav.penup()
        row = data[data["state"] == answer_state]
        dav.goto(row["x"].item(),row["y"].item())
        dav.write(answer_state)
    screen.exitonclick()
