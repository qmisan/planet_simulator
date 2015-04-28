from space import Space
from Elements.element import Element
from Elements.planet import Planet
from Elements.star import Star
from visual import *


class Simulation(object):
    """
    This class is instance of simulation state.
    It owns current space along with its elements.
    It also runs physics part forward in time.
    """
    # Settings
    labels = True


    def __init__(self, **kwargs):
        self.space = Space()

        # NOTE: TESTPRINT
        for key in kwargs:
            print(key)
        if kwargs["labels"] == False:
            self.labels = False

    def load(self, file):  # NOTE: DONE Parsing state from file
        """
        Parses simulation state out of file
        """
        with open(file) as f:
            data = f.readlines()
            for line in data:
                if not line.startswith("#"):
                    line_data = line.split()
                    # If type planet
                    if line_data[0].strip().lower() == "planet":
                        label = line_data[1]
                        vec = line_data[2].split(",")
                        position = vector(float(vec[0]), float(vec[1]),
                                          float(vec[2]))
                        vec = line_data[3].split(",")
                        velocity = vector(float(vec[0]), float(vec[1]),
                                          float(vec[2]))
                        mass = float(line_data[4])
                        line_data[5].strip("\n")
                        clr = Element.colors[line_data[5]]
                        new_element = Planet(label, position, velocity,
                                             mass, clr)
                        self.add(new_element)

                    elif line_data[0].strip().lower() == "star":
                        label = line_data[1]
                        vec = line_data[2].split(",")
                        position = vector(float(vec[0]), float(vec[1]),
                                          float(vec[2]))
                        vec = line_data[3].split(",")
                        velocity = vector(float(vec[0]), float(vec[1]),
                                          float(vec[2]))
                        mass = float(line_data[4])
                        line_data[5].strip("\n")
                        # clr = Element.colors[line_data[5]]
                        new_element = Star(label, position,
                                           velocity, mass)
                        self.add(new_element)

                    # NOTE: Other types here
        print("Loaded following elements to simulation state:")
        self.space.print_elements()
        f.close()
        self.make_visuals()
        self.render()

    def save(self, file):  # NOTE: DONE Saving state into file
        """
        Saves current state in a file
        """
        f = open(file, "w")
        f.write("# This is simulation state file\n")
        f.write("# Tyyppi label position(muodossa: x,y,z)"
                "velocity(x,y,z) mass color\n")
        for element in self.space.element_list:
            f.write(element.type + " " +
                    element.label + " " +
                    str(element.position.x)+","+str(element.position.y)+","
                    + str(element.position.y) + " " +
                    str(element.velocity.x)+","+str(element.velocity.y)+","
                    + str(element.velocity.y)+" "+str(element.mass) + " " +
                    element.get_color() + "\n")
        f.close()



    def add(self, element):
        self.space.add_element(element)

    def make_visuals(self):
        """
        Makes visual model for each element in space
        """
        for element in self.space.element_list:
            element.visual = sphere(pos=element.position,
                                    make_trail=True, radius=1)
            if self.labels:
                element.visual.label = label(pos=element.visual.pos,
                                             text=str(element), xoffset=20,
                                             yoffset=12,
                                             space=element.visual.radius,
                                             height=10, border=6,
                                             font='sans')

            if element.type == "Planet":
                # Earth has unique texture material
                # Other than that its similar to planet objects
                if element.label == "Earth":
                    element.visual.material = materials.earth
                else:
                    element.visual.color = element.color

            # Stars have unique ability: Emitting light
            # In addition they have increased radius compared to other objects
            if element.type == "Star":
                element.visual.color = element.color
                element.visual.material = materials.emissive
                element.visual.radius = 2

    def run(self, speed, timestep, frequency, **kwargs):
        """
        Runs simulation forward from current state with current parameters
        @param speed: How many times physics calculated per second
        @param timestep: How much time elapses between calculations
        @param frequency: How many many times visual models updated per speed
        (seconds/real second)
        """
        i = 0

        while(1):
            rate(speed)
            self.space.calculate_physics(timestep)
            self.space.update_physics()

            self.render()
            i = i + 1
            # print(str(self.space.element_list[0]))
            if i == frequency:
                self.render()
                i = 0

    def render(self):
        """
        Renders space for every frame and updates visual model position
        to it's paraller in physics engine
        """
        for element in self.space.element_list:
            element.visual.pos = element.position

            # If options define to show labels
            if self.labels:
                element.visual.label.pos = element.visual.pos
                element.visual.label.text = str(element)

