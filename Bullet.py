from turtle import Turtle

class Bullet(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.setheading(90)
        self.pencolor("yellow")
        self.shapesize(0.5,0.5)
        self.hideturtle()