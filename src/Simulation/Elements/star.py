from element import Element
from visual import *

class Star(Element):
    """
    docstring for Star
    """
    # Not on init
    type = "Star" # Made always for this type, used in element __str__
    space = None
    visual = None
    radius = 3

    def __init__( self, label, position, velocity, mass, color=color.yellow):

        self.color = color
        self.label = label
        self.position = position # Vector value from origon
        self.velocity = velocity # Vector value
        self.mass = mass

        self.acceleration = vector(0,0,0)
        self.next_pos = self.position
        self.next_vel = self.velocity