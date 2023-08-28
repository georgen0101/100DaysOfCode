from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game - Day 1")
screen.tracer(0)  # Turn off the auto update screen

# Snake OBJECT
snake = Snake()
time.sleep(7)

# Liston to user actions to move the Snake
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

screen.listen()

game_is_on = True
while game_is_on:
    screen.update()  # Update the screen
    time.sleep(0.1)  # Pause the script for 0.1 s

    snake.move()


screen.exitonclick()
