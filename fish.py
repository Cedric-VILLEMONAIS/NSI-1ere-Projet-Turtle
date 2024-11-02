from modules import *

def fish(x_start, x_end, y_start, y_end):
    """
    Cette fonction permet de créer des poissons
    def factorielle(n):
    :param x_start: int
    :param x_end: int
    :param y_start: int
    :param y_end: int
    """
    number = randint(5,10)
    penup()
    for i in range(number) :
        width = randint(1,3)
        up()
        teleport(randint(x_start, x_end), randint(y_start, y_end))
        pencolor("#646969")
        fillcolor("#646969")
        down()
        setheading(randint(0,360))
        dot(randint(4,6))
        begin_fill()
        right(60)
        forward(6)
        left(120)
        forward(6)
        left(120)
        forward(6)
        end_fill()
