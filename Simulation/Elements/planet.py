from element import Element
from visual import *


class Planet(Element):
    """
    docstring for Planet
    """
    def __init__(self, label, position, velocity, mass, color):

        self.color = color
        self.type = "Planet"  # Made always for this type, used in element str
        self.visual = None
        self.label = label
        self.position = position  # Vector value from origon
        self.velocity = velocity  # Vector value
        self.mass = mass
        self.space = None

        self.acceleration = vector(0, 0, 0)
        self.next_pos = self.position
        self.next_vel = self.velocity
