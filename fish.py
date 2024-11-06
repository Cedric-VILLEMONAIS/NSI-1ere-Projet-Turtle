from modules import *

def fish(x_start, x_end, y_start, y_end): #on crée une fonction "fish()" pour dessiner des poissons
    """
    Cette fonction permet de créer des poissons à des positions aléatoires aux coordonnées données
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
    number = randint(5,10) #on créer la variable "number" à laquelle on affecte un nombre choisit aléatoirement entre 5 et 10
    penup() #on relève le stylet
    for i in range(number) : #on créer la boucle for qui va s'exécuter number fois, c'est-à-dire, le nombre aléatoire entre 5 et 10 affecter à la variable "number"
        up() #on relève le stylet
        teleport(randint(x_start, x_end), randint(y_start, y_end)) #on déplace la tortue (sans tracer de trait) au point de coordonnées: le nombre sur l'axe des abcisses qui vaut un nombre aléatoire entre "x_start" et "x_end"; et le nombre sur l'axe des ordonnées qui vaut un nombre aléatoire entre y_start et y_end 
        pencolor("#646969") #on modifie la couleur du trait du stylo à la couleur "gris"
        fillcolor("#646969") #on sélectionne la couleur "gris" pour le remplissage 
        down() #on baisse le stylet; le stylet est en position d'écriture
        setheading(randint(0,360)) #on oriente la tortue à une direction aléatoire
        dot(randint(4,6)) #on fait un point d'épaisseur d'un nombre chosit aléatoirement entre les nombres 4 et 6
        begin_fill() #on active le mode remplissage
        right(60) #on tourne la tortue vers la droite de 60 degrés
        forward(6) #on avance la tortue de 6 pixels
        left(120) #on tourne la tortue vers la gauche de 120 degrés 
        forward(6) #on avance la tortue de 6 pixels
        left(120) #on tourne la tortue vers la gauche de 120 degrés 
        forward(6) #on avance la tortue de 6 pixels
        end_fill() #on désactive le mode remplissage
