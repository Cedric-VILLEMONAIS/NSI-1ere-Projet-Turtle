from modules import *

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
    
    teleport(x_start,y_start)
    color("#eabb75")
    fillcolor("#eabb75")
    begin_fill()
    goto(x_end, y_start)
    goto(x_end,y_end)
    goto(x_start,y_end)
    goto(x_start, y_start)
    end_fill()