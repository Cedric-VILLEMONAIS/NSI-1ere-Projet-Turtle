# Importation du fichier modules.py
from modules import *

# Création de la fonction beach
def beach(x_start, x_end, y_start, y_end) :
    """
    Cette fonction permet de faire apparaître la plage aux coordonnées données
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
    # Téléportation de la tortue aux coordonnées donnés
    teleport(x_start,y_start)
    # Changement de la couleur du stylo ainsi que la couleur de remplissage
    color("#eabb75")
    fillcolor("#eabb75")
    # Démarrage du remplissage
    begin_fill()
    # Dessin d'un rectangle à partir des coordonnées donnés
    goto(x_end, y_start)
    goto(x_end,y_end)
    goto(x_start,y_end)
    goto(x_start, y_start)
    # Fin du remplissage
    end_fill()