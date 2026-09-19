import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from collision import car_collision , sussessful_crossing
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player(screen)
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move_cars()

    if car_collision(turtle.player, car_manager):
        game_is_on = False
        scoreboard.game_over()

    if sussessful_crossing(turtle.player, 280):
        turtle.player.goto(0, -280)
        car_manager.car_speed += 5
        scoreboard.increase_level()
        print(f"Level: {scoreboard.level}")

    screen.update()



screen.exitonclick()