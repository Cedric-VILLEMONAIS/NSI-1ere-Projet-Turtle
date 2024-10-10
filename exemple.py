from turtle import *
# Application 1 :
forward(60) # la tortue avance de 60 pixels
left(120) # la tortue tourne sur elle-même de 120° à gauche
forward(60) # la tortue avance de 60 pixels
right(90) # la tortue tourne de 90° à droite
circle(60, 300) # trace un arc de rayon 60 et d'angle 300°
right(90) # la tortue tourne de 90° à droite
forward(60) # la tortue avance de 60 pixels
goto(0, 0) # revient à la position initiale
#done() # pour pycharm pour que la fenêtre ne se ferme pas
exitonclick() # ou pour que la fenêtre ne se ferme pas à la fin du dessin

#Application 2 :
# rectangle épais
width(6) #epaisseur du trait
color(1, 0, 0) # R max, G = 0, B = 0,
goto(60, 0)
goto(60, 110)
goto(0, 110)
goto(0, 0)
#deplacement
up()
goto(5, 5)
down()
#sablier gris clair
width(1)
fillcolor("grey")
begin_fill()
goto(55, 5)
goto(5, 105)
goto(55, 105)
goto(5, 5)
end_fill()
done()

# Application 3 :
def spirale_carre(n, increment):
    speed(5) # parametrage de la vitesse de 1 lent à 10 rapide, 0 étant la vitesse la plus rapide
    shape("turtle") # choix de la forme de la tortue
    pencolor("red") # choix de la couleur du crayon
    pensize(4) # épaisseur du crayon
    up() # lever le crayon
    goto(0, 0) # aller à la position (0,0)
    setheading(0) # orientation de la tortue vers l'Est / 90 Nord / 180 Ouest / 270 Sud
    down() # poser le crayon
    angle = 90 # angle de rotation
    cote = 0 # longueur du coté tracé
    for k in range(4 * n):
        cote = cote + increment
        forward(cote) # avancer de cote pixels
        left(angle) # tourner de angle degrés

spirale_carre(6, 5) # appel de la fonction pour tracer une spirale carrée
exitonclick() # indispensable en cas d'exécution dans un IDE

# Application 4 :
def carre(cote):
    for i in range(4):
        forward(cote)
        left(90)
def frise (nbre, cote):
    speed(100)
    for i in range(nbre):
        carre(cote)
        left(5)
frise(10,100)
exitonclick()