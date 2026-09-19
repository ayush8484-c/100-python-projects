from turtle import Turtle, Screen
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
MOVE_INCREMENT = 10


class Player:
    def __init__(self, screen):
        self.level = 1
        self.car_speed = 10
        self.player = Turtle("turtle")
        self.player.penup()
        self.player.goto(STARTING_POSITION)
        self.player.setheading(90)
        self.player.color("black")
        self.screen = screen
        self.screen.listen()
        self.screen.onkey(self.move, "Up")

    def move(self):
        self.player.forward(MOVE_DISTANCE)



