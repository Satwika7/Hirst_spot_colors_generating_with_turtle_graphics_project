import turtle

import colorgram
# colors=colorgram.extract('hirstimage.jpg',20)
# lists=[]
# for _ in colors:
#     lists.append(tuple(_.rgb))
# print(lists)
from turtle import Turtle,Screen
import random
turtle.colormode(255)
colors_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61), (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39), (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58)]
tim = Turtle()
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
y = tim.ycor()
x = tim.xcor()
tim.hideturtle()
for __ in range(10):
    for _ in range(10):
        tim.dot(20,random.choice(colors_list))
        tim.penup()
        tim.forward(50)
    tim.goto(x,tim.ycor()+50)

sc = Screen()
sc.exitonclick()