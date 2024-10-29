# Importation des modules
from turtle import *
from random import randint
from tkinter import messagebox

# Demander à l'utilisateur à l'aide de la fonction numinput : 
# l'heure et est-ce qu'il y a des nuages et enregistrer sa réponse dans une variable
# minval et maxval permettent de définir les valeurs minimales et maximales autorisées
# On utilise round pour arrondir la valeur obtenue si l'utilisateur à donné une heure à virgule

messagebox.showwarning(title="Attention", message="Pour un fonctionnement optimal veuillez utiliser une résolution d'affichage suppérieure ou égale à 1920 * 1080 pixels avec une mise à l'échelle de 100%")

# user_hour = round(numinput("Heure", "Quelle heure entre 17 et 21 h ?", minval=17, maxval=21))
# user_cloud = round(numinput("Nuages", "Est-ce que le temps est nuageux (0 non et 1 oui)?", minval=0, maxval=1))

# For developpement :
user_hour = 21
user_cloud = 1

# Configurer la fenêtre d'affichage
title("NSI 1ere Projet Turtle par Nora TERRAL et Cédric VILLEMONAIS")
setup(width=1820, height=980, startx=0, starty=0)
screensize(1500, 750)
background_color = [17, "#caf0f8", 18, "#90e0ef", 19, "#00b4d8", 20, "#0077b6", 21, "#03045e"]
bgcolor(background_color[(background_color.index(user_hour))+1])
# hideturtle()




def cloud() :
    number = randint(1,10)
    # hideurtle()
    pendown()
    color("#cacaca")
    for i in range(number):
        width = randint(1,5)
        teleport(randint(-750, 750), randint(0,375))
        origin = pos()
        begin_fill()
        circle(7.5*width,210)
        right(140)
        while pos()[1] > origin[1] :
            circle(randint(5,9)*width,200)
            right(190)
        goto(origin)
        end_fill()
        setheading(0)

def sunset() :
    """
    Cette fonction permet de dessiner un soleil et de lui attribuer une couleur en fonction de l'heure choisie précédemment
    """   
    up()
    goto(-200,200)
    down()
    seth(90)
    if 17>=user_hour<18:
        fillcolor("#FCFE43")
        begin_fill()
        color("#FCFE43")
        circle(100,180)
        end_fill()
    elif 18>=user_hour<19:
        fillcolor("#FFD668")
        begin_fill()
        color("#FFD668")
        circle(70,180)
        end_fill()
    elif 19>=user_hour<20:
        fillcolor("#FFCF68")
        begin_fill()
        color("#FFCF68")
        circle(40,180)
        end_fill()
    elif 20>=user_hour<21:
        fillcolor("#FFBF68")
        begin_fill()
        color("#FFBF68")
        circle(20,180)
        end_fill()
    else:
        fillcolor("#FF9668")
        begin_fill()
        color("#FF9668")
        circle(10,180)
        end_fill()
        
def sea():
    """
    Cette fonction permet de dessiner la mer
    """
    up()
    goto(-750,200) #pointer vers le bas
    down()
    
def reflection():
    """
    Cette fonction permet de représenter le reflet du soleil sur la mer
    """
    up()
    goto(-200,200)
    down()
   
    
if user_cloud==1 : cloud()
sunset()
sea()
reflection()

ht()

done()
