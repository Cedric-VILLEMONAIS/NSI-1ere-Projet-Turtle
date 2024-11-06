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
    # On définit l'orientation sur 0 (vers l'Est)
    setheading(0)
    # On enregistre dans la variable number un nombre aléatoire entre 1 et 10 (cela correspond au nombre de nuages)
    number = randint(1,10)
    # On met la tortue en position d'écriture
    pendown()
    # Changement de la couleur du stylo
    color("#cacaca")
    # Création à l'aide d'une boucle for du nombre de nuages définit avant
    for i in range(number):
        # On enregistre dans la variable width un nombre aléatoire entre 1 et 3 (cela correspond a la taille des nuages)
        width = randint(1,3)
        # Téléportation vers une position aléatoire dans les coordonnées donnés
        teleport(randint(x_start, x_end), randint(y_start, y_end))
        # Enregistrement des coordonnées actuelles
        origin = pos()
        # Démarrage du remplissage
        begin_fill()
        # Création d'un cercle de taille 7.5 * la taille définit au dessus et de 210°
        circle(7.5*width,210)
        # La tortue tourne à droite de 140°
        right(140)
        # Tant que la tortue n'a pas atteint son y de départ du nuage on fait des cercles de 200°
        while pos()[1] > origin[1] :
            circle(randint(5,9)*width,200)
            right(190)
        # On retourne au point de départ du nuage pour tracer le bas du nuage
        goto(origin)
        # On arrête le remplissage
        end_fill()
        # On définit l'orientation sur 0 (vers l'Est)
        setheading(0)