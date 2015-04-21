"""
Test simulation visual running
"""
from visual import *
from simulation import Simulation
from Elements.element import Element
from Elements.planet import Planet
from Elements.star import Star


simu = Simulation()


star = Star("Aurinko",vector(0,0,0),vector(0,0,0),2e10,simu.space)
simu.space.add_element(star)
Star()
simu.space.print_elements()
