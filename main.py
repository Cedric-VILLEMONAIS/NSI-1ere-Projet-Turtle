# Importation des modules
from turtle import *

# Demander à l'utilisateur à l'aide de la fonction numinput : 
# l'heure, le nombre de nuages ainsi que la taille des nuages et enregistrer sa réponse dans une variable
# minval et maxval permettent de définir les valeurs minimales et maximales autorisées
# On utilise round pour arrondir la valeur obtenue si l'utilisateur à donné une heure à virgule
user_hour = round(numinput("Heure", "Quelle heure entre 17 et 21 h ?", minval=17, maxval=21))
user_cloud = round(numinput("Nuages", "Quel est la quantité de nuages de 0 (peu de nuages) à 5 (énormément de nuages)", minval=0, maxval=5))
user_cloud_size = round(numinput("Taille des nuages", "Quel est la taille des nuages entre 0 (nuages fins) et 5 (gros nuages)", minval=0, maxval=5))

# Configurer la fenêtre d'affichage
title("NSI 1ere Projet Turtle par Nora TERRAL et Cédric VILLEMONAIS")
setup(width=1820, height=980, startx=0, starty=0)
screensize(1500, 750)

background_color = [17, "#caf0f8", 18, "#90e0ef", 19, "#00b4d8", 20, "#0077b6", 21, "#03045e"]
bgcolor(background_color[(background_color.index(user_hour))+1])
# hideturtle()






def sunset() :
    # penup()
    goto(-750,375)
    color(yellow)
    circle(187.5,180)
    fillcolor(yellow)
    begin_fill()

done()
