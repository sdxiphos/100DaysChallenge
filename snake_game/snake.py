from turtle import Turtle


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

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
        self.head.forward(20)

    def turn_up(self):
        if int(self.head.heading()) != 270:
            self.head.setheading(90)
            print("Up")

    def turn_down(self):
        if int(self.head.heading()) != 90:
            self.head.setheading(270)
            print("Down")

    def turn_left(self):
        if int(self.head.heading()) != 0:
            self.head.setheading(180)
            print("Left")

    def turn_right(self):
        if int(self.head.heading()) != 180:
            self.head.setheading(0)
            print("Right")

    def add_tail(self):
        snake = Turtle("square")
        snake.color("white")
        snake.pu()

        if self.snake_body[-1].ycor() == self.snake_body[-2].ycor():
            new_y = self.snake_body[-1].ycor()
        else:
            new_y = self.snake_body[-1].ycor() - 20

        if self.snake_body[-1].xcor() == self.snake_body[-2].xcor():
            new_x = self.snake_body[-1].xcor()
        else:
            new_x = self.snake_body[-1].xcor() - 20

        snake.goto(new_x, new_y)
        self.snake_body.append(snake)

    def base_snake(self):
        temporary_snake = []
        base_x = 0
        for segment in self.snake_body[3:]:
            segment.hideturtle()
            segment.goto(300, 300)
        temporary_snake = self.snake_body[0:3]
        self.snake_body = []
        self.snake_body = temporary_snake
        for i in self.snake_body:
            i.goto(base_x, 0)
            base_x -= 20
        self.head = self.snake_body[0]
        self.head.setheading(0)
