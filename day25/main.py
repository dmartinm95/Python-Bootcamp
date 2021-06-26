# Day 25: U.S States Games
import pandas
import turtle

ALIGNMENT = "center"
FONT = ("Arial", 8, "bold")


screen = turtle.Screen()
screen.tracer(0)

screen.title("U.S. States Game")

image = "day25\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screen.update()

states_file = pandas.read_csv("day25\\50_states.csv")
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

states_correct = 0

game_is_on = True

guessed_states = []

while len(guessed_states) < 50:

    input = screen.textinput(
        title=f"{states_correct}/50 States Correct", prompt="What's another state's name?")

    if input != None:
        answer_state = input.title()

        answer_row = states_file[states_file["state"] == answer_state]

        if answer_state == "Exit":
            break

        if not answer_row.empty:
            guessed_states.append(answer_state)
            state_x = int(answer_row["x"])
            state_y = int(answer_row["y"])
            states_correct += 1
            new_state = turtle.Turtle()
            new_state.hideturtle()
            new_state.penup()
            new_state.goto((state_x, state_y))
            new_state.write(answer_state, False,
                            align=ALIGNMENT, font=FONT)
            screen.update()

# states_to_learn.csv
all_states = states_file["state"].to_list()
missing_states = [state for state in all_states if state not in guessed_states]

missing_states_dict = {"Missing States": missing_states}

missing_states_data_frame = pandas.DataFrame(missing_states_dict)

missing_states_data_frame.to_csv("day25\\states_to_learn.csv")
