# Importation du fichier modules.py
from modules import *

# Création de la fonction cloud()
def cloud(x_start, x_end, y_start, y_end) :
    """
    Cette fonction permet de faire apparaître des nuages à des tailles et positions aléatoires aux coordonnées données
    Arguments :
        :param x_start: int
            Coordonnée x de départ pour le dessin
        :param x_end: int
            Coordonnée x de fin pour le dessin
        :param y_start: int
            Coordonnée y de départ pour le dessin
        :param y_end: int
            Coordonnée y de fin pour le dessin
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