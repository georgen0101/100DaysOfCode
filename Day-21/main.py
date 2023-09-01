from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game - Day 1")
screen.tracer(0)  # Turn off the auto update screen

# Snake OBJECT
snake = Snake()
food = Food()
scoreboard = Scoreboard()
# time.sleep(5)

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
    snake.move()  # The method to move the Snake

    # Detect collision with food
    if snake.head.distance(food) < 15:
        print(scoreboard.score)
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        # If the head collides with any segment in the tail
        if snake.head.distance(segment) < 10:
            # Trigger Game over
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
