import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Day 23: Turtle Crossing Capstone Project
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(player.move_up, "Up")


car_manager.generate_car()

car_tick = 0

while game_is_on:
    time.sleep(0.1)

    screen.update()
    if car_tick % 6 == 0:
        car_manager.generate_car()

    car_tick += 1

    car_manager.move_cars()

    if car_manager.check_player_collision(player):
        game_is_on = False
        scoreboard.game_over()

    if player.reached_finish_line():
        scoreboard.increase_level()
        car_manager.increase_speed()

screen.exitonclick()
