from modules import *

def reflection(): #on crée la fonction "reflection" pour dessiner la réflection du soleil sur la mer
    """
    Cette fonction permet de dessiner le reflet du soleil sur l'eau
    """
    down() #on baisse le stylet pour qu'il puisse modifier le dessin
    if 17>=user_hour<18: #on effectue la condition
        teleport(-230,-3)
        color("#FCFE43")
        y=-170
        plus=100
    elif 18>=user_hour<19:
        teleport(-305,-3)
        color("#FFD668")
        y=-140
        plus=70
    elif 19>=user_hour<20:
        teleport(-360,-3)
        color("#FFCF68")
        y=-100
        plus=40
    elif 20>=user_hour<21:
        teleport(-430,-3)
        color("#FFBF68")
        y=-50
        plus=20
    else:
        teleport(-512,-3)
        color("#FF9668")
        y=-30
        plus=5
    x=xcor()
    begin_fill()
    while ycor()>y:
        if xcor()>=x+5:
            goto(randint(xcor(),xcor()+2),randint(ycor()-6,ycor()-4))
        elif xcor()<=x-5:
            goto(randint(xcor()-2,xcor()),randint(ycor()-6,ycor()-4))
        else:
            goto(randint(xcor()-2,xcor()+2),randint(ycor()-6,ycor()-4))
    y1=ycor()
    x1=xcor()
    teleport(x,-3)
    goto(x+plus,-3)
    x2=xcor()
    while ycor()>y:
        if xcor()>=x2+5:
            goto(randint(xcor()-2,xcor()),randint(ycor()-6,ycor()-4))
        elif xcor()<=x2-5:
            goto(randint(xcor(),xcor()+2),randint(ycor()-6,ycor()-4))
        else:
            goto(randint(xcor()-2,xcor()+2),randint(ycor()-6,ycor()-4))
    goto(x1,y1)
    end_fill()
