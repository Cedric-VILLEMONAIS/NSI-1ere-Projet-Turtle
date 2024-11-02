from modules import *

def cloud(x_start, x_end, y_start, y_end) :
    """
    cette fonction permet de faire apparaître des nuages 
    :param x_start: int
    :param x_end: int
    :param y_start: int
    :param y_end: int
    """
    setheading(0)
    number = randint(1,10)
    pendown()
    color("#cacaca")
    for i in range(number):
        width = randint(1,3)
        teleport(randint(x_start, x_end), randint(y_start, y_end))
        origin = pos()
        begin_fill()
        circle(7.5*width,210)
        right(140)
        while pos()[1] > origin[1] :
            circle(randint(5,9)*width,200)
            right(190)
        goto(origin)
        end_fill()
        setheading(0)