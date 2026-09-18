from turtle import Turtle

def mid_line():
    tim = Turtle()
    tim.penup()
    tim.hideturtle()
    tim.goto(0, 235)
    tim.pensize(5)
    tim.setheading(270)
    tim.color("white")

    for _ in range(11):
        tim.pendown()
        tim.fd(20)
        tim.penup()
        tim.fd(25)


def border_line():
    tim = Turtle()
    tim.penup()
    tim.goto(-395, 245)
    tim.pendown()

    tim.color("white")
    tim.pensize(5)

    for _ in range(2):
        tim.forward(790)
        tim.right(90)
        tim.forward(490)
        tim.right(90)

    tim.hideturtle()

