from turtle import Turtle
import random
import time


def choose_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = 15
        self.first_road_y = -280
        self.second_road_y = 20
        self.first_last_x = 420
        self.second_last_x = 420
        self.car_count =  0
        self.cars = []

    def create_car(self):
        i = random.randint(1, 5)
        random_first_y = random.choice([-280, -220, -160, -100])
        random_second_y = random.choice([20, 80, 140, 200])
        if i == 4 and self.car_count != 50:
            car = Turtle("square")
            car.color(choose_color())
            car.pu()
            car.shapesize(stretch_wid=1, stretch_len=1.5)
            car.setheading(180)
            car.goto(420, random_first_y)
            self.car_count += 1
            self.cars.append(car)

        if i == 3 and self.car_count != 50:
            car = Turtle("square")
            car.color(choose_color())
            car.pu()
            car.shapesize(stretch_wid=1, stretch_len=1.5)
            car.setheading(180)
            car.goto(420, random_second_y)
            self.car_count += 1
            self.cars.append(car)

    def car_mover(self):

        for car in self.cars:
            if car.xcor() <= -650 and car.ycor() > 0:
                random_second_y = random.choice([20, 80, 140, 200])
                car.goto(520, random_second_y)
            elif car.xcor() <= -650 and car.ycor() < 0:
                random_first_y = random.choice([-280, -220, -160, -100])
                car.goto(520, random_first_y)
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += 3

