"""
Test simulation visual running
"""
from visual import *
from simulation import Simulation
from Elements.element import Element
from Elements.planet import Planet
from Elements.star import Star
from physics import *




simu = Simulation()

star = Star("Aurinko", vector(0, 0, 0), vector(0, 0, 0), 5e10)
simu.space.add_element(star)

planet = Planet("Earth", vector(0, 50, 0), vector(1, 0, 0), 10, color.blue)
simu.space.add_element(planet)

planet2 = Planet("Mars", vector(0, -50, 0), vector(-1, 0, 0), 10, color.red)
simu.space.add_element(planet2)

simu.space.print_elements()
simu.make_visuals()

print(simu.space.element_list)


def calc(space):
    for element in space.element_list:
        calc_next(element, space, 1)


def calc_next(element, space, dt):
    element.acceleration = vector(0, 0, 0)
    for other in space.element_list:
        if not (other.position == element.position):
            g = gravity(element, other)
            element.acceleration = element.acceleration + g/element.mass

    element.next_pos = (element.position + element.velocity*dt + 0.5 *
                        element.acceleration * (dt**2))
    element.next_vel = element.velocity + element.acceleration*dt


def update(space):
    for element in space.element_list:
        element.position = element.next_pos
        element.velocity = element.next_vel

# Speed timestep and freq(renders/second)
while(1):
    rate(10)
    # calc(simu.space)
    # simu.space.calculate_physics(1)
    # simu.space.update_physics() # WORKS
    # simu.render()
    simu.run(10, 1, 60)
