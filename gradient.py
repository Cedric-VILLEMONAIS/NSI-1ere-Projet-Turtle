from modules import *

#attention la fonction ne fonctionne pas
def gradient(): # on crée une fonction"gradient" pour faire un dégradé
    if user_hour == 17 or user_hour == 18: #on réalise le programme suivant si l'heure choisie par l'utilisateur vaut 17 ou vaut 18
        color_start = "#4563EB" #on attribue la couleur bleu foncé à la variable "color_start"
        color_end = "#3A87C4" #on attribue la couleur bleu clair à la variable "color_start"
    elif user_hour == 19 or user_hour==20: #on réalise le programme suivant si l'heure choisie par l'utilisateur vaut 19 ou vaut 20
        color_start = "#3750C1" #on attribue la couleur d'une teinte de bleu foncé à la variable "color_start"
        color_end = "#3A87C4" #on attribue la couleur d'une teinte de bleu clair à la variable "color_start"
    else: #on réalise le programme suivant si l'heure choisie par l'utilisateur vaut 21
        color_start = "#293C8F" #on attribue la couleur d'une teinte de bleu foncé à la variable "color_start"
        color_end = "#29628F" #on attribue la couleur d'une teinte de bleu clair à la variable "color_start"
    number=0 #on crée une variable "number" et on your affecte 0
    for i in range(number<2): #on fait la boucle 
        fillcolor(color_start+color_end) #on sélectionne les deux couleurs (start et end) pour le mode remplissage
        number=number+1 #on incrémente 1 à la variable number
    begin_fill #on active le mode remplissage
    up() #on lève le stylet
    goto(-750,0) #on déplace la tortue au point d'abcisse -750 et d'ordonnée 0
    down() # on pose le stylet
    #la fonction n'est pas terminée
    end_fill() #désactiver le mode remplissage
