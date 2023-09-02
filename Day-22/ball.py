from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("white")
        self.y_speed_move = 0.5
        self.x_speed_move = 0.5

    def move_ball(self):
        new_x = self.xcor() + self.x_speed_move
        new_y = self.ycor() + self.y_speed_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_speed_move *= -1

    def bounce_x(self):
        self.x_speed_move *= -1

    def reset_position(self):
        self.home()
        self.bounce_x()

    def increase_speed(self):
        self.x_speed_move *= 1.5

    def reset_speed(self):
        self.x_speed_move = 1