#EASE

import math

def easeOut(easetype,start,end,lenght):

    if easetype == "linear":
        add = (end-start)/lenght
        graph = [start]

        for i in range(lenght):
            graph.append(graph[i]+add)

    elif easetype == "sine":
        add = (end-start)/lenght
        graph = []

        for i in range(lenght):
            graph.append((math.sin(((i+1)*math.pi)/(lenght*2))*(end-start))+start)

    print (len(graph))

    return graph

def easeIn(easetype,start,end,lenght):

    easein = easeOut(easetype,start,end,lenght)[::-1]
    graph = []

    for i in range(lenght):
        graph.append(end - easein[i])

    return graph

def easeInOut(easetype,start,end,lenght):

    easein = easeIn(easetype,start+((end-start)/2),end,int(lenght/2))
    easeout = easeOut(easetype,start,end-((end-start)/2),int(lenght/2))

    for i in range(int(lenght/2)):
        easeout[i] += (end-start)/2

    if lenght/2 == round(lenght/2):
        return easein + easeout
