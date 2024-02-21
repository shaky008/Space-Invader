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

    def increase_score(self):
        self.score += 10
        self.clear()
        self.write(f"Score: {self.score}", False, align="left", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", font=("Arial", 15, "normal"))

    def you_won(self):
        self.goto(0, 0)
        self.write("YOU WON", False, "center", font=("Arial", 15, "normal"))


