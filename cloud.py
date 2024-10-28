from turtle import *
from random import randint

def cloud() :
    number = randint(0,10)
    width = randint(0,10)

    hideturtle()
    penup()
    goto(randint(-750, 750), randint(0,375))
    pendown()
    color("#cacaca")

