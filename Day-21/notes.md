# Day 21 - Build the Snake Game Part 2: Inheritance & List Slicing
Goals:

Build the first part of the Snake game
- End with 3 classes: Snake(), Food() and Scoreboard()


Breakdown the problem:

1. Create a snake body (day 1)
2. Move the snake (day 1)
3. Create snake food (day 1)
4. Detect collision with food (day 2)
5. Create a scoreboard (day 2)
6. Detect collision with wall (day 2)
7. Detect collision with tail (day 2)


## Detect collision with food

### Class inheritance
> Take the method and attributes a class(superclass) to use and modify in a new class(subclass).
```python
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()  # Not strictly required

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()
```

### Create the food class

```python
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.shapesize(stretch_wid=10, stretch_len=10)
        self.color("red")
        self.speed(0)
        random_x = random.randint(a=-280, b=280)
        random_y = random.randint(a=-280, b=280)
        self.goto(x=random_x, y=random_y)
```

### Detect the collision between the food and snake head

Code from main
```python
    # Detect collision
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
```
See if the distance between the food(turtle instance) and head(turtle instance) is lesser than 15.
If yes the food goes to another random location.

Food method
```python
    def refresh(self):
        random_x = random.randint(a=-280, b=280)
        random_y = random.randint(a=-280, b=280)
        self.goto(x=random_x, y=random_y)
```

![CleanShot 2023-08-31 at 18.50.07.gif](..%2F..%2F..%2FLibrary%2FApplication%20Support%2FCleanShot%2Fmedia%2Fmedia_UhtchVoiBH%2FCleanShot%202023-08-31%20at%2018.50.07.gif)

## Create a scoreboard

```python
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=260)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

```
![CleanShot 2023-08-31 at 18.51.04.gif](..%2F..%2F..%2FLibrary%2FApplication%20Support%2FCleanShot%2Fmedia%2Fmedia_Ee8ilELqrB%2FCleanShot%202023-08-31%20at%2018.51.04.gif)


## Detect collision with wall

In main
```python
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
```

Scoreboard method
```python
    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
```

![CleanShot 2023-08-31 at 19.01.35.gif](..%2F..%2F..%2FLibrary%2FApplication%20Support%2FCleanShot%2Fmedia%2Fmedia_scdKod15U6%2FCleanShot%202023-08-31%20at%2019.01.35.gif)


## Detect collision with tail

### Extend the snake when it gets food

In main
```python
    if snake.head.distance(food) < 15:
        print(scoreboard.score)
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
```

In Snake class

```python
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.pu()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # Add a new segment
        self.add_segment(self.segments[-1].position())
```

![CleanShot 2023-08-31 at 19.08.33.gif](..%2F..%2F..%2FLibrary%2FApplication%20Support%2FCleanShot%2Fmedia%2Fmedia_uHVFg7LqBC%2FCleanShot%202023-08-31%20at%2019.08.33.gif)

### Collision with segments

```python
    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        # If the head collides with any segment in the tail
        elif snake.head.distance(segment) < 10:
            # Trigger Game over
            game_is_on = False
            scoreboard.game_over()
```

![CleanShot 2023-08-31 at 20.36.36.gif](..%2F..%2F..%2FLibrary%2FApplication%20Support%2FCleanShot%2Fmedia%2Fmedia_ygCVR6IaBZ%2FCleanShot%202023-08-31%20at%2020.36.36.gif)

#### With Slicing

```python
    # Detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        # If the head collides with any segment in the tail
        if snake.head.distance(segment) < 10:
            # Trigger Game over
            game_is_on = False
            scoreboard.game_over()
```
