from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        pass

    def generate_car(self):
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randint(-250, 250))
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)

    def check_player_collision(self, player):
        for car in self.cars:
            if player.distance(car) < 20:
                return True

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
