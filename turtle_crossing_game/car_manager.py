from turtle import Turtle
import random
import time


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = 15
        self.first_road_y = -280
        self.second_road_y = 20
        self.first_last_x = 420
        self.second_last_x = 420
        self.cars = []
        self.create_car()

    def color_generator(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        return color

    def create_car(self):
        for i in range(70):
            car = Turtle("square")
            car.color(self.color_generator())
            car.pu()
            car.shapesize(stretch_wid=1, stretch_len=1.5)
            car.setheading(180)
            self.cars.append(car)
        self.car_line()

    def car_mover(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += 7

    def car_line(self):
        for car in self.cars[0:35]:
            if self.first_road_y > -100:
                self.first_road_y = -280
            car.goto(self.first_last_x, self.first_road_y)
            self.first_last_x += 20
            self.first_road_y += 60

        for car in self.cars[36:69]:
            if self.second_road_y > 200:
                self.second_road_y = 20
            car.goto(self.second_last_x, self.second_road_y)
            self.second_last_x += 20
            self.second_road_y += 60
