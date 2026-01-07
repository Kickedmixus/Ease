#EASE

import math

def easeOut(easetype,start,end,length):

    if easetype == "linear":
        graph = []

        for i in range(length):
            graph.append(start+((end-start)*(i/(length-1))))

    elif easetype == "sine":
        graph = []

        for i in range(length):
            graph.append(start+(end-start)*math.sin(i/(length-1)*math.pi/2))

    elif easetype == "quad" or easetype == "quadratic":
        graph = []

        for i in range(length):
            graph.append(start+(end-start)*(1-(1-i/(length-1))**2))

    elif easetype == "cube" or easetype == "cubic":
        graph = []

        for i in range(length):
            graph.append(start+(end-start)*(1-(1-i/(length-1))**3))

    elif easetype == "quart" or easetype == "quartic":
        graph = []

        for i in range(length):
            graph.append(start+(end-start)*(1-(1-i/(length-1))**4))

    elif easetype == "quint" or easetype == "quintic":
        graph = []

        for i in range(length):
            graph.append(start+(end-start)*(1-(1-i/(length-1))**5))



    return graph

def easeIn(easetype,start,end,length):

    easein = easeOut(easetype,start,end,length)[::-1]
    graph = []

    for i in range(length):
        graph.append(end-easein[i])

    return graph

def easeInOut(easetype,start,end,length):

    easeout = easeOut(easetype,(end-start)/2,end,length//2)
    easein = easeIn(easetype,start,(end-start)/2,length-length//2)

    return easein+easeout


#lenght