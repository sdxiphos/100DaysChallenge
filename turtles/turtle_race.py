import random
from turtle import Turtle, Screen

bets = []
all_turtles = []
is_race_on = False
screen = Screen()
screen.setup(500, 400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]


def player_choose():
    global bets
    bets = []
    player_count = int(screen.textinput("Player Count", "How many players are going to bet: "))

    for i in range(player_count):
        bet = screen.textinput("Let's Get Your Bet", "Pleace choose your turtle? Enter a color: ")
        bets.append(bet)


def starting_position():

    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.pu()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=-230, y=y_position[turtle_index])
        all_turtles.append(new_turtle)


player_choose()
starting_position()

if bets:
    is_race_on = True


def retry_position():
    for tim in all_turtles:
        tim.goto(x=-230, y=tim.ycor())


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color in bets:
                print(f"{bets.index(winning_color)+1}. player have won! The winning turtle is: {winning_color}")

            else:
                print(f"You have lost! The winning turtle is: {winning_color}")
            play_again = screen.textinput("Play Again", "Do you want to play again! y or n: ")
            if play_again == 'y':
                is_race_on = True
                retry_position()
                player_choose()


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()