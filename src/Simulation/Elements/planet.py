from element import Element
from visual import *


class Planet(Element):
    """
    docstring for Planet
    """
    # Not on init
    type = "Planet"  # Made always for this type, used in element str
    space = None
    visual = None
    radius = 1

    def __init__(self, label, position, velocity, mass, color=color.blue):

        self.color = color


        self.label = label
        self.position = position  # Vector value from origon
        self.velocity = velocity  # Vector value
        self.mass = mass

        self.acceleration = vector(0, 0, 0)
        self.next_pos = self.position
        self.next_vel = self.velocity
