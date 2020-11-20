from turtle import Turtle, Screen, colormode
import random
import colorgram


colors = [(141, 163, 182), (14, 119, 185), (206, 138, 168), (199, 175, 9), (240, 213, 62), (220, 156, 97), (150, 17, 34), (122, 72, 100), (13, 143, 53), (74, 29, 35), (59, 34, 31)]

screen = Screen()
tim = Turtle()
tim.shape('turtle')
colormode(255)
tim.hideturtle()


def random_colors():
    random_color = random.choice(colors)
    return random_color


def screen_shot():
    global looper
    tim.home()
    looper = False


while True:
    angles = [0, 90, 180, 270]
    tim.speed('fastest')
    (x, y) = screen.screensize()
    print(screen.screensize())
    tim.pu()
    tim.setpos(-x, -y)

    for i in range(1, 101):
        dot_color = random_colors()

        tim.dot(50, dot_color)
        tim.pu()
        tim.forward(100)

        if i % 10 == 0:
            tim.setheading(90)
            tim.forward(75)
            tim.setheading(180)
            tim.forward(1000)
            tim.setheading(0)
        screen.exitonclick()
