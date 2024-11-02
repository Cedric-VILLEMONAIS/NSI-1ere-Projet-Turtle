from modules import *

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