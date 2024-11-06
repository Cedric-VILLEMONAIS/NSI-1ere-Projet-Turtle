from modules import *

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
    
    register_shape("bird_1.gif")
    register_shape("bird_2.gif")
    setheading(0)
    bird_var = Turtle()
    bird_var.penup()
    bird_var.speed(1)
    for i in range(15) :
        bird_var.teleport(x_start-200, randint(y_start, y_end))
        while bird_var.pos()[0] < (x_end+200) :
            bird_var.shape("bird_1.gif")
            bird_var.forward(25)
            bird_var.shape("bird_2.gif")
            bird_var.forward(25)
