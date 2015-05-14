from visual import *  # For vectors
from physics import *

class Space(object):
    """
    docstring for Space
    """
    def __init__(self):
        # Makes space object with given x,y,z size
        self.element_list = []

    def add_element(self, element):
        element.space = self
        self.element_list.append(element)

    def calculate_physics(self, time):
        for element in self.element_list:
            for other in self.element_list:
                if not (other.position == element.position):
                    g = gravity(element, other)
                    element.acceleration = element.acceleration + g/element.mass
                    if collision(element,other):
                        print("COLLIDEDDDD!!!")
            element.next_pos = element.position + element.velocity*time+0.5*element.acceleration*(time**2)
            element.next_vel = element.next_vel + element.acceleration*time

    def update_physics(self):
        for element in self.element_list:
            element.update()

    def get_smallest(self):
        smallest = self.element_list[0]
        for element in self.element_list:
            if element.mass < smallest.mass:
                smallest = element
        return smallest

    def get_biggest(self):
        biggest = self.element_list[0]
        for element in self.element_list:
            if element.mass > biggest.mass:
                biggest = element
        return biggest

    def get_longest_distance(self):
        longest = self.element_list[0]
        for element in self.element_list:
            if mag(element.position) > mag(longest.position):
                longest = element
        return mag(longest.position)

    def print_elements(self):
        for element in self.element_list:
            print("______________________")
            print(element)
            print("______________________")

