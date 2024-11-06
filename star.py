from modules import *

def star(x_start, x_end, y_start, y_end) :
    """
    Cette fonction permet de créer des étoiles
    def factorielle(n):
    :param x_start: int
    :param x_end: int
    :param y_start: int
    :param y_end: int
    """
    number = randint(1,50)
    penup()
    for i in range(number) :
        try:
            teleport(randint(x_start, x_end), randint(y_start, y_end))
        except:
            my_teleport(randint(x_start, x_end), randint(y_start, y_end))
        dot(4, "#ffffff")