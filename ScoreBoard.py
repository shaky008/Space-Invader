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

    # increases score and updates screen
    def increase_score(self):
        self.score += 10
        self.clear()
        self.write(f"Score: {self.score}", False, align="left", font=("Arial", 14, "normal"))

    # displays message if game lost
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", font=("Arial", 15, "normal"))

    # displays message if game won
    def you_won(self):
        self.goto(0, 0)
        self.write("YOU WON", False, "center", font=("Arial", 15, "normal"))


