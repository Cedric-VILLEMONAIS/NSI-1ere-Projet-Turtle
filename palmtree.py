from modules import *



def palmtree(): #on crée la fonction "palmtree" pour dessiner un palmier
    """
    Cette fonction permet de dessiner un palmier à droite du dessin
    """
    up() #on lève le stylet
    width = randint(1,3) #on met l'épaisseur du stylet à un nombre aléatoire entre 1 et 3
    goto(750,-375) #on déplace la tortue, avec le stylet en position écriture, au point de coordonnées 750 pour l'axe des abcisses, x, et -375 pour l'axe des ordonnées, y
    if user_hour==17 or user_hour==18: #on 
        fillcolor("#AA7B6B")
    elif user_hour==19 or user_hour==20:
        fillcolor("#6D4C41")
    else:
        fillcolor("#424949")
    pencolor("#1D0B04")
    down()
    begin_fill()
    setheading(90)
    forward(475)
    left(90)
    forward(40)
    while ycor() >= -375:
        setheading(randint(200,250))
        forward(randint(20,25))
        setheading(0)
        setx(750)
        setx(710)
        ycor()
    setx(750)
    end_fill()
    up()
    if user_hour==17 or user_hour==18:
        fillcolor("#229954")
    elif user_hour==19 or user_hour==20:
        fillcolor("#1E8449")
    else:
        fillcolor("#196F3D")
    pencolor("#145A32")
    down()
    begin_fill()
    teleport(730,100)
    setheading(130)
    forward(150)
    left(30)
    forward(40)
    left(85)
    forward(70)
    x=xcor()
    y=ycor()
    for i in range (6):
        forward(30)
        teleport(x,y)
        x=x+20
    goto(730,100)
    end_fill()
    angle= 165
    for i in range (2):
        begin_fill()
        teleport(730,100)
        setheading(angle)
        forward(150)
        left(30)
        forward(40)
        left(75)
        forward(40)
        x=xcor()
        y=ycor()
        while x<700:
            forward(30)
            teleport(x,y)
            x=x+20
        goto(730,100)
        angle=angle+30
        end_fill()
 
