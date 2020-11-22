from turtle import Screen
from player import Player
from scoreboard import Scoreboard
import time


screen = Screen()
screen.tracer(0)
screen.setup(1500, 1000)
screen.bgcolor("black")


player = Player()
scoreboard = Scoreboard()
screen.update()



screen.exitonclick()