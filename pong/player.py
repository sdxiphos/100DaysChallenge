from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.players = {}
        self.create_players()
        self.players_move_position()


    def create_players(self):

        for x in range(2):
            ycor = 0
            player = []
            for i in range(3):
                ponger = Turtle("square")
                ponger.color("white")
                ponger.shapesize(stretch_wid=3.6, stretch_len=1)
                ponger.pu()
                ponger.goto(0, ycor)
                ycor -= 20
                player.append(ponger)
            self.players[x] = player


    def players_move_position(self):
        xcor = 720
        for player in self.players:
            template = self.players[player]
            for pong in template:
                pong.goto(xcor, pong.ycor())
            xcor *= -1
