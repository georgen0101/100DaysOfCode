from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.color("red")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(a=-280, b=280)
        random_y = random.randint(a=-280, b=280)
        self.goto(x=random_x, y=random_y)

