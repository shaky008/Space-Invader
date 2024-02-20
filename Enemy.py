from turtle import Turtle

class Enemy(Turtle):

    def __init__(self):
        super().__init__()
        self.screen.register_shape("Images/invader.gif")
        self.shape("Images/invader.gif")

