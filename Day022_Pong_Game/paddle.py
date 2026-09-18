from turtle import Turtle


position = [(370, 0), (-370, 0)]
paddles = []


for pong in range(2):
    paddle = Turtle()
    paddle.shape("square")
    paddle.shapesize(stretch_wid=1, stretch_len=5)
    paddle.left(90)
    paddle.color("white")
    paddle.penup()
    paddle.goto(position[pong])
    paddles.append(paddle)


def right_up():
    if paddles[0].ycor() < 195:
        paddles[0].fd(20)


def right_down():
    if paddles[0].ycor() > -195:
        paddles[0].bk(20)


def left_up():
    if paddles[1].ycor() < 195:
        paddles[1].fd(20)


def left_down():
    if paddles[1].ycor() > -195:
        paddles[1].bk(20)

