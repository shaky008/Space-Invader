import turtle
from ScoreBoard import ScoreBoard
from Player import Player
from Enemy import Enemy
from Bullet import Bullet
import random

wn = turtle.Screen()

wn.setup(700, 700)
wn.bgcolor("black")
wn.title("Space Invader")
wn.bgpic("Images/space_invaders_background.gif")
wn.register_shape("Images/player.gif")

score = ScoreBoard()
player = Player()
bullet = Bullet()
enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()
enemy4 = Enemy()

wn.listen()
wn.onkey(player.left, "Left")
wn.onkey(player.right, "Right")

enemy_list = [enemy1, enemy2, enemy3, enemy4]

for i in range(len(enemy_list)):
    ranx = random.randint(-250, 250)
    rany = random.randint(100, 200)
    enemy_list[i].penup()
    enemy_list[i].goto(ranx, rany)
    enemy_list[i].pendown()

gameOver = False

while not gameOver:
    for enemy in enemy_list:
        if enemy.direction == "right":
            enemy.setx(enemy.xcor() + enemy.move_speed)
        elif enemy.direction == "left":
            enemy.setx(enemy.xcor() - enemy.move_speed)
        if enemy.xcor() > 280:
            enemy.direction = "left"
            enemy.sety(enemy.ycor() - enemy.drop_down)
        elif enemy.xcor() < -280:
            enemy.direction = "right"
            enemy.sety(enemy.ycor() - enemy.drop_down)

wn.exitonclick()
