# Importation des modules
from turtle import *
from cloud import *

# Demander à l'utilisateur à l'aide de la fonction numinput : 
# l'heure et est-ce qu'il y a des nuages et enregistrer sa réponse dans une variable
# minval et maxval permettent de définir les valeurs minimales et maximales autorisées
# On utilise round pour arrondir la valeur obtenue si l'utilisateur à donné une heure à virgule
user_hour = round(numinput("Heure", "Quelle heure entre 17 et 21 h ?", minval=17, maxval=21))
user_cloud = round(numinput("Nuages", "Est-ce que le temps est nuageux (0 non et 1 oui)?", minval=0, maxval=1))

# Configurer la fenêtre d'affichage
title("NSI 1ere Projet Turtle par Nora TERRAL et Cédric VILLEMONAIS")
setup(width=1820, height=980, startx=0, starty=0)
screensize(1500, 750)
background_color = [17, "#caf0f8", 18, "#90e0ef", 19, "#00b4d8", 20, "#0077b6", 21, "#03045e"]
bgcolor(background_color[(background_color.index(user_hour))+1])
# hideturtle()


if user_cloud==1 : cloud()


def sunset() :
    """
    Cette fonction permet de dessiner un soleil et de lui attribuer une couleur en fonction de l'heure choisie précédemment
    """   
    up()
    goto(-200,100)
    down()
    seth(90)
    if 17>=user_hour<18:
        fillcolor("#FCFE43")
        begin_fill()
        color("#FCFE43")
        circle(150,180)
        end_fill()
    elif 18>=user_hour<19:
        fillcolor("#FFD668")
        begin_fill()
        color("#FFD668")
        circle(100,180)
        end_fill()
    elif 19>=user_hour<20:
        fillcolor("#FFCF68")
        begin_fill()
        color("#FFCF68")
        circle(50,180)
        end_fill()
    elif 20>=user_hour<21:
        fillcolor("#FFBF68")
        begin_fill()
        color("#FFBF68")
        circle(30,180)
        end_fill()
    else:
        fillcolor("#FF9668")
        begin_fill()
        color("#FF9668")
        circle(20,180)
        end_fill()
   
    

sunset()

done()
