import turtle as t
import random as rd
import colorgram


tim = t.Turtle()
tim.hideturtle()
screen = t.Screen()
tim.speed(0)
t.colormode(255)


colors = colorgram.extract('hirst-spot-painting.jpg', 10)
print(colors)
print(colors[0].rgb)
rgb = colors[0].rgb
print(rgb.replace("rgb", ""))



for i in range(10):
    tim.pencolor(colors[0].rgb)
    tim.pensize(10)
    tim.circle(100)
    tim.setheading(tim.heading() + 20)


screen.exitonclick()
