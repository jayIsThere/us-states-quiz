import turtle
import pandas

guess_states = []

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
data_file = "50_states.csv"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(data_file)
states = data.state.to_list()




while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct", prompt="What's another state's name?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guess_states]
        data = pandas.DataFrame(missing_states)
        data.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        coordinate = data[data.state == answer_state]
        coordinate_x = int(coordinate.x)
        coordinate_y = int(coordinate.y)
        t.goto(coordinate_x, coordinate_y)
        t.write(answer_state)

  
