from modules import *

def beach(x_start, x_end, y_start, y_end) :
    """
    cette fonction permet de faire apparaître la plage
    :param x_start: int
    :param x_end: int
    :param y_start: int
    :param y_end: int
    """
    teleport(x_start,y_start)
    color("#eabb75")
    fillcolor("#eabb75")
    begin_fill()
    goto(x_end, y_start)
    goto(x_end,y_end)
    goto(x_start,y_end)
    goto(x_start, y_start)
    end_fill()