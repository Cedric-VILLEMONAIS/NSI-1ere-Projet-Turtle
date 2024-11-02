from modules import *

def sunset() :
    """
    Cette fonction permet de dessiner un soleil ainsi que de lui attribuer une couleur et de le déplacer en fonction de l'heure choisie précédemment
    """   
    up()
    x=0
    y=0
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
        
