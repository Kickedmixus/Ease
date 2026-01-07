import matplotlib.pyplot as plt
import turtle
import ease
import numpy as np

scale = 5

def test(easeMovement,easeType):

    if easeMovement == "easeIn":
        graph = ease.easeIn(easeType,0,100,100)
    elif easeMovement == "easeOut":
        graph = ease.easeOut(easeType,0,100,100)
    elif easeMovement == "easeInOut":
        graph = ease.easeInOut(easeType,0,100,100)

    fig, ax = plt.subplots()

    plt.plot(graph, linewidth=2.5)

    ax.set(xlim=[0,100], xticks=[100,50,0,],
        ylim=[0,100], yticks=[100,50,0])

test("easeIn","sine")
test("easeOut","sine")
test("easeInOut","sine")

plt.show()