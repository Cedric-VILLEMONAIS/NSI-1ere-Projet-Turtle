from turtle import *
from random import randint

def cloud() :
    number = randint(1,10)
    hideturtle()
    pendown()
    color("#cacaca")
    for i in range(number):
        teleport(randint(-750, 750), randint(0,375))
        forward(50*randint(1,5))
