from element import Element
from visual import *


class NaturalSatellite(Element):
    """
    docstring for NaturalSatellite
    """
    # Not on init
    type = "NaturalSatellite"  # Made always for this type, used in element str
    space = None
    visual = None
    radius = 0.2

    def __init__(self, label, position, velocity, mass, color=color.blue):

        self.color = color


        self.label = label
        self.position = position  # Vector value from origon
        self.velocity = velocity  # Vector value
        self.mass = mass

        self.acceleration = vector(0, 0, 0)
        self.next_pos = self.position
        self.next_vel = self.velocity
