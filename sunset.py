from modules import *

def sunset() : #on crée une fonction "sunset()" pour dessiner un soleil différent en fonction de l'heure choisie par l'utilisateur pour faire un soleil couchant plus ou moins prononcé en fonction de l'heure
    """
    Cette fonction permet de dessiner un soleil ainsi que de lui attribuer une couleur et de le déplacer en fonction de l'heure choisie précédemment
    """   
    up() #on lève le stylet
    x=0 #on crée une variable "x" à laquelle on affecte 0
    y=0 #on crée une variable "y" à laquelle on affecte 0
    seth(90) #on oriente la tortue vers le nord (le haut du dessin)
    if 17>=user_hour<18: #on réalise le programme suivant si l'heure choisie par l'utilisateur est entre 17 inclus et 18 non inclus
        x=-80 #on affecte -80 à la variable x"
        goto(x,y)
        x=xcor()
        down()
        fillcolor("#FCFE43")
        begin_fill()
        color("#FCFE43")
        circle(100,180)
    elif 18>=user_hour<19:
        x=-200
        goto(x,y)
        x=xcor()
        down()
        fillcolor("#FFD668")
        begin_fill()
        color("#FFD668")
        circle(70,180)
    elif 19>=user_hour<20:
        x=-300
        goto(x,y)
        x=xcor()
        down()
        fillcolor("#FFCF68")
        begin_fill()
        color("#FFCF68")
        circle(40,180)
    elif 20>=user_hour<21:
        x=-400
        goto(x,y)
        x=xcor()
        down()
        fillcolor("#FFBF68")
        begin_fill()
        color("#FFBF68")
        circle(20,180)
    else:
        x=-500
        goto(x,y)
        x=xcor()
        down()
        fillcolor("#FF9668")
        begin_fill()
        color("#FF9668")
        circle(10,180)
    goto(x,0)
    end_fill()
        
       
