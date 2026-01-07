#EASE

import math

def easeOut(easetype,start,end,length):

    if easetype == "linear":
        add = (end-start)/length
        graph = [start]

        for i in range(length):
            graph.append(graph[i]+add)

    elif easetype == "sine":
        add = (end-start)/length
        graph = []

        for i in range(length):
            graph.append((math.sin(((i+1)*math.pi)/(length*2))*(end-start))+start)

    print (len(graph))

    return graph

def easeIn(easetype,start,end,length):

    easein = easeOut(easetype,start,end,length)[::-1]
    graph = []

    for i in range(length):
        graph.append(end - easein[i])

    return graph

def easeInOut(easetype,start,end,length):

    easein = easeIn(easetype,start+((end-start)/2),end,int(length/2))
    easeout = easeOut(easetype,start,end-((end-start)/2),int(length/2))

    for i in range(int(length/2)):
        easeout[i] += (end-start)/2

    if length/2 == round(length/2):
        return easein + easeout
