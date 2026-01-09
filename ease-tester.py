import matplotlib.pyplot as plt
import turtle
import ease
import numpy as np

scale = 5

def test(easeMovement,easeType):

    if easeMovement == "easeIn":
        graph = ease.easeIn(easeType,0,amount,amount)
    elif easeMovement == "easeOut":
        graph = ease.easeOut(easeType,0,amount,amount)
    elif easeMovement == "easeInOut":
        graph = ease.easeInOut(easeType,0,amount,amount)
    elif easeMovement == "easeOutIn":
        graph = ease.easeInOut(easeType,0,amount,amount,True)

    print ("min "+str(min(graph))+" max "+str(max(graph))+" len "+str(len(graph)))

    fig, ax = plt.subplots()

    plt.plot(graph, linewidth=2.5)

    ax.set(xlim=[0,len(graph)], xticks=[len(graph),0],
        ylim=[0,len(graph)], yticks=graph)

amount = int(input("lenght of test >"))

test("easeIn","quint")
test("easeOut","quint")
test("easeInOut","quint")
test("easeOutIn","quint")

plt.show()

#lenght