from turtle import Screen, Turtle, color
import random
import turtle
import colorgram

tim = Turtle()
turtle.colormode(255)

colors = colorgram.extract('day18\image.jpg', 30)

list_colors = []

for i in range(len(colors)):
    rgb_tuple = (colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b)
    list_colors.append(rgb_tuple)


color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
              (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


screen = Screen()

tim.speed("fastest")
x_iterations = 10
y_iterations = 10

start_x = tim.pos()[0]
start_y = tim.pos()[1]

x_pos = start_x
y_pos = start_y
for _ in range(y_iterations):

    for _ in range(x_iterations):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        x_pos += 50
        tim.setpos((x_pos, y_pos))
        tim.pendown()
    tim.penup()
    y_pos += 50
    x_pos = 0
    tim.setpos((x_pos, y_pos))
    tim.pendown()


screen.exitonclick()
