#on importe des différents fichiers les fonctions suivantes
from modules import *
from cloud import *
from star import *
from sunset import *
from sea import *
from gradient import *
from reflection import *
from waves import *
from fish import *
from bird import *
from beach import *
from palmtree import *
from ecume import *

#on fait apparaître les étoiles en fonction de l'heure de la journée, préalablement choisie par l'utilisateur
if user_hour==20 or user_hour==21 : star(-750,750,0,375)
  
sunset()#on fait apparaître le soleil

#on fait apparaître la mer en fonction de la marée, c'est-à-dire, en fonction de l'heure de la journée
if user_hour==17 or user_hour==18 : sea(-750,750,-300,0)
elif user_hour==19 or user_hour==20 : sea(-750,750,-250,0)
elif user_hour==21 : sea(-750,750,-200,0)

#on fait apparaître la plage en fonction de la marée, c'est-à-dire, en fonction de l'heure de la journée
if user_hour==17 or user_hour==18 : beach(-750,750,-375,-300)
elif user_hour==19 or user_hour==20 : beach(-750,750,-375,-250)
elif user_hour==21 : beach(-750,750,-375,-200)
  
ecume() #on fait apparaître l'écume
reflection() #on fait apparaître la réflection du soleil sur l'eau

#on fait apparaître les nuages en fonction de la réponse de l'utilisateur
if user_cloud==1 : cloud(-750,750,0,375)

#on fait apparaître les poissons en fonction de la marée, c'est-à-dire, en fonction de l'heure de la journée
if user_hour==17 or user_hour==18 : fish(-750,750,-270,-10)
elif user_hour==19 or user_hour==20 : fish(-750,750,-230,-10)
elif user_hour==21 : fish(-750,750,-180,-10)

#on fait apparaître les vagues en fonction de la marée, c'est-à-dire, en fonction de l'heure de la journée
if user_hour==17 or user_hour==18 : waves(-750,750,-270,-10)
elif user_hour==19 or user_hour==20 : waves(-750,750,-230,-10)
elif user_hour==21 : waves(-750,750,-180,-10)

palmtree() #on fait apparaître le palmier
bird(-750,750,0,375) #on fait apparaître l'oiseau


ht() #on fait disparaître la tortue

done() #on arrête le dessin
