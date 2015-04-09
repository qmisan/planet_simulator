# from .Simulation.simulation import *
import wx
from visual import *
# from Visualization.planetModel import PlanetModel
# from Visualization.starModel import StarModel


class View(wx.Frame):
    title = "3D-canvas"

    def __init__(self, parentWindow):
        print("GOT:{}\nAND:{}".format(parentWindow.width,parentWindow.height))

        display(window=parentWindow, width=parentWindow.width*0.8, 
                height=parentWindow.height*0.8)
        sphere()
if __name__ == "__main__":
    pass