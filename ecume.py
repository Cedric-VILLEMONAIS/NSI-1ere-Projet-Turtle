from modules import *

def ecume(): #on crée une fonction "ecume()" pour dessiner de l'écume
    """
    Cette fonction permet de dessiner de l'écume
    """
    color("#F0F3F4")#on affecte du blanc comme couleur
    begin_fill() #on active le mode remplissage
    if user_hour==17 or user_hour==18 : #on réalise la condition: si l'heure choisie par l'utilisateur vaut soit 17, soit 18:
        try:
            teleport(-750,-320) #on déplace la tortue au point de coordonnées: l'axe des abcisses, x, qui vaut -750 et l'axe des ordonnées, y, qui vaut -320; sans que le stylet ne dessine entre sa position actuelle et sa future position
        except:
            my_teleport(-750,-320)
    elif user_hour==19 or user_hour==20 : #on réalise la suite de la condition: si l'heure choisie par l'utilisateur vaut soit 19, soit 20:
        try:
            teleport(-750,-270) #on déplace la tortue au point de coordonnées: l'axe de abcisses, x, qui vaut -750 et l'axe des ordonnées, y, qui vaut -270; sans que le stylet ne dessine un trait entre sa position actuelle et sa future position
        except:
            my_teleport(-750,-270)
    else: #on réalise la fin de la condition: sinon:
        try:
            teleport(-750,-220) #on déplace la tortue au point de coordonnées: l'axe des abcisses, x, qui vaut -750 et l'axe des ordonnées, y,qui vaut -220; sans que le stylet ne dessine un trait entre sa position actuelle et sa future position
        except:
            my_teleport(-750,-220)    
    y=ycor() #on créer une variable "y" à laquelle on assigne la valeur "ycor()", qui est la position actuelle de la tortue sur l'axe des ordonnées uniquement
    while xcor()<750: #on effectue une boucle "while" jusqu'à ce que "xcor()", donc la position actuelle de la tortue sur l'axe des abcisses, soit inférieur à 750
        if ycor()>=y+15: #on réalise la condition: si la position actuelle de la tortue sur l'axe des ordonnées, ycor(), est supérieure ou égale à la variable "y" à laquelle on ajoute 15:
            goto(randint(xcor()+5,xcor()+10),randint(ycor()-2,ycor())) #on déplace la tortue, avec le stylet baissé et donc en position d'écriture, à une position aléatoire avec comme coordonnées: le nombre des abcisses choisit aléatoirement entre la position actuelle sur l'axe des abcisses à laquelle on ajoute 5, et la position actuelle sur l'axe des abcisses à laquelle on ajoute 10; et le nombre des ordonnées choisit aléatoirement dans l'intervalle de la position actuelle de la tortue sur l'axe des ordonnées à laquelle on enlève 2, et de la position actuelle de la tortue sur l'axe des ordonnées
        elif ycor()<=y-10: #on réalise la suite de la condition: si la position actuelle de la tortue sur l'axe des ordonnées, ycor(), est inférieure ou égale à la variable "y" à laquelle on enlève 10:
            goto(randint(xcor()+5,xcor()+10),randint(ycor(),ycor()+2)) #on déplace la tortue, avec le stylet baissé et donc en position d'écriture, à une position aléatoire avec comme coordonnées: le nombre des abcisses choisit aléatoirement entre la position actuelle sur l'axe des abcisses à laquelle on ajoute 5, et la position actuelle sur l'axe des abcisses à laquelle on ajoute 10; et le nombre des ordonnées choisit aléatoirement dans l'intervalle de la position actuelle de la tortue sur l'axe des ordonnées, et de la position actuelle de la tortue sur l'axe des ordonnées à laquelle on ajoute 2
        else: #on réalise la fin de la condition: sinon:
            goto(randint(xcor()+5,xcor()+10),randint(ycor()-2,ycor()+2)) #on déplace la tortue, avec le stylet baissé et donc en position d'écriture, à une position aléatoire avec comme coordonnées: le nombre des abcisses choisit aléatoirement entre la position actuelle sur l'axe des abcisses à laquelle on ajoute 5, et la position actuelle sur l'axe des abcisses à laquelle on ajoute 10; et le nombre des ordonnées choisit aléatoirement dans l'intervalle de la position actuelle de la tortue sur l'axe des ordonnées à laquelle on enlève 2, et de la position actuelle de la tortue sur l'axe des ordonnées à laquelle on ajoute 2
    goto(750,y+32) #on déplace la tortue en position d'écriture au point de coordonnées: l'axe des abcisses, x, valant 750 et l'axe des ordonéées, y, valant la position actuelle de la tortue à laquelle on ajoute 32
    y=ycor() #on assigne à la variable "y" la valeur "ycor()", qui est la position actuelle de la tortue sur l'axe des ordonnées uniquement
    while xcor()> -750: #on effectue une boucle "while" jusqu'à ce que "xcor()", donc la position actuelle de la tortue sur l'axe des abcisses, soit supérieur à -750
        if ycor()>=y+15: #on réalise la condition: si la position actuelle de la tortue sur l'axe des ordonnées, ycor(), est supérieure ou égale à la variable "y" à laquelle on ajoute 15:
            goto(randint(xcor()-10,xcor()-5),randint(ycor()-2,ycor())) #on déplace la tortue, avec le stylet baissé et donc en position d'écriture, à une position aléatoire avec comme coordonnées: le nombre des abcisses choisit aléatoirement entre la position actuelle sur l'axe des abcisses à laquelle on enlève 10, et la position actuelle sur l'axe des abcisses à laquelle on enlève 5; et le nombre des ordonnées choisit aléatoirement dans l'intervalle de la position actuelle de la tortue sur l'axe des ordonnées à laquelle on enlève 2, et de la position actuelle de la tortue sur l'axe des ordonnées
        elif ycor()<=y-10: #on réalise la suite de la condition: si la position actuelle de la tortue sur l'axe des ordonnées, ycor(), est inférieure ou égale à la variable "y" à laquelle on enlève 10:
            goto(randint(xcor()-10,xcor()-5),randint(ycor(),ycor()+2)) #on déplace la tortue, avec le stylet baissé et donc en position d'écriture, à une position aléatoire avec comme coordonnées: le nombre des abcisses choisit aléatoirement entre la position actuelle sur l'axe des abcisses à laquelle on enlève 10, et la position actuelle sur l'axe des abcisses à laquelle on enlève 5; et le nombre des ordonnées choisit aléatoirement dans l'intervalle de la position actuelle de la tortue sur l'axe des ordonnées, et de la position actuelle de la tortue sur l'axe des ordonnées à laquelle on ajoute 2
        else: #on réalise la fin de la condition: sinon:
            goto(randint(xcor()-10,xcor()-5),randint(ycor()-2,ycor()+2)) #on déplace la tortue, avec le stylet baissé et donc en position d'écriture, à une position aléatoire avec comme coordonnées: le nombre des abcisses choisit aléatoirement entre la position actuelle sur l'axe des abcisses à laquelle on enlève 10, et la position actuelle sur l'axe des abcisses à laquelle on enlève 5; et le nombre des ordonnées choisit aléatoirement dans l'intervalle de la position actuelle de la tortue sur l'axe des ordonnées à laquelle on enlève 2, et de la position actuelle de la tortue sur l'axe des ordonnées à laquelle on ajoute 2
    end_fill() #on désactive le mode remplissage, et la zone dessinée se colore de la couleur choisie
