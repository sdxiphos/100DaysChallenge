from turtle import Screen, Turtle
from player import Player
from level_counter import LevelCounter
from car_manager import Cars
import time
import random


screen = Screen()
screen.colormode(255)
screen.tracer(0)
screen.setup(800, 700)
game_on = True


def create_sidewalk():
    path_y = -330
    for i in range(3):
        sidewalk = Turtle("square")
        sidewalk.color("green")
        sidewalk.pu()
        sidewalk.shapesize(stretch_wid=3, stretch_len=40)
        sidewalk.goto(0,path_y)
        path_y += 300


def create_path():
    path_y = -300
    for t in range(12):
        path_x = 400
        for i in range(22):
            path = Turtle("square")
            path.color("black")
            path.up()
            path.shapesize(stretch_wid=0.2, stretch_len=1)
            path.goto(path_x, path_y)
            path_x -= 40
        path_y += 60


create_path()
create_sidewalk()
level_counter = LevelCounter()
player = Player()
cars = Cars()

screen.listen()
screen.onkeypress(player.player_move_forward, "Up")
screen.onkeypress(player.player_move_backward, "Down")


def level_up_controller():
    if player.ycor() >= 240:
        print('Level Up')
        cars.level_up()
        level_counter.update_counter()
        time.sleep(1)
        player.start_position()


def car_hit_controller():
    for car in cars.cars:
        if car.distance(player) <= 5:
            print('Player hit the car!')
            level_counter.lose_life()
            time.sleep(1)
            player.start_position()


while game_on:
    screen.update()
    time.sleep(0.1)
    cars.car_mover()
    car_hit_controller()
    level_up_controller()