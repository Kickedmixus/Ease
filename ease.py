#EASE

import math

def easeOut(easetype,start,end,length):

    if easetype == "linear":
        dif = (end-start)
        graph = []

        for i in range(length):
            graph.append(start+(dif*(i/(length-1))))

    elif easetype == "sine":
        add = (end-start)/length
        graph = []

        for i in range(length):
            graph.append(start+(end-start)*math.sin(i/(length-1)*math.pi/2))

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