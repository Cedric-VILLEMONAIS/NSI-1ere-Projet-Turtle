from modules import *

def bird(x_start, x_end, y_start, y_end) :
    """
    cette fonction permet de faire apparaître des oiseaux 
    :param x_start: int
    :param x_end: int
    :param y_start: int
    :param y_end: int
    """
    
    register_shape("bird_1.gif")
    register_shape("bird_2.gif")
    setheading(0)
    bird_var = Turtle()
    bird_var.penup()
    bird_var.speed(1)
    while True :
        bird_var.teleport(x_start-200, randint(y_start, y_end))
        while bird_var.pos()[0] < (x_end+200) :
            bird_var.shape("bird_1.gif")
            bird_var.forward(25)
            bird_var.shape("bird_2.gif")
            bird_var.forward(25)
