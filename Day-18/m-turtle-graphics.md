# Day 18 - Turtle Graphics, Tuples and Importing Modules

We used the python module turtle to draw graphics into the screen.

### Reading Documentation:
- Use the documentation of the module to search for functions or variables.
- Use Google to search how to use it
- Use AI

**Tk interface**:
A module to create a GUI.
> GUI - Graphical User Interface


### First Challenge: Draw a square
```python
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("chocolate")

for step in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)


screen = Screen()
screen.exitonclick()
```
![img.png](img.png)

### Importing Modules

**Basic Import**:<br>
```python
# Import
import turtle

# Syntax
tim = turtle.Turtle()
```

**from...import...**:<br>
When we use one specific import a lot.
```python
from turtle import Turtle

# Syntax:
tim = Turtle()
```

**from...import (*)**:<br>
Import all the methods and variables
```python
from turtle import *
from random import *

# Syntax
forward(100)
random()
choice("hello")
```

**Aliases modules**:<br>
Give the module a alias name
```python
import turtle as t

# Syntax
tim = t.Turtle()
```

## Python standard library
All the modules that are included in python, like the turtle module.

### Access another modules
We use PyPI to install the modules.

## Challenge 2 - Draw Dashed line
My first attempt:
```python
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("chocolate")

for _ in range(4):
    for steps in range(10):
        if steps % 2:
            tim.pu()
            tim.forward(10)
        tim.pd()
        tim.forward(10)
    tim.right(90)


screen = Screen()
screen.exitonclick()
```
Simple version:
```python
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("chocolate")

for _ in range(4):
    for steps in range(10):
        tim.pu()
        tim.forward(10)
        tim.pd()
        tim.forward(10)
    tim.right(90)


screen = Screen()
screen.exitonclick()
```

![img_1.png](img_1.png)

## Challenge 3:
Solution: Use 360 and divide by the corners.

```python
from turtle import Turtle, Screen
import random

number_of_colors = 100

color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]

tim = Turtle()
tim.shape("turtle")
tim.color("chocolate")

# range is exclusive.
for corners in range(3, 11):
    angle = 360 / corners  # 90 degree
    tim.pencolor(random.choice(color)) # Random color
    for sides in range(corners):
        tim.forward(100)
        tim.right(angle)

screen = Screen()
screen.exitonclick()
```

![img_2.png](img_2.png)

### With functions
Took me more to make the functions and I don't even feel satisfied by how I made them. Will force myself to make the 
code only with functions.

```python
from turtle import Turtle, Screen
from random import choice
number_of_colors = 10

color = ["#"+''.join([choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]

tim = Turtle()
tim.shape("turtle")
tim.color("chocolate")


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)


def multiple_shapes(n):
    """Start with a triangle"""
    for corner in range(3, n + 1):
        tim.pencolor(choice(color))
        draw_shape(corner)


multiple_shapes(10)

screen = Screen()
screen.exitonclick()
```

![img_3.png](img_3.png)

## Challenge 4: Random walk
https://en.wikipedia.org/wiki/Random_walk

1. Draw randomly
2. Change the thickness of the drawing
3. Speed te turtle drawing
4. The lines must be in random colors

```python
from turtle import Turtle, Screen
from random import choice
number_of_colors = 10

color = ["#"+''.join([choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]

tim = Turtle()
tim.hideturtle()
screen = Screen()
# screen.screensize(5000, 3000)
tim.speed(0)


def random_direction():
    """Set tim to a random heading direction"""
    angles = [0, 90, 180, 270]
    tim.setheading(choice(angles))


def move_randomly():
    """This function move tim forward by 50 steps with a pensize of 10 and a random color"""
    tim.pencolor(choice(color))
    tim.pensize(5)
    tim.forward(20)
    random_direction()


for i in range(500):
    move_randomly()


screen.exitonclick()
```

![img_4.png](img_4.png)

## Generate random colors in RGB with tuples

```python
import turtle as t
import random as rd

tim = t.Turtle()
tim.hideturtle()
screen = t.Screen()
tim.speed(0)
t.colormode(255)


def random_color():
    r = rd.randint(0, 255)  # Inclusive range
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    return (r, g, b)


def random_direction():
    """Set tim to a random heading direction"""
    angles = [0, 90, 180, 270]
    tim.setheading(rd.choice(angles))


def move_randomly():
    """This function move tim forward by 50 steps with a pensize of 10 and a random color"""
    tim.pencolor(random_color())
    tim.pensize(5)
    tim.forward(20)
    random_direction()


for i in range(500):
    move_randomly()

screen.exitonclick()
```
![img_5.png](img_5.png)

## Draw a spirograph

- Only documentation

```python
import turtle as t
import random as rd

tim = t.Turtle()
tim.hideturtle()
screen = t.Screen()
tim.speed(0)
t.colormode(255)


def random_color():
    r = rd.randint(0, 255)  # Inclusive range
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    return (r, g, b)


def draw_spirograph(gap):
    for i in range(int(360 / gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)


draw_spirograph(1)


screen.exitonclick()

```

![img_6.png](img_6.png)
![img_7.png](img_7.png)

## Final project - The Hirst Painting


