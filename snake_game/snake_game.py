from turtle import Turtle, Screen
import time
import snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

game_on = True
screen.update()
snake = snake.Snake()
screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()
