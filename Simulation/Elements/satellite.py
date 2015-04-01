from Simulation.element import Element
class Satellite(Element):
    """docstring for Satellite"""
    def __init__( self, label, position, velocity, mass, space):
        self.location = location
        self.velocity = velocity # Vector value (power,direction)
        self.direction = direction
        self.type = "Satellite"
        self.id = "MIR-500"