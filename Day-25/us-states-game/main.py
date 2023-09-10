import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

# Shape of the turtle to be the image
turtle.shape(image)
# Message turtle
message = turtle.Turtle()
message.pu()
message.hideturtle()


# Check if the guess is among the 50 states
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

# Correct guesses
guessed_states = []

while len(guessed_states) < 50:

    # User State choice
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        # Save the missing states
        # states_to_learn.csv
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        pandas.Series(missing_states).to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        state = data[data.state == answer_state]  # Get the row of the state
        y_cor = state["y"].item()  # Get the value without dtype or name
        x_cor = state["x"].item()
        message.goto(x_cor, y_cor)  # Go to the location of the state
        message.write(answer_state)  # Write the name of the state
        guessed_states.append(answer_state)  # Add the state to the list

