import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_player, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    if player.at_finish_line():
        player.go_to_start()
        score.update_scoreboard()
    for i in car.all_cars:
        if player.distance(i)<20:
            game_is_on = False
            score.game_over()

screen.exitonclick()