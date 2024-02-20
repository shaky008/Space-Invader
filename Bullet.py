from turtle import Turtle

class Bullet(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.setheading(90)
        self.pencolor("yellow")
        self.shapesize(0.5,0.5)
        self.penup()
        self.hideturtle()
        self.state = "ready"
        self.speed = 5


    def fire(self, player):
        if self.state == 'ready':
            self.goto(player.xcor(), player.ycor())
            self.state = "fire"

