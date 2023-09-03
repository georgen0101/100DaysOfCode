import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("The Turtle Crossing")

# Create the player
player = Player()
screen.listen()
screen.onkey(fun=player.move_forwards, key="Up")

# Create the scoreboard
scoreboard = Scoreboard()

# Car manager
car_class = CarManager()

current_level = scoreboard.current_level

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_class.create_car()
    car_class.move_cars()

    if player.ycor() > 280:
        player.start_position()
        scoreboard.level_up()
        car_class.increase_speed()

    for car in car_class.cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
