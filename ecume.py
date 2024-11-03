from modules import *

def ecume():
    """
    Cette fonction permet de dessiner de l'écume
    """
    color("#F0F3F4")
    begin_fill()
    if user_hour==17 or user_hour==18 :
        teleport(-750,-320)
    elif user_hour==19 or user_hour==20 :
        teleport(-750,-270)
    else:
        teleport(-750,-220)
    y=ycor()
    while xcor()<750:
        if ycor()>=y+15:
            goto(randint(xcor()+5,xcor()+10),randint(ycor()-2,ycor()))
        elif ycor()<=y-10:
            goto(randint(xcor()+5,xcor()+10),randint(ycor(),ycor()+2))
        else:
            goto(randint(xcor()+5,xcor()+10),randint(ycor()-2,ycor()+2))
    goto(750,y+32)
    y=ycor()
    while xcor()> -750:
        if ycor()>=y+15:
            goto(randint(xcor()-10,xcor()-5),randint(ycor()-2,ycor()))
        elif ycor()<=y-10:
            goto(randint(xcor()-10,xcor()-5),randint(ycor(),ycor()+2))
        else:
            goto(randint(xcor()-10,xcor()-5),randint(ycor()-2,ycor()+2))
    end_fill()
