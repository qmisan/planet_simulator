from visual import *

class Element(object):
    """
    docstring for Element
    Element can be red, blue, yellow, cyan, white, orange or magenta
    """

    # Possible element colors 
    # NOTE: Can be RGB too but needs structure changing
    colors = {"red": color.red, "blue": color.blue,
              "cyan": color.cyan, "yellow": color.yellow,
              "white": color.white, "orange": color.orange,
              "magenta": color.magenta}

    def __init__(self, label, position, velocity, mass, color):
        pass

    def update(self):
        """
        This updates next position and velocity
        """
        self.position = self.next_pos
        self.velocity = self.next_vel
        self.acceleration = vector(0, 0, 0)

    def __str__(self):
        return (self.type + ": " + self.label +
                "\n" + "Position: {}".format(self.position) +
                "\n" + "Velocity: {}".format(self.velocity) +
                "\n" + "Mass: {}".format(self.mass))

    def get_color(self):
        for key in Element.colors.keys():
            if Element.colors[key] == self.color:
                return key
