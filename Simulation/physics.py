from visual import *
"""
This file will include the physics equations I will use for this project
"""


def gravity(element1, element2):
    """
    Returns force vector (so that it has direction) 
    so it must be scalar
    times unit vector from element1.location to element2.location
    """
    return (((element1.mass * element2.mass) /
            distance(element1.position, element2.position)**2)
            * 6.67384**(-11)) * unit_vector(element2.position
                                            - element1.position)


def acceleration(force, mass):
    """
    Gives result a = F/m
    """
    return (force*(1/mass))


def distance(loc1, loc2):  # Locations vectorvalues
    return mag(loc1-loc2)


def unit_vector(vector):
    """
    Makes unit vector with same direction as param
    """
    return vector/mag(vector)

