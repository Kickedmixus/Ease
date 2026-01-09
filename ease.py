#EASE

import math

def easeOut(easetype,start,end,length,reverse=False):
    graph = []

    #each if/elif for one function

    if easetype == "linear":

        for i in range(length):
            graph.append(start+((end-start)*(i/(length-1))))

    elif easetype == "sine":

        for i in range(length):
            graph.append(start+(end-start)*math.sin(i/(length-1)*math.pi/2))

    elif easetype == "quad" or easetype == "quadratic":

        for i in range(length):
            graph.append(start+(end-start)*(1-(1-i/(length-1))**2))

    elif easetype == "cube" or easetype == "cubic":

        for i in range(length):
            graph.append(start+(end-start)*(1-(1-i/(length-1))**3))

    elif easetype == "quart" or easetype == "quartic":

        for i in range(length):
            graph.append(start+(end-start)*(1-(1-i/(length-1))**4))

    elif easetype == "quint" or easetype == "quintic":

        for i in range(length):
            graph.append(start+(end-start)*(1-(1-i/(length-1))**5))

    if reverse:
        return graph[::-1]
    else:
        return graph

#after this point only reformating easeOut() to other functions

def easeIn(easetype, start, end, length, reverse=False):

    easeout = easeOut(easetype,start,end,length,reverse)[::-1]
    graph = []

    for i in range(len(easeout)):
        graph.append(start+(end-easeout[i]))

    return graph

def easeInOut(easetype,start,end,length,swap=False):
    
    if swap:
        easein = easeIn(easetype,start+((end-start)/2),end,length//2)
        easeout = easeOut(easetype,start,start+((end-start)/2),length-length//2)
        return easeout+easein
    else:
        easein = easeIn(easetype,start,start+(end-start)/2,length-length//2)
        easeout = easeOut(easetype,start+(end-start)/2,end,length//2)
        return easein+easeout


#lenght