from space import Space
from Elements.element import Element
from Elements.planet import Planet
from Elements.star import Star
from Elements.satellite import NaturalSatellite
from visual import *


class Simulation(object):
    """
    This class is instance of simulation state.
    It owns current space along with its elements.
    It also runs physics part forward in time.
    """
    # Flags
    debug_mode = False
    collided = False

    def __init__(self, window):
        self.space = Space(self)
        self.win = window

    def load(self, file):  # NOTE: DONE Parsing state from file
        """
        Parses simulation state out of file
        """
        if self.win.debug_mode:
            print("Loading file...")
        self.collided = False
        with open(file) as f:
            data = f.readlines()
            for line in data:
                if not line.startswith("#"):
                    line_data = line.split()

                    # If type planet
                    if line_data[0].strip().lower() == "planet":
                        if self.win.debug_mode:
                            print("Loader found planet")
                        label = line_data[1]
                        vec = line_data[2].split(",")
                        position = vector(float(vec[0]), float(vec[1]),
                                          float(vec[2]))
                        vec = line_data[3].split(",")
                        velocity = vector(float(vec[0]), float(vec[1]),
                                          float(vec[2]))
                        mass = float(line_data[4])
                        try:
                            line_data[5].strip("\n")
                            clr = Element.colors[line_data[5]]

                            new_element = Planet(label, position, velocity,
                                                 mass, clr)
                        except IndexError:
                            new_element = Planet(label, position, velocity, mass)

                        self.add(new_element)

                    elif line_data[0].strip().lower() == "star":
                        if self.win.debug_mode:
                            print("Loader found star")
                        label = line_data[1]
                        vec = line_data[2].split(",")
                        position = vector(float(vec[0]), float(vec[1]),
                                          float(vec[2]))
                        vec = line_data[3].split(",")
                        velocity = vector(float(vec[0]), float(vec[1]),
                                          float(vec[2]))
                        mass = float(line_data[4])
                        # try:
                        #     line_data[5].strip("\n")
                        #     clr = Element.colors[line_data[5]]
                        #     new_element = Planet(label, position, velocity,
                        #                          mass, clr)
                        # except IndexError:
                        #     new_element = Star(label, position, velocity, mass)

                        # clr = Element.colors[line_data[5]]
                        new_element = Star(label, position,
                                           velocity, mass)
                        self.add(new_element)

                    # If type NaturalSatellite
                    elif line_data[0].strip().lower() == "naturalsatellite":
                        if self.win.debug_mode:
                            print("Loader found naturalsatellite")
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

                        new_element = NaturalSatellite(label, position, velocity,
                                             mass, clr)
                        self.add(new_element)
                    # NOTE: Other types here

        if self.win.debug_mode:
            print("Loaded following elements to simulation state:")
            self.space.print_elements()
        f.close()
        self.make_visuals()
        # self.render()

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
        if self.win.debug_mode:
            print("Simulation adding element")
        self.space.add_element(element)

    def make_visuals(self):
        """
        Makes visual model for each element in space
        """

        if self.win.debug_mode:
            print("Making visuals")
        # If already frame old one needs to be destroyed
        if not self.win.scene == None:
            self.win.scene.delete()

        # Initializing 3D-canvas
        self.win.SetDisplay()

        for element in self.space.element_list:
            if element.type == "Planet" and (element.label == "Earth" or element.label == "earth"):
                if self.win.debug_mode:
                    print("Visualizator found label earth")
                element.visual = sphere(pos=element.position, make_trail=True, radius=element.radius,
                                        material=materials.earth)

            elif element.type == "Star":
                element.visual = sphere(pos=element.position, make_trail=True, radius=element.radius,
                                        color=element.color, material=materials.emissive)

            else:
                element.visual = sphere(pos=element.position, make_trail=True, radius=element.radius,
                                        color=element.color)

            element.visual.label = label(pos=element.visual.pos,
                                         text=str(element), xoffset=20,
                                         yoffset=12,
                                         space=element.visual.radius,
                                         height=10, border=6,
                                         font='sans')

            # Stars have unique ability: Emitting light
            # In addition they have increased radius compared to other objects

    def run(self, speed, timestep, frequency, **kwargs):
        """
        Runs simulation forward from current state with current parameters
        @param speed: How many times physics calculated per second
        @param timestep: How much time elapses between calculations
        @param frequency: How many many times visual models updated per speed
        (seconds/real second)
        """
        if self.win.debug_mode:
            print("Simulation running")
        self.win.simulation_stopped = False
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

    def stop(self):
        if self.win.debug_mode:
            print("Simulation stopped")
        if self.win.simulation_stopped == True:
            pass
        else:
            self.win.simulation_stopped = True
            while(True):
                rate(10)

    def render(self):
        """
        Renders space for every frame and updates visual model position
        to it's paraller in physics engine
        """
        for element in self.space.element_list:
            element.visual.pos = element.position

            # Always update labels too (can hide)
            element.visual.label.pos = element.visual.pos
            element.visual.label.text = str(element)

        if not self.win.following==None:
            self.win.scene.center = self.win.following.visual.pos
