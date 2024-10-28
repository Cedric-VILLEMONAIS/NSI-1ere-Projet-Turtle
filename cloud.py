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
        begin_fill()
        forward(50*width)
        circle(15*width,randint(10,180))
