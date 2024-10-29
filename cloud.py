from turtle import *
from random import randint

def cloud() :
    number = randint(1,10)
    # hideturtle()
    pendown()
    color("#cacaca")
    for i in range(number):
        width = randint(1,5)
        teleport(randint(-750, 750), randint(0,375))
        x_origin = xcor()
        begin_fill()
        forward(50*width)
        while xcor() > x_origin :
            circle(7.5*width,randint(180,250))
            right(180)
        setheading(0)