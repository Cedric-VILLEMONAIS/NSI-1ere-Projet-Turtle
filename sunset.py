from modules import * # Importation du fichier modules.py

def sunset() : #on crée une fonction "sunset()" pour dessiner un soleil différent en fonction de l'heure choisie par l'utilisateur pour faire un soleil couchant plus ou moins prononcé en fonction de l'heure
    """
    Cette fonction permet de dessiner un soleil ainsi que de lui attribuer une couleur et de le déplacer en fonction de l'heure choisie précédemment
    """   
    up() #on lève le stylet
    x=0 #on crée une variable "x" à laquelle on affecte 0
    y=0 #on crée une variable "y" à laquelle on affecte 0
    seth(90) #on oriente la tortue vers le nord (le haut du dessin)
    #réalisation du premier soleil
    if 17>=user_hour<18: #on réalise le programme suivant si l'heure choisie par l'utilisateur est entre 17 inclus et 18 non inclus
        x=-80 #on affecte -80 à la variable "x"
        goto(x,y) #on déplace la tortue tout en modifiant le dessin au point d'abcisse de la valeur de la variable "x" et d'ordonnée de la valeur de la variable "y"
        x=xcor() #on change une nouvelle fois la variable "x" en affectant la valeur de la position actuelle de la tortue sur l'axe des abcisses uniquement 
        down() #on met le stylet en position d'écriture
        fillcolor("#FCFE43") #on sélectionne la couleur jaune clair pour le mode remplissage
        begin_fill() #on active le mode remplissage
        color("#FCFE43") #on sélectionne la couleur jaune clair pour les traits
        circle(100,180) #on dessine un demi-cercle de rayon 100 pixels et donc d'angle 180 degrés
    #réalisation du deuxième soleil
    elif 18>=user_hour<19: #on réalise le programme suivant si l'heure choisie par l'utilisateur est entre 18 inclus et 19 non inclus
        x=-200 #on affecte -200 à la variable "x"
        goto(x,y) #on déplace la tortue tout en modifiant le dessin au point d'abcisse de la valeur de la variable "x" et d'ordonnée de la valeur de la variable "y"
        x=xcor() #on change une nouvelle fois la variable "x" en affectant la valeur de la position actuelle de la tortue sur l'axe des abcisses uniquement 
        down() #on met le stylet en position d'écriture
        fillcolor("#FFD668") #on sélectionne la couleur jaune pour le mode remplissage
        begin_fill() #on active le mode remplissage
        color("#FFD668") #on sélectionne la couleur jaune pour les traits
        circle(70,180) #on dessine un demi-cercle de rayon 70 pixels et donc d'angle 180 degrés
    #réalisation du troisième soleil
    elif 19>=user_hour<20: #on réalise le programme suivant si l'heure choisie par l'utilisateur est entre 19 inclus et 20 non inclus
        x=-300 #on affecte -300 à la variable "x"
        goto(x,y) #on déplace la tortue tout en modifiant le dessin au point d'abcisse de la valeur de la variable "x" et d'ordonnée de la valeur de la variable "y"
        x=xcor() #on change une nouvelle fois la variable "x" en affectant la valeur de la position actuelle de la tortue sur l'axe des abcisses uniquement 
        down() #on met le stylet en position d'écriture
        fillcolor("#FFCF68") #on sélectionne la couleur jaune foncé pour le mode remplissage
        begin_fill() #on active le mode remplissage
        color("#FFCF68") #on sélectionne la couleur jaune foncé pour les traits
        circle(40,180) #on dessine un demi-cercle de rayon 40 pixels et donc d'angle 180 degrés
    #réalisation du quatrième soleil
    elif 20>=user_hour<21: #on réalise le programme suivant si l'heure choisie par l'utilisateur est entre 20 inclus et 21 non inclus
        x=-400 #on affecte -400 à la variable "x"
        goto(x,y) #on déplace la tortue tout en modifiant le dessin au point d'abcisse de la valeur de la variable "x" et d'ordonnée de la valeur de la variable "y"
        x=xcor() #on change une nouvelle fois la variable "x" en affectant la valeur de la position actuelle de la tortue sur l'axe des abcisses uniquement 
        down() #on met le stylet en position d'écriture
        fillcolor("#FFBF68") #on sélectionne la couleur jaune-orangé pour le mode remplissage
        begin_fill() #on active le mode remplissage
        color("#FFBF68") #on sélectionne la couleur jaune-orangé pour les traits
        circle(20,180) #on dessine un demi-cercle de rayon 20 pixels et donc d'angle 180 degrés
    #réalisation du dernier soleil
    else: #on réalise le programme suivant si l'heure choisie par l'utilisateur vaut 21
        x=-500 #on affecte -500 à la variable "x"
        goto(x,y) #on déplace la tortue tout en modifiant le dessin au point d'abcisse de la valeur de la variable "x" et d'ordonnée de la valeur de la variable "y"
        x=xcor() #on met le stylet en position d'écriture
        down() #on met le stylet en position d'écriture
        fillcolor("#FF9668") #on sélectionne la couleur rouge-orangé pour le mode remplissage
        begin_fill() #on active le mode remplissage
        color("#FF9668") #on sélectionne la couleur rouge-orangé pour les traits
        circle(10,180) #on dessine un demi-cercle de rayon 10 pixels et donc d'angle 180 degrés
    goto(x,0) #on déplace la tortue tout en modifiant le dessin au point d'abcisse de la valeur de la variable "x" et d'ordonnée 0
    end_fill() #on désactive le mode remplissage
        
       
