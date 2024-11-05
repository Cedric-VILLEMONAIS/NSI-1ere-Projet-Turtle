from modules import *

def waves(x_start, x_end, y_start, y_end): 
    """
    Cette fonction permet de créer des vagues
    def factorielle(n):
    :param x_start: int
    :param x_end: int
    :param y_start: int
    :param y_end: int
    """
    number = randint(20,50)
    penup()
    for i in range(number) :
        width = randint(6,10)
        up()
        teleport(randint(x_start, x_end), randint(y_start, y_end))
        pencolor("#154360")
        down()
        setheading(135)
        forward(6)
        circle(10,100)
        setheading(205)
        forward(6)
