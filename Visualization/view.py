# from .Simulation.simulation import *
import wx
from visual import *
# from Visualization.planetModel import PlanetModel
# from Visualization.starModel import StarModel


class View(object):
    def __init__(self, parentWindow):
        self.scene = display(window=parentWindow, x=0, y=0,
                             width=parentWindow.dwidth,
                             height=parentWindow.dheight,
                             forward=-vector(0, 1, 2))

        print("Been there done that")
        self.scene = display

        # Scale factors (NOTE: DO I Need these?)
        # scale_dist = simulation.space.get_longest_distance()
        # scale_mass = simulation.space.get_smallest().mass
        sphere()

        # model_list = []
        # for element in simulation.space.element_list:
        #     if element.type == "Star":
        #         new = StarModel((element.position), element.mass/scale_mass,
        #                         str(element))
        #     else:
        #         new = PlanetModel(element.position/scale_dist,
        #                           element.mass/scale_mass, str(element))
        #     model_list.append(new)

if __name__ == "__main__":
    pass