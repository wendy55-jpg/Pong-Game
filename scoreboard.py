from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_point()

    def update_point(self):
        self.clear()
        self.goto(-150, 200)
        self.write(f"Score:{self.l_score}", align="center", font=("Arial", 15, "normal"))
        self.goto(150, 200)
        self.write(f"Score:{self.r_score}", align="center", font=("Arial", 15, "normal"))

    def left_score(self):
        self.l_score += 1
        self.update_point()

    def right_score(self):
        self.r_score += 1
        self.update_point()