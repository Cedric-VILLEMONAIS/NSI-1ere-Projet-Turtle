from modules import * # Importation du fichier modules.py

def palmtree(): #on crée la fonction "palmtree()" pour dessiner un palmier
    """
    Cette fonction permet de dessiner un palmier à droite du dessin
    """
    up() #on lève le stylet
    goto(750,-375) #on déplace la tortue, avec le stylet en position écriture, au point de coordonnées 750 pour l'axe des abcisses, x, et -375 pour l'axe des ordonnées, y
    if user_hour==17 or user_hour==18: #on réalise le programme suivant si l'heure choisie par l'utilisateur vaut 17 ou vaut 18
        fillcolor("#AA7B6B") #on sélectionne la couleur marron clair pour le remplissage
    elif user_hour==19 or user_hour==20: #on réalise le programme suivant si l'heure choisie par l'utilisateur vaut 19 ou vaut 20
        fillcolor("#6D4C41") #on sélectionne la couleur marron pour le remplissage
    else: #on réalise le programme suivant si l'heure choisie par l'utilisateur vaut 21
        fillcolor("#424949")  #on sélectionne la couleur marron foncé pour le remplissage
    pencolor("#1D0B04") #on met le trait du stylet en noir
    down() #on reprend le dessin
    begin_fill() #on active le mode remplissage
    setheading(90) #on oriente la tortue vers le nord, le haut du dessin
    forward(475) #on fait avancer la tortue de 475 pixels
    left(90) #on oriente la tortue de 90 degrés vers la gauche
    forward(40) #on fait avancer la tortue de 40 pixels
    while ycor() >= -375: #on entre dans la boucle "while" tant que la position de la tortue sur l'axe des ordonnées, ycor(), est supérieur ou égale à-375
        setheading(randint(200,250)) #on oriente la tortue dans une direction aléatoire du sud-ouest, plus précisément entre les nombre 200 et 250
        forward(randint(20,25)) #on fait avancer la tortue d'un nombre aléatoire entre 20 et 25
        setheading(0) #on oriente la tortue vers l'est, le côté droit du dessin
        setx(750) #on déplace la tortue uniquement sur l'axe des abcisses, x, jusqu'à ce qu'elle soit sur le point d'abcisse 750
        setx(710) #on déplace la tortue uniquement sur l'axe des abcisses, x, jusqu'à ce qu'elle soit sur le point d'abcisse 710
        ycor() #on demande la position de la tortue uniquement sur l'axe des ordonnées, y
    setx(750) #on déplace la tortue uniquement sur l'axe des abcisses, x, jusqu'à ce qu'elle soit sur le point d'abcisse 750
    end_fill() #on désactive le mode remplissage
    up() #on relève le stylet
    if user_hour==17 or user_hour==18: #on réalise le programme suivant si l'heure choisie par l'utilisateur vaut 17 ou vaut 18
        fillcolor("#229954") #on sélectionne la couleur vert clair pour le remplissage
    elif user_hour==19 or user_hour==20:  #on réalise le programme suivant si l'heure choisie par l'utilisateur vaut 19 ou vaut 20
        fillcolor("#1E8449") #on sélectionne la couleur vert pour le remplissage
    else: #on réalise le programme suivant si l'heure choisie par l'utilisateur vaut 21
        fillcolor("#196F3D") #on sélectionne la couleur vert foncé pour le remplissage
    pencolor("#145A32") #on met le trait du stylet en noir
    down() #on reprend le dessin
    begin_fill() #on active le mode remplissage
    teleport(730,100) #on déplace la tortue au point d'abcisse 730 et d'ordonnée 100 en interrompant le dessin
    setheading(130) #on oriente la tortue à 130 degrés
    forward(150) #on fait avancer la tortue de 150 pixels 
    left(30) #on oriente la tortue de 30 degrés à gauche
    forward(40) #on fait avancer la tortue de 40 pixels
    left(85) #on oriente la tortue de 85 degrés à gauche
    forward(70) #on fait avancer la tortue de 70 pixels 
    x=xcor() #on crée la variable x à laquelle on affecte le nombre des abcisses de la position actuelle de la tortue
    y=ycor() #on crée la variable y à laquelle on affecte le nombre des ordonnées de la position actuelle de la tortue
    for i in range (6): #on répète 6 fois grâce à la boucle "for"
        forward(30) #on fait avancer la tortue de 30 pixels
        teleport(x,y) #on déplace la tortue au point de coordonnée ayant pour abcisse la variable x et pour ordonnée la variable y en interrompant le dessin pour cette action uniquement
        x=x+20 #on incrémente 20 à la variable x
    goto(730,100) #on déplace la tortue au point d'abcisse 730 et à l'ordonnée 100 sans interrompre le dessin
    end_fill() #on désactive le mode remplisage 
    angle= 165 #on crée une variable angle à laquelle on affecte 165
    for i in range (2): #on répète 2 fois le programme ci-après à l'aide de la boucle "for"
        begin_fill() #on active le mode remplissage
        teleport(730,100) #on déplace la tortue au point d'abcisse 730 et à l'ordonnée 100 sans modifier le dessin
        setheading(angle) #on oriente la tortue de "angle" degrés donc du nombre constituant la variable angle
        forward(150) #on fait avancer la tortue de 150 pixels
        left(30) #on oriente la tortue de 30 degrés à gauche
        forward(40) #on fait avancer la tortue de 40 pixels
        left(75) #on oriente la tortue de 75 degres à gauche
        forward(40) #on fait avancer la tortue de 40 pixels
        x=xcor() #on crée la variable x à laquelle on affecte le nombre des abcisses de la position actuelle de la tortue
        y=ycor() #on crée la variable y à laquelle on affecte le nombre des ordonnées de la position actuelle de la tortue
        while x<700: #on répète le programme dans la boucle "while" tant que le nombre affecter à la variable x est inférieur à 700
            forward(30) #on fait avancer la tortue de 30 pixels
            teleport(x,y) #on déplace la tortue au point d'abcisse étant le nombre affecté à la variable "x"; et d'ordonnée étant le nombre affecté à la variable "y"
            x=x+20 #on incrémente 20 à la variable "x"
        goto(730,100) #on déplace la tortue au point d'abcisse 730 et d'ordonnée 100 sans interrompre le dessin
        angle=angle+30 #on incrémente 30 à la variable "angle"
        end_fill() #on désactive le mode de remplissage
