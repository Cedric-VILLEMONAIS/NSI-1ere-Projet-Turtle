# Importation du fichier modules.py
from modules import *

# Création de la fonction star()
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
    # On enregistre dans la variable number un nombre aléatoire entre 1 et 50 (cela correspond au nombre d'étoiles)
    number = randint(1,50)
    # On relève le stylo
    penup()
    # Création à l'aide d'une boucle for du nombre d'étoiles définit avant
    for i in range(number) :
        # Téléportation vers une position aléatoire dans les coordonnées donnés
        teleport(randint(x_start, x_end), randint(y_start, y_end))
        # Création d'un point de rayon 4 pixel et de couleur blanc
        dot(4, "#ffffff")