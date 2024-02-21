import turtle
from ScoreBoard import ScoreBoard
from Player import Player
from Enemy import Enemy
from Bullet import Bullet
import random


def is_collision(turtle1, turtle2):
    distance = turtle1.distance(turtle2.xcor(), turtle2.ycor())
    return distance < 20


wn = turtle.Screen()

wn.setup(700, 700)
wn.bgcolor("black")
wn.title("The Lord Of The Space: Return Of The Invaders")
# wn.bgpic("Images/space_invaders_background.gif")
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
wn.onkey(lambda: bullet.fire(player), "space")

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
        if (score.score == 200):
            gameOver = True
            score.you_won()

        if is_collision(player, enemy):
            gameOver = True
            score.game_over()
            player.hideturtle()

        if enemy.ycor() < -270:
            gameOver = True
            score.game_over()
            player.hideturtle()

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

        if bullet.state == "fire":
            bullet.showturtle()
            bullet.sety(bullet.ycor() + bullet.speed)

        if bullet.ycor() > 280:
            bullet.state = "ready"
            bullet.hideturtle()

        if is_collision(bullet,enemy):
            score.increase_score()
            bullet.hideturtle()
            bullet.goto(player.xcor(), player.ycor())
            bullet.state = "ready"
            new_ran_x = random.randint(-250, 250)
            new_ran_y = random.randint(100, 200)
            enemy.setpos(new_ran_x,new_ran_y)



wn.exitonclick()
