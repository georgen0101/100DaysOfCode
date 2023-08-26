import turtle as t
import random as rd

tim = t.Turtle()
tim.hideturtle()
screen = t.Screen()
tim.speed(0)
tim.penup()
t.colormode(255)
screen.bgcolor((248, 244, 233))

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
              (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
              (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42),
              (210, 200, 151)]


screen.setup(width=600, height=600)


for y_cor in range(-225, 275, 50):
    for x_cor in range(-225, 275, 50):
        tim.goto(x_cor, y_cor)
        tim.dot(20, rd.choice(color_list))


screen.exitonclick()
