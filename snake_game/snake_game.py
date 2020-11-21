from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

game_on = True
screen.update()
snake = Snake()
food = Food()
score_board = ScoreBoard()


def game_over_control():
    global game_on
    if snake.head.xcor() > 275 or snake.head.xcor() < -275 or snake.head.ycor() < -275 or snake.head.ycor() > 275:
        print("You hit the wall!")
        game_on = False

    for segment in snake.snake_body:
        if segment == snake.head:
            pass
        else:
            if snake.head.distance(segment) < 8:
                print("You hit the tail!")
                game_on = False

    if not game_on:
        choose = screen.textinput('Play Again?', 'Do you want to play again? Press y or n: ')
        if choose.lower() == 'y':
            score_board.clear_scoreboard()
            snake.base_snake()
            game_on = True
            screen.listen()


screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_tail()
        score_board.increase_score()

    game_over_control()

screen.exitonclick()
