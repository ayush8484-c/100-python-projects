import random

from color_extraction import color_list
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.shape("turtle")
timmy.penup()
timmy.hideturtle()
timmy.goto(-250, -250)




def horizontal_line():
    for _ in range(10):
        timmy.dot(10, random.choice(color_list))
        timmy.forward(50)


def vertical_line():
    timmy.penup()
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)


for _ in range(10):
    horizontal_line()

    if _ < 9:  # Only call vertical_line if not the last row
        vertical_line()


screen.exitonclick()