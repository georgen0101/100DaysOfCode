from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.pu()
        self.speed(0)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 40
        self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - 40
        self.sety(new_y)
