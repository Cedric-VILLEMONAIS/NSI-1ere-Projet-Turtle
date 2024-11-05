from modules import *

def ecume():
    """
    Cette fonction permet de dessiner de l'écume
    """
    color("#F0F3F4") #on affecte du blanc comme couleur
    begin_fill() #on active le mode remplissage
    if user_hour==17 or user_hour==18 : #on réalise une condition: si l'heure choisie par l'utilisateur vaut soit 17, soit 18:
        teleport(-750,-320) #on déplace la tortue vers les coordonnées x=-750 et y=-320 sans que le stylet ne dessine un trait entre sa position actuelle et sa future position
    elif user_hour==19 or user_hour==20 : #on réalise une condition: si l'heure choisie par l'utilisateur vaut soit 19, soit 20:
        teleport(-750,-270) #on déplace la tortue vers les coordonnées x=-750 et y=-320 sans que le stylet ne dessine un trait entre sa position actuelle et sa future position
    else: #on réalise la fin de la condition: sinon:
        teleport(-750,-220) #on déplace la tortue vers les coordonnées x=-750 et y=-320 sans que le stylet ne dessine un trait entre sa position actuelle et sa future position
    y=ycor() #on
    while xcor()<750:
        if ycor()>=y+15:
            goto(randint(xcor()+5,xcor()+10),randint(ycor()-2,ycor()))
        elif ycor()<=y-10:
            goto(randint(xcor()+5,xcor()+10),randint(ycor(),ycor()+2))
        else:
            goto(randint(xcor()+5,xcor()+10),randint(ycor()-2,ycor()+2))
    goto(750,y+32)
    y=ycor()
    while xcor()> -750:
        if ycor()>=y+15:
            goto(randint(xcor()-10,xcor()-5),randint(ycor()-2,ycor()))
        elif ycor()<=y-10:
            goto(randint(xcor()-10,xcor()-5),randint(ycor(),ycor()+2))
        else:
            goto(randint(xcor()-10,xcor()-5),randint(ycor()-2,ycor()+2))
    end_fill()
