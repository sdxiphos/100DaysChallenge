from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from ball import Ball
import time


screen = Screen()
screen.tracer(0)
screen.setup(1500, 1000)
screen.bgcolor("black")

ball = Ball()
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move_player_up, "Up")
screen.onkeypress(player.move_player_down, "Down")


def goal_control():
    if ball.xcor() < -760:
        scoreboard.update_scoreboard(0)
        ball.goto(0, 0)
        return True

    if ball.xcor() > 760:
        scoreboard.update_scoreboard(1)
        ball.goto(0, 0)
        return True

    return False


while True:
    screen.update()
    time.sleep(0.07)
    ball.move_ball()

    if ball.xcor() < - 350:
        player.computer_moves( ball.ycor())

    if ball.ycor() > 470 or ball.ycor() < -470:
        ball.bounce_wall()

    if ball.distance(player.players[0]) < 50:
        ball.bounce_paddle()

    if goal_control():
        screen.update()
        time.sleep(1)




screen.exitonclick()