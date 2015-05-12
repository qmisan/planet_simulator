"""
This is model for unittest file. For every module there will be thorough
unittest walkthrough to test module functionality properly
"""
import unittest
from Simulation.simulation import *
from visual import *


class Test(unittest.TestCase): # TODO: TEST doesn't follow recent changes to program structure

    def setUp(self):
        """
        In setUp make needed testing structure (class instances etc)
        """

        # Planet
        self.planet = Planet("Testi1", vector(1, 2, 3),
                             vector(1, 2, 3), 100, color.green)
        # Star
        self.star = Star("Testi2", vector(0, 0, 0),
                         vector(0, 0, 0), 100)

        #Space
        self.space = Space()

    def test_physics(self):
    	"""
    	In test 2 elements, star and planet
    	"""
        pass

    def test_element(self):

        # Init values
        self.assertEqual(self.planet.label, "Testi1",
                         "Name was not implemented properly")
        self.assertEqual(self.planet.position, vector(1, 2, 3),
                         "Position was not implemented properly")
        self.assertEqual(self.planet.velocity, vector(1, 2, 3),
                         "Velocity was not implemented properly")
        self.assertEqual(self.planet.mass, 100,
                         "Mass was not implemented properly")
        self.assertEqual(self.planet.space, None,
                         "Parent space was not implemented properly")

        # Init values
        self.assertEqual(self.star.label, "Testi2",
                         "Name was not implemented properly")
        self.assertEqual(self.star.position, vector(0, 0, 0),
                         "Position was not implemented properly")
        self.assertEqual(self.star.velocity, vector(0, 0, 0),
                         "Velocity was not implemented properly")
        self.assertEqual(self.star.mass, 100,
                         "Mass was not implemented properly")
        self.assertEqual(self.star.space, None,
                         "Parent space was not implemented properly")

        # Test for element methods update, __str__ and get_color
        new_pos = self.planet.velocity + self.planet.position
        self.planet.next_pos = new_pos
        self.planet.update()
        self.assertEqual(self.planet.position, vector(2, 4, 6),
                         "Element method update not working proberly,"
                         + "got {}.".format(self.planet.position))

    def test_space(self):
        # Init
        self.assertTrue(self.space, "Initiating space is not working properly")

        # Testing add_element
        self.space.add_element(self.planet)
        self.assertEqual(len(self.space.element_list), 1,
                         "add_element is not working properly")

        self.assertEqual(self.space.element_list[0].label, "Testi1",
                         "add_element is not working properly")

        # Test update


if __name__ == "__main__":
    unittest.main()
