"""
This is model for unittest file. For every module there will be thorough
unittest walkthrough to test module functionality properly
"""
import unittest
from simulation import *
from visual import *


class Test(unittest.TestCase):

    def setUp(self):
        """
        In setUp make needed testing structure (class instances etc)
        """

    def test_physics(self):
        pass

    def test_element(self):

        # Planet
        test_planet = Planet("Testi1", vector(1, 2, 3),
                             vector(1, 2, 3), 100, color.green, None)
        # Init values
        self.assertEqual(test_planet.label, "Testi1",
                         "Name was not implemented properly")
        self.assertEqual(test_planet.position, vector(1, 2, 3),
                         "Position was not implemented properly")
        self.assertEqual(test_planet.velocity, vector(1, 2, 3),
                         "Velocity was not implemented properly")
        self.assertEqual(test_planet.mass, 100,
                         "Mass was not implemented properly")
        self.assertEqual(test_planet.space, None,
                         "Parent space was not implemented properly")

        # Star
        test_star = Star("Testi2", vector(0, 0, 0),
                         vector(0, 0, 0), 100, None)
        # Init values
        self.assertEqual(test_star.label, "Testi2",
                         "Name was not implemented properly")
        self.assertEqual(test_star.position, vector(0, 0, 0),
                         "Position was not implemented properly")
        self.assertEqual(test_star.velocity, vector(0, 0, 0),
                         "Velocity was not implemented properly")
        self.assertEqual(test_star.mass, 100,
                         "Mass was not implemented properly")
        self.assertEqual(test_star.space, None,
                         "Parent space was not implemented properly")

        # Test for element methods update, __str__ and get_color
        new_pos = test_planet.velocity + test_planet.position
        test_planet.new_pos = new_pos
        test_planet.update()
        self.assertEqual(test_planet.position, vector(2, 4, 6),
                         "Element method update not working proberly")


    def test_space(self):
        pass


    def test_simulation(self):
        pass


if __name__ == "__main__":
    unittest.main()
