from modules import *

def sea(x_start, x_end, y_start, y_end) : #on crée une fonction "sea()" pour dessiner la mer
    """
    cette fonction permet de faire apparaître la plage
    :param x_start: int
    :param x_end: int
    :param y_start: int
    :param y_end: int
    """
    teleport(x_start,y_start) #on déplace la tortue, en interrompant le dessin pour cette action, au point d'abcisse "x_start" (défini au moment de l'exécution du programme) et d'ordonnée "y_start" (défini au moment de l'exécution du programme)
    color("#21618C") #on sélectionne la couleur bleu foncé pour les traits
    fillcolor("#21618C") #on sélectione également la couleur bleu foncé pour le mode remplissage
    begin_fill() #on active le mode remplissage
    goto(x_end, y_start) #on déplace la tortue sans interrompre le dessin au point d'abcisse "x_end" (défini au moment de l'exécution du programme) et d'ordonnée "y_start" (défini au moment de l'exécution du programme)
    goto(x_end,y_end) #on déplace la tortue sans interrompre le dessin au point d'abcisse "x_end" (défini au moment de l'exécution du programme) et d'ordonnée "y_end" (défini au moment de l'exécution du programme)
    goto(x_start,y_end) #on déplace la tortue sans interrompre le dessin au point d'abcisse "x_start" (défini au moment de l'exécution du programme) et d'ordonnée "y_end" (défini au moment de l'exécution du programme)
    goto(x_start, y_start) #on déplace la tortue sans interrompre le dessin au point d'abcisse "x_start" (défini au moment de l'exécution du programme) et d'ordonnée "y_start" (défini au moment de l'exécution du programme)
    end_fill() #on désactive le mode remplissage
