from space import Space
from Elements.element import Element
from Elements.planet import Planet
from Elements.star import Star
from visual import *

class Simulation(object):
    """
    This class is instance of simulation state. It owns current space along with
    its elements. It also runs physics part forward in time.
    """
    def __init__(self):
        self.space = Space()
        # Simulation parameters
        # TODO: self.Space initialization and shit to simulation
        self.timestep = 1

    def load(self,file): # TODO: Parsing state from file
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
                        position = vector(float(vec[0]),float(vec[1]),float(vec[2]))
                        vec = line_data[3].split(",")
                        velocity = vector(float(vec[0]),float(vec[1]),float(vec[2]))
                        mass = float(line_data[4])
                        line_data[5].strip("\n")
                        clr = Element.colors[line_data[5]]
                        new_element = Planet(label, position, velocity, mass, clr, self.space)
                        self.add(new_element)

                    elif line_data[0].strip().lower() == "star":
                        label = line_data[1]
                        vec = line_data[2].split(",")
                        position = vector(float(vec[0]),float(vec[1]),float(vec[2]))
                        vec = line_data[3].split(",")
                        velocity = vector(float(vec[0]),float(vec[1]),float(vec[2]))
                        mass = float(line_data[4])
                        line_data[5].strip("\n")
                        # clr = Element.colors[line_data[5]]
                        new_element = Star(label, position, velocity, mass, self.space)
                        self.add(new_element)

                    # TODO: Other types here
        print("Current state contains now following elements:")
        self.space.print_elements()
        f.close()

    def save(self,file): # TODO: Saving state into file
        """
        Saves current state in a file
        """
        f = open(file,"w")
        f.write("# This is simulation state file\n")
        f.write("# Tyyppi label position(muodossa: x,y,z) velocity(x,y,z) mass color\n")
        for element in self.space.element_list:
            f.write(element.type + " " +
            element.label + " " +
            str(element.position.x) +","+ str(element.position.y) +","+ str(element.position.y) + " " +
            str(element.velocity.x) +","+ str(element.velocity.y) +","+ str(element.velocity.y) + " " +
            str(element.mass) + " " +
            element.get_color() + "\n") # TODO: Color type? How to make string?
        f.close()

    def run(self,samp):
        """
        Runs simulation forward from current state with current parameters
        @param samp: how many times per second this is updated (seconds/real second)
        """
        
        while(True):
            rate(samp)
            self.space.calculate_physics(self.timestep)
            self.space.update_physics()
            print(str(self.space.element_list[0]))


    def add(self,element):
        self.space.add_element(element)

    def render(self): # TODO: Can I move this to some kind of Visualization Right now in simulation or space?
        for element in self.space.element_list:
            element.visualization.pos = element.position
            element.visualization.label.pos = element.visualization.pos
            element.visualization.label.text = str(element)
