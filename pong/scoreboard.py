from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.opponent_score = 0
        self.player_score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0, 430)
        self.create_scoreboard()
        self.create_line()

    def create_scoreboard(self):
        self.write(f"{self.opponent_score}            {self.player_score}", align=ALIGN, font=FONT)

    def create_line(self):
        line_y = 480
        for i in range(20):
            line = Turtle("square")
            line.color("white")
            line.pu()
            line.shapesize(stretch_wid=1, stretch_len=0.5)
            line.goto(0, line_y)
            line_y -= 50

    def update_scoreboard(self, player):
        self.clear()
        if player == 0:
            self.player_score += 1
        else:
            self.opponent_score += 1

        self.write(f"{self.opponent_score}            {self.player_score}", align=ALIGN, font=FONT)
