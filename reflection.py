from modules import *

def reflection(): #on crée la fonction "reflection()" pour dessiner la réflection du soleil sur la mer
    """
    Cette fonction permet de dessiner le reflet du soleil sur l'eau
    """
    down() #on baisse le stylet pour qu'il puisse modifier le dessin
    if 17>=user_hour<18: #on réalise le programme suivant si l'heure choisie par l'utilisateur est entre 17 inclus et 18 non inclus
        teleport(-230,-3) #on déplace la tortue au point d'abcisse -230 et d'ordonnée -3 sans modifier le dessin
        color("#FCFE43") #on sélectionne la couleur jaune clair 
        y=-170 #on crée une variable "y" à laquelle on affecte la valeur -170
        plus=100 #on crée la variable "plus" à laquelle on affecte la valeur 100
    elif 18>=user_hour<19: #on réalise le programme suivant si l'heure choisie par l'utilisateur est entre 18 inclus et 19 non inclus
        teleport(-305,-3) #on déplace la tortue au point d'abcisse -305 et d'ordonnée -3 sans modifier le dessin
        color("#FFD668") #on sélectionne la couleur jaune orangé clair
        y=-140 #on crée une variable "y" à laquelle on affecte la valeur -140
        plus=70 #on crée la variable "plus" à laquelle on affecte la valeur 70
    elif 19>=user_hour<20: #on réalise le programme suivant si l'heure choisie par l'utilisateur est entre 19 inclus et 20 non inclus
        teleport(-360,-3) #on déplace la tortue au point d'abcisse -365 et d'ordonnée -3 sans modifier le dessin
        color("#FFCF68")  #on sélectionne la couleur jaune orangé 
        y=-100 #on crée une variable "y" à laquelle on affecte la valeur -100
        plus=40 #on crée la variable "plus" à laquelle on affecte la valeur 40
    elif 20>=user_hour<21: #on réalise le programme suivant si l'heure choisie par l'utilisateur est entre 20 inclus et 21 non inclus
        teleport(-430,-3) #on déplace la tortue au point d'abcisse -430 et d'ordonnée -3 sans modifier le dessin
        color("#FFBF68") #on sélectionne la couleur orange clair
        y=-50 #on crée une variable "y" à laquelle on affecte la valeur -50
        plus=20 #on crée la variable "plus" à laquelle on affecte la valeur 20
    else: #on réalise le programme suivant si l'heure choisie par l'utilisateur vaut 21
        teleport(-512,-3) #on déplace la tortue au point d'abcisse -512 et d'ordonnée -3 sans modifier le dessin
        color("#FF9668")  #on sélectionne la couleur rouge-orange
        y=-30 #on crée une variable "y" à laquelle on affecte la valeur -30
        plus=5 #on crée la variable "plus" à laquelle on affecte la valeur 5
    x=xcor() #on crée la variable "x" à laquelle on affecte la position actuelle sur l'axe des abcisses uniquement de la tortue
    begin_fill() #on active le mode remplissage 
    #on dessine une première ligne avec des directions aléatoires, partant du soleil et allant vers le bas, tout en prenant garde à ce que le trait ne choisisse pas une position aléatoire trop éloignée
    while ycor()>y: #on effectue le programme dans la boucle "while" tant que la position actuelle sur l'axe des ordonnées, y, de la tortue est strictement supérieur à la variable y 
        if xcor()>=x+5: #on réalise le programme suivant si la position sur l'axe des abcisses, x, de la tortue est supérieur ou égale à la variable "x" à laquelle on incrémente 5
            goto(randint(xcor(),xcor()+2),randint(ycor()-6,ycor()-4)) #on déplace la tortue en dessinant au point d'abcisse aléatoire entre les valeurs de la position actuelle de la tortue sur l'axe des abcisses,x, et de la position actuelle de la tortue sur l'axe des abcises à laquelle on ajoute 2; et d'ordonnée aléatoire entre les valeurs de la position actuelle de la tortue sur l'axe des ordonnées, y, à laquelle on enlève 6, et de la position actuelle sur l'axe des ordonnées à laquelle on enlève 4 
        elif xcor()<=x-5: #on réalise le programme suivant si la position sur l'axe des abcisses, x, de la tortue est inférieur ou égale à la variable "x" à laquelle on enlève 5
            goto(randint(xcor()-2,xcor()),randint(ycor()-6,ycor()-4)) #on déplace la tortue en dessinant au point d'abcisse aléatoire entre les valeurs de la position actuelle de la tortue sur l'axe des abcisses,x, à laquelle on enlève 2 et de la position actuelle de la tortue sur l'axe des abcises; et d'ordonnée aléatoire entre les valeurs de la position actuelle de la tortue sur l'axe des ordonnées, y, à laquelle on enlève 6, et de la position actuelle sur l'axe des ordonnées à laquelle on enlève 4 
        else: #on réalise le programme suivant si les conditions précédentes ne sont pas respectées
            goto(randint(xcor()-2,xcor()+2),randint(ycor()-6,ycor()-4)) #on déplace la tortue en dessinant au point d'abcisse aléatoire entre les valeurs de la position actuelle de la tortue sur l'axe des abcisses,x, à laquelle on enlève 2 et de la position actuelle de la tortue sur l'axe des abcises à laquelle on ajoute 2; et d'ordonnée aléatoire entre les valeurs de la position actuelle de la tortue sur l'axe des ordonnées, y, à laquelle on enlève 6, et de la position actuelle sur l'axe des ordonnées à laquelle on enlève 4 
    y1=ycor() #on crée une fonction "y1" à laquelle on affecte la position actuelle de la tortue sur l'axe des ordonnées
    x1=xcor() #on crée une fonction "x1" à laquelle on affecte le position actuelle de la tortue sur l'axe des abcisses
    teleport(x,-3) #on déplace la tortue au point d'abcisse de la valeur présente dans la variable "x" et d'ordonnée -3 sans modifier le dessin
    goto(x+plus,-3) #on déplace la tortue en traçant un trait au point de la valeur présente dans la variable "x" à laquelle on incrémente 3, et d'ordonnée -3
    x2=xcor() #on crée la variable "x2" à laquelle on affecte la position actuelle de la tortue sur l'axe des abcisses 
    #on dessine une seconde ligne avec des directions aléatoires, partant du soleil et allant vers le bas, tout en prenant garde à ce que le trait ne choisisse pas une position aléatoire trop éloignée
    while ycor()>y: #on effectue le programme dans la boucle "while" tant que la position actuelle sur l'axe des ordonnées, y, de la tortue est strictement supérieur à la variable y 
        if xcor()>=x2+5: #on réalise le programme suivant si la position sur l'axe des abcisses, x, de la tortue est supérieur ou égale à la variable "x2" à laquelle on incrémente 5
            goto(randint(xcor()-2,xcor()),randint(ycor()-6,ycor()-4)) #on déplace la tortue en dessinant au point d'abcisse aléatoire entre les valeurs de la position actuelle de la tortue sur l'axe des abcisses,x, à laquelle on enlève 2 et de la position actuelle de la tortue sur l'axe des abcises; et d'ordonnée aléatoire entre les valeurs de la position actuelle de la tortue sur l'axe des ordonnées, y, à laquelle on enlève 6, et de la position actuelle sur l'axe des ordonnées à laquelle on enlève 4 
        elif xcor()<=x2-5: #on réalise le programme suivant si la position sur l'axe des abcisses, x, de la tortue est inférieur ou égale à la variable "x2" à laquelle on enlève 5
            goto(randint(xcor(),xcor()+2),randint(ycor()-6,ycor()-4)) #on déplace la tortue en dessinant au point d'abcisse aléatoire entre les valeurs de la position actuelle de la tortue sur l'axe des abcisses,x, et de la position actuelle de la tortue sur l'axe des abcises à laquelle on ajoute 2; et d'ordonnée aléatoire entre les valeurs de la position actuelle de la tortue sur l'axe des ordonnées, y, à laquelle on enlève 6, et de la position actuelle sur l'axe des ordonnées à laquelle on enlève 4 
        else: #on réalise le programme suivant si les conditions précédentes ne sont pas respectées
            goto(randint(xcor()-2,xcor()+2),randint(ycor()-6,ycor()-4)) #on déplace la tortue en dessinant au point d'abcisse aléatoire entre les valeurs de la position actuelle de la tortue sur l'axe des abcisses,x, à laquelle on enlève 2 et de la position actuelle de la tortue sur l'axe des abcises à laquelle on ajoute 2; et d'ordonnée aléatoire entre les valeurs de la position actuelle de la tortue sur l'axe des ordonnées, y, à laquelle on enlève 6, et de la position actuelle sur l'axe des ordonnées à laquelle on enlève 4 
    goto(x1,y1) #on déplace la tortue tout en modifiant le dessin au point d'abcisse de la valeur de la variable "x1" et d'ordonnée de la valeur de la variable "y1"
    end_fill() #on désactive le mode de remplissage
