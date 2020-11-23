from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.players = {}
        self.create_players()
        self.players_move_position()
        self.player_paddle = self.players[0]
        self.computer_paddle = self.players[1]

    def create_players(self):
        for x in range(2):
            paddle = Turtle("square")
            paddle.color("white")
            paddle.pu()
            paddle.goto(0, 10)
            self.players[x] = paddle
        self.players[0].shapesize(stretch_wid=5.1, stretch_len=1)
        self.players[1].shapesize(stretch_wid=1, stretch_len=5.1)
        self.players[1].setheading(90)


    def players_move_position(self):
        xcor = 720
        for player in self.players:
            self.players[player].goto(xcor, 0)
            xcor *= -1

    def move_player_up(self):
        if self.player_paddle.ycor() < 440:
            new_y = self.player_paddle.ycor() + 30
            self.player_paddle.goto(self.player_paddle.xcor(), new_y)

    def move_player_down(self):
        if self.player_paddle.ycor() > -440:
            new_y = self.player_paddle.ycor() - 30
            self.player_paddle.goto(self.player_paddle.xcor(), new_y)

    def computer_moves(self, ball_position_y):
        computer_y = self.computer_paddle.ycor()
        if ball_position_y != computer_y:
            y_diffrence = computer_y+10/ball_position_y
            y_factor = y_diffrence/abs(y_diffrence)
            self.computer_paddle.forward(20*y_factor)
