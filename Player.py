from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.screen.register_shape("Images/player.gif") 
        self.shape("Images/player.gif")
        self.penup()
        self.goto(0, -250)
        self.setheading(90)

    # disable movement of player if reached boundary
    def left(self):
        if(self.xcor() < -280):
            self.setx(self.xcor() - 0)
        else:
            self.setx(self.xcor() - 20)

    def right(self):
        if(self.xcor() > 280):
            self.setx(self.xcor() + 0)
        else:
            self.setx(self.xcor() + 20)


