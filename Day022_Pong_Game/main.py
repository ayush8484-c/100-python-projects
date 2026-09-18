from turtle import Screen
from paddle import *
from ball import Ball
from scoreboard import Scoreboard
from borders import *
import time


screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("Pong Game")

ball = Ball()
scoreboard = Scoreboard()
border = border_line()
mid = mid_line()

screen.listen()
screen.onkey(right_up, "Up")
screen.onkey(right_down, "Down")
screen.onkey(left_up, "w")
screen.onkey(left_down, "s")


is_game_on = True
while is_game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Wall collision
    if ball.ycor() > 235 or ball.ycor() < -235:
        ball.y_move *= -1


    # Right paddle
    if 350 < ball.xcor() < 370:
        if paddles[0].ycor() + 50 > ball.ycor() > paddles[0].ycor() - 50:
            if ball.x_move > 0:
                ball.x_move *= -1
                ball.increase_speed()

    # Left paddle
    if -370 < ball.xcor() < -350:
        if paddles[1].ycor() + 50 > ball.ycor() > paddles[1].ycor() - 50:
            if ball.x_move < 0:
                ball.x_move *= -1
                ball.increase_speed()


    # Player misses
    if ball.xcor() > 380:
        scoreboard.left_point()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.right_point()
        ball.reset_position()







screen.exitonclick()