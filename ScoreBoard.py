from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(-280, 270)
        self.write(f"Score: {self.score}", False, align="left", font=("Arial", 14, "normal"))
        self.hideturtle()

    def write_score(self):
        self.write(f"Score: {self.score}", False, align="left", font=("Arial", 14, "normal"))
