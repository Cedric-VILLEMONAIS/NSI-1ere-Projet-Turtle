# Importation des modules
from turtle import *
from random import randint
from tkinter import messagebox
from time import sleep

def teleport(x,y):
    penup()
    goto(x,y)
    pendown()

def init() :
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
    
    return user_hour, user_cloud

init_var = init()
user_hour, user_cloud = init_var[0], init_var[1]

color("#000000")
pensize(1)
teleport(-750,375)
goto(750,375)
goto(750,-375)
goto(-750,-375)