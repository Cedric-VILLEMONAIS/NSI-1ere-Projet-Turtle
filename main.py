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
# reflection()



bird(-750,750,0,375)


ht()

done()
