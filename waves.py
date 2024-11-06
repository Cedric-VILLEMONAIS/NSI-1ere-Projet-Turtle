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
        width = randint(6,10) #on fait choisir au programme un nombre aléatoire entre 6 et 10 pour changer l'épaisseur du trait 
        up() #on lève le stylet
        teleport(randint(x_start, x_end), randint(y_start, y_end)) #
        pencolor("#154360") #
        down()
        setheading(135)
        forward(6)
        circle(10,100)
        setheading(205)
        forward(6)
