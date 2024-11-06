# Importation du fichier modules.py
from modules import *

# Création de la fonction bird()
def bird(x_start, x_end, y_start, y_end) :
    """
    Cette fonction est une animation qui permet de faire apparaître des oiseaux  aux coordonnées données
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
    # Enregistrement des deux images de l'oiseau en tant que nouveaux "costumes" pour la tortue
    register_shape("bird_1.gif")
    register_shape("bird_2.gif")
    # Réglage de l'orientation de la tortue sur 0 (vers l'Est)
    setheading(0)
    # Création d'une nouvelle tortue sous le nom de bird_var
    bird_var = Turtle()
    # Relever le stylo et réglage de la vitesse sur 1
    bird_var.penup()
    bird_var.speed(1)
    # Création d'une boucle qui va créer 10 oiseaux
    for i in range(10) :
        # Téléportation de l'oiseau à x : valeur donnée -200 pour que l'oiseau de départ ne soit pas visible et à un y aléatoire dans la zone donnée
        bird_var.teleport(x_start-200, randint(y_start, y_end))
        # Tant que la tortue n'a pas dépassé le x de fin donné + 200 la tortue change de "costume" puis avance de 25 pixels
        while bird_var.pos()[0] < (x_end+200) :
            bird_var.shape("bird_1.gif")
            bird_var.forward(25)
            bird_var.shape("bird_2.gif")
            bird_var.forward(25)
