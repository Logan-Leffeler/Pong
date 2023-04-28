from turtle import Screen, Turtle
from paddle import Paddle
from puck import Puck
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

puck = Puck()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(puck.move_speed)
    screen.update()
    puck.move()

    # Detect collision with wall
    if puck.ycor() > 280 or puck.ycor() < -280:
        puck.bounce_y()


    # Detect collision with right paddle
    if puck.distance(r_paddle) < 50 and puck.xcor() > 320 or puck.distance(l_paddle) < 50 and puck.xcor() < -320:
        puck.bounce_x()


    #Detect when right paddle misses
    if puck.xcor() > 380:
        puck.reset()
        scoreboard.l_point()

    if puck.xcor() < -380:
        puck.reset()
        scoreboard.r_point()






screen.exitonclick()