from turtle import Turtle

FINISH_LINE_Y = 280

def car_collision(player, car_manager):
    for car in car_manager.cars:
        if player.distance(car) < 20:
            print("Car collision detected!")
            return True
    return False

def sussessful_crossing(player,  finish_line_y):
    if player.ycor() >= finish_line_y:
        print("Successful crossing!")
        return True
    return False

