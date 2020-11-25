from turtle import Turtle
SPEED = 15


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.shape("turtle")
        self.color("black")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.setheading(90)
        self.pu()
        self.start_position()

    def player_move_forward(self):
        if self.ycor() < 250:
            self.forward(SPEED)

    def player_move_backward(self):
        if self.ycor() > -340:
            self.backward(SPEED*0.8)

    def start_position(self):
        self.goto(50, -330)
