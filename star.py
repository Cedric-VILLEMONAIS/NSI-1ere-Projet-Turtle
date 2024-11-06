from modules import *

def star(x_start, x_end, y_start, y_end) :
    """
    Cette fonction permet de créer des étoiles à des positions aléatoires aux coordonnées données
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
    number = randint(1,50)
    penup()
    for i in range(number) :
        teleport(randint(x_start, x_end), randint(y_start, y_end))
        dot(4, "#ffffff")