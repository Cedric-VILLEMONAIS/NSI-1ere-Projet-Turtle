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


if user_hour==20 or user_hour==21 : star(-750,750,0,375)
sunset()

if user_hour==17 or user_hour==18 : sea(-750,750,-300,0)
elif user_hour==19 or user_hour==20 : sea(-750,750,-250,0)
elif user_hour==21 : sea(-750,750,-200,0)

if user_hour==17 or user_hour==18 : beach(-750,750,-375,-300)
elif user_hour==19 or user_hour==20 : beach(-750,750,-375,-250)
elif user_hour==21 : beach(-750,750,-375,-200)

if user_cloud==1 : cloud(-750,750,0,375)

if user_hour==17 or user_hour==18 : fish(-750,750,-300,0)
elif user_hour==19 or user_hour==20 : fish(-750,750,-250,0)
elif user_hour==21 : fish(-750,750,-200,0)

if user_hour==17 or user_hour==18 : waves(-750,750,-300,0)
elif user_hour==19 or user_hour==20 : waves(-750,750,-250,0)
elif user_hour==21 : waves(-750,750,-200,0)
# reflection()

palmtree()
bird(-750,750,0,375)


ht()

done()
