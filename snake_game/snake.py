from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        xcor = 0

        for _ in range(3):
            snake = Turtle("square")
            snake.color("white")
            snake.pu()
            snake.goto(xcor, 0)
            xcor += -20
            self.snake_body.append(snake)

    def move_forward(self):
        for seg_num in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[seg_num-1].xcor()
            new_y = self.snake_body[seg_num-1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_body[0].forward(20)

    def turn_up(self):
        if int(self.snake_body[0].heading()) != 270:
            self.snake_body[0].setheading(90)

    def turn_down(self):
        if int(self.snake_body[0].heading()) != 90:
            self.snake_body[0].setheading(270)

    def turn_left(self):
        if int(self.snake_body[0].heading()) != 0:
            self.snake_body[0].setheading(180)

    def turn_right(self):
        if int(self.snake_body[0].heading()) != 180:
            self.snake_body[0].setheading(0)

    def add_tail(self):
        snake = Turtle("square")
        snake.color = "white"
        snake.pU()

        if self.snake_body[-1].ycor() == self.snake_body[-2].ycor():
            new_y = self.snake_body[-1].ycor()
        else:
            new_y = self.snake_body[-1].ycor() - 20

        if self.snake_body[-1].xcor() == self.snake_body[-2].xcor():
            new_x = self.snake_body[-1].xcor()
        else:
            new_x = self.snake_body[-1].xcor() - 20

        snake.goto(new_x,new_y)
        self.snake_body.append(snake)