from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow4", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        probability_of_spawn = random.randint(0, 5)
        if probability_of_spawn == 0:
            new_car = Turtle("square")
            new_car.pu()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.goto(x=300, y=random.randint(-250, 280))
            self.cars.append(new_car)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)
