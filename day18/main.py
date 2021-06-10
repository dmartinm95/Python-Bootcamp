from turtle import Screen, Turtle
import random

tim = Turtle()

screen = Screen()

number_of_shapes = 8
sides = 3

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]

tim.width(10)
tim.speed("fastest")

steps = 200

for _ in range(steps):
    direction = random.choice(directions)
    tim.color(random.choice(colours))
    tim.right(direction)
    tim.forward(30)


screen.exitonclick()
