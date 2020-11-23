from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        self.moving_factor_y = 1
        self.moving_factor_x = 1
        super().__init__()

        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1.3, stretch_len=1.3)
        self.pu()
        self.goto(0, 0)
        self.setheading(235)
        self.move_ball()

    def move_ball(self):
        new_x = self.xcor() + (30*self.moving_factor_x)
        new_y = self.ycor() + (30*self.moving_factor_y)
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.moving_factor_y *= -1

    def bounce_paddle(self):
        self.moving_factor_x *= -1
