from modules import *

def reflection(x_start, x_end, y_start, y_end):
    """
    Cette fonction permet de représenter le reflet du soleil sur la mer
    :param x_start: int
    :param x_end: int
    :param y_start: int
    :param y_end: int
    """
    up()
    goto(x,y)
    down()
    color("") # créer variable soleil couleur pour la mettre la
    fillcolor("")
