from turtle import Turtle
FONT = ("Arial", 22, "normal")


class LevelCounter(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = []
        self.live_counter = 3
        self.level = 0
        self.counter = []
        self.create_counter()
        self.create_life_counter()

    def create_counter(self):
        level_counter = Turtle("square")
        level_counter.color("black")
        level_counter.pu()
        level_counter.hideturtle()
        level_counter.shapesize(stretch_wid=2, stretch_len=4)
        level_counter.goto(-360, 310)
        self.counter.append(level_counter)
        self.update_counter()

    def create_life_counter(self):
        life_x = 360
        for i in range(3):
            life_turtle = Turtle("turtle")
            life_turtle.color("red")
            life_turtle.pu()
            life_turtle.setheading(90)
            life_turtle.shapesize(stretch_wid=1.7, stretch_len=1.7)
            life_turtle.goto(life_x, 320)
            life_x -= 35
            self.lives.append(life_turtle)

    def lose_life(self):
        self.lives[self.live_counter-1].color("pink")
        self.live_counter -= 1
        if self.live_counter == 0:
            return False
        return True

    def write_score(self):
        self.counter[0].write(f"Level: {self.level}", font=FONT)

    def update_counter(self):
        self.level += 1
        self.counter[0].clear()
        self.write_score()

    def reset_counter(self):
        self.live_counter = 3
        self.level = 0
        self.update_counter()
        for live in self.lives:
            live.color("red")

