from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)

is_race_on = False

colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]
y_positions = [-250, -150, -50, 50, 150, 250]
all_turtle = []


for turtle in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(-300, y_positions[turtle])
    all_turtle.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        turtle.forward(random.randint(0, 10))

        if turtle.xcor() > 300:
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle is the winner!")
            is_race_on = False


screen.exitonclick()