from modules import *

def waves(x_start, x_end, y_start, y_end): #on crée la fonction "waves()" pour dessiner des vagues sur la mer
    """
    Cette fonction permet de créer des vagues
    def factorielle(n):
    :param x_start: int
    :param x_end: int
    :param y_start: int
    :param y_end: int
    """
    number = randint(20,50) #on choisit un numéro au hasard entre 20 et 50 que l'on affecte dans la variable "number" que l'on crée au même moment
    for i in range(number) : #on fait le programme autant de fois que la valeur de la variable "number"
        up() #on lève le stylet
        teleport(randint(x_start, x_end), randint(y_start, y_end)) #on déplace la tortue (sans tracer de trait) au point de coordonnées: le nombre sur l'axe des abcisses qui vaut un nombre aléatoire entre "x_start" et "x_end" qui sont définis à l'exécution de programme; et le nombre sur l'axe des ordonnées qui vaut un nombre aléatoire entre y_start et y_end qui sont définis à l'exécution du programme 
        pencolor("#154360") #on sélectionne la couleur bleu marine aux traits du stylet 
        down() #on baisse le stylet pour pouvoir modifier le dessin
        setheading(135) #on oriente la tortue à 135 degrés
        forward(6) #on fait avancer la tortue de 6 pixels
        circle(10,100) #on dessine un ar-de-cercle de 10 pixels de rayon et de 100 degrés
        setheading(205) #on oriente la totue à 205 degrés
        forward(6) #on fait avancer la tortue de 6 pixels
