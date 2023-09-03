# Day 23 - The Turtle Crossing Capstone Project

Difficulty Normal 😎: Use all Steps to complete the project.

Difficulty Hard 🤔: Use only Steps 1 and 2 to complete the project.

Difficulty Expert 🤯: Only use Step 1 to complete the project.


Problem breakdown:
1. Create the player and make it move 
2. Generate limited random cars along the y-axis
3. Return the player to the starting position when reaches the top
4. Increase the level when return to the starting position
5. Increase the car speed in each level
6. Detect collision with cars
7. Game_over


## Create the player

Requirements:
- Create the player turtle
- Make the turtle move forwards with the "Up" key

In main
```python
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the player
player = Player()

screen.listen()
screen.onkey(fun=player.move_forwards, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
```
Player class
```python
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_forwards(self):
        self.forward(MOVE_DISTANCE)

```
![CleanShot 2023-09-02 at 18.48.50.gif](..%2F..%2F..%2FLibrary%2FApplication%20Support%2FCleanShot%2Fmedia%2Fmedia_kYlWnmG32a%2FCleanShot%202023-09-02%20at%2018.48.50.gif)


## Generate the cars

Requirements:
Create 1 car
- Generate random cars
- Make them move constantly
- Remove them when reach the end
- Make them in random colors

Main
```python
import random
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

# Create the car
# car = CarManager()
# List of car objects
cars = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    probability_of_respawn = random.randint(0, 9)
    if probability_of_respawn == 0:
        car = CarManager()
        cars.append(car)

    for car in cars:
        car.move()
        if car.xcor() < -330:
            cars.remove(car)


screen.exitonclick()

```
CarManager class
```python
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow4", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.pu()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.starting_position()

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def starting_position(self):
        self.goto(x=300, y=random.randint(-250, 280))
```

## Return the player when reaches the top

Requirements:

```python
    if player.ycor() > 280:
        player.start_position()
```

```python
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.setheading(90)
        self.start_position()

    def move_forwards(self):
        self.forward(MOVE_DISTANCE)

    def start_position(self):
        self.goto(STARTING_POSITION)
```

## Create the scoreboard

```python
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.color("black")
        self.current_level = 1
        self.goto(x=-230, y=260)
        self.update_scoreboard()

    def level_up(self):
        self.current_level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.current_level}", align="center", font=FONT)


```

## Increase the speed in each level





