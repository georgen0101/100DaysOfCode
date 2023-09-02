from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Welcome to the Pong Game")
# Tracer method
screen.tracer(0)


# Create the paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create the ball
ball = Ball()

# Create the scoreboard
scoreboard = Scoreboard()


# Move the paddle
screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

# Game loop
is_game_on = True
while is_game_on:
    screen.update()
    # Wall collision and bounce
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    ball.move_ball()

    # Detect collision with a paddle
    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.increase_speed()
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.reset_position()
        ball.reset_speed()

    # Detect L paddle misses
    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.reset_position()
        ball.reset_speed()

screen.exitonclick()
