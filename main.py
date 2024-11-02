# Importation des modules
from turtle import *
from random import randint
from tkinter import messagebox

# Demander à l'utilisateur à l'aide de la fonction numinput : 
# l'heure et est-ce qu'il y a des nuages et enregistrer sa réponse dans une variable
# minval et maxval permettent de définir les valeurs minimales et maximales autorisées
# On utilise round pour arrondir la valeur obtenue si l'utilisateur à donné une heure à virgule

messagebox.showwarning(title="Attention", message="Pour un fonctionnement optimal veuillez utiliser une résolution d'affichage suppérieure ou égale à 1920 * 1080 pixels avec une mise à l'échelle de 100%")
user_hour = round(numinput("Heure", "Quelle heure entre 17 et 21 h ?", minval=17, maxval=21))
user_cloud = round(numinput("Nuages", "Est-ce que le temps est nuageux (0 non et 1 oui)?", minval=0, maxval=1))

# Configurer la fenêtre d'affichage
title("NSI 1ere Projet Turtle par Nora TERRAL et Cédric VILLEMONAIS")
setup(width=1820, height=980, startx=0, starty=0)
screensize(1500, 750)
background_color = [17, "#caf0f8", 18, "#90e0ef", 19, "#00b4d8", 20, "#0077b6", 21, "#03045e"]
bgcolor(background_color[(background_color.index(user_hour))+1])
hideturtle()
speed(0)
def teleport(x,y):
    penup()
    goto(x,y)
    pendown()

def star(x_start, x_end, y_start, y_end) :
    """
    Cette fonction permet de créer des étoiles
    def factorielle(n):
    :param x_start: int
    :param x_end: int
    :param y_start: int
    :param y_end: int
    """
    number = randint(1,50)
    penup()
    for i in range(number) :
        teleport(randint(x_start, x_end), randint(y_start, y_end))
        dot(4, "#ffffff")

def cloud(x_start, x_end, y_start, y_end) :
    """
    cette fonction permet de faire apparaître des nuages 
    :param x_start: int
    :param x_end: int
    :param y_start: int
    :param y_end: int
    """
    setheading(0)
    number = randint(1,10)
    pendown()
    color("#cacaca")
    for i in range(number):
        width = randint(1,3)
        teleport(randint(x_start, x_end), randint(y_start, y_end))
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
    Cette fonction permet de dessiner un soleil ainsi que de lui attribuer une couleur et de le déplacer en fonction de l'heure choisie précédemment
    """   
    up()
    x=0
    y=100
    seth(90)
    if 17>=user_hour<18:
        x=-80
        goto(x,y)
        down()
        fillcolor("#FCFE43")
        begin_fill()
        color("#FCFE43")
        circle(100,180)
        end_fill()
    elif 18>=user_hour<19:
        x=-0
        goto(x,y)
        down()
        fillcolor("#FFD668")
        begin_fill()
        color("#FFD668")
        circle(70,180)
        end_fill()
    elif 19>=user_hour<20:
        x=-300
        goto(x,y)
        down()
        fillcolor("#FFCF68")
        begin_fill()
        color("#FFCF68")
        circle(40,180)
        end_fill()
    elif 20>=user_hour<21:
        x=-400
        goto(x,y)
        down()
        fillcolor("#FFBF68")
        begin_fill()
        color("#FFBF68")
        circle(20,180)
        end_fill()
    else:
        x=-500
        goto(x,y)
        down()
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

def gradient(): # fonctionne pas -> à bidouiller
    if user_hour == 17 or user_hour == 18:
        color_start = "#4563EB"
        color_end = "#3A87C4"
    elif user_hour == 19 or user_hour==20:
        color_start = "#3750C1"
        color_end = "#3A87C4"
    else:
        color_start = "#293C8F"
        color_end = "#29628F"
    for i in range(number<2):
        fillcolor(color_start+color_end)
        number=number+1
    begin_fill
    up()
    goto(-750,0)
    down()
    width,height = 1500,-375
    up()
    end_fill
    
def reflection(x_start, x_end, y_start, y_end):
    """
    Cette fonction permet de représenter le reflet du soleil sur la mer
    :param x_start: int
    :param x_end: int
    :param y_start: int
    :param y_end: int
    """
    up()
    goto(x,y)
    down()
    color("") # créer variable soleil couleur pour la mettre la
    fillcolor("")

def waves(x_start, x_end, y_start, y_end): #marche paaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaas
    """
    Cette fonction permet de créer des vagues
    def factorielle(n):
    :param x_start: int
    :param x_end: int
    :param y_start: int
    :param y_end: int
    """
    number = randint(20,50)
    penup()
    for i in range(number) :
        width = randint(1,3)
        up()
        teleport(randint(x_start, x_end), randint(y_start, y_end))
        color("#154360")
        down()
        setheading(135)
        forward(6)
        circle(10,180)
        setheading(205)
        forward(6)

def fish(x_start, x_end, y_start, y_end):
    """
    Cette fonction permet de créer des poissons
    def factorielle(n):
    :param x_start: int
    :param x_end: int
    :param y_start: int
    :param y_end: int
    """
    number = randint(5,10)
    penup()
    for i in range(number) :
        width = randint(1,3)
        up()
        teleport(randint(x_start, x_end), randint(y_start, y_end))
        color("#424949")
        down()
        setheading(randint(0,360))
        dot(randint(4,6))
        right(60)
        forward(3)
        left(60)
        forward(3)
        left(60)
        forward(3)

if user_hour==20 or user_hour==21 : star(-750,750,0,375)
sunset()
sea()
if user_cloud==1 : cloud(-750,750,0,375)

if user_hour==17 or user_hour==18 : fish(-750,750,-300,0)
if user_hour==19 or user_hour==20 : fish(-750,750,-250,0)
if user_hour==21 : fish(-750,750,-200,0)

if user_hour==17 or user_hour==18 : waves(-750,750,-300,0)
if user_hour==19 or user_hour==20 : waves(-750,750,-250,0)
if user_hour==21 : waves(-750,750,-200,0)
reflection()

ht()

done()
