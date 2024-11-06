from modules import *

def sea(x_start, x_end, y_start, y_end) : #on crée une fonction "sea()" pour dessiner la mer
    """
    cette fonction permet de faire apparaître la plage aux coordonnées données
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
    teleport(x_start,y_start) #on déplace la tortue, en interrompant le dessin pour cette action, au point d'abcisse "x_start" (défini au moment de l'exécution du programme) et d'ordonnée "y_start" (défini au moment de l'exécution du programme)
    color("#21618C") #on sélectionne la couleur bleu foncé pour les traits
    fillcolor("#21618C") #on sélectione également la couleur bleu foncé pour le mode remplissage
    begin_fill() #on active le mode remplissage
    goto(x_end, y_start) #on déplace la tortue sans interrompre le dessin au point d'abcisse "x_end" (défini au moment de l'exécution du programme) et d'ordonnée "y_start" (défini au moment de l'exécution du programme)
    goto(x_end,y_end) #on déplace la tortue sans interrompre le dessin au point d'abcisse "x_end" (défini au moment de l'exécution du programme) et d'ordonnée "y_end" (défini au moment de l'exécution du programme)
    goto(x_start,y_end) #on déplace la tortue sans interrompre le dessin au point d'abcisse "x_start" (défini au moment de l'exécution du programme) et d'ordonnée "y_end" (défini au moment de l'exécution du programme)
    goto(x_start, y_start) #on déplace la tortue sans interrompre le dessin au point d'abcisse "x_start" (défini au moment de l'exécution du programme) et d'ordonnée "y_start" (défini au moment de l'exécution du programme)
    end_fill() #on désactive le mode remplissage
