import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle would win the race? Enter a color from the "
                                                          "rainbow: ").lower()
colors_rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


# Create 6 turtles with different colors
y_cor = 90
for i in range(6):
    # Initialize with the shape of the turtle
    turtle = t.Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors_rainbow[i])
    turtle.goto(x=-230, y=y_cor)
    y_cor -= 30
    all_turtles.append(turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
