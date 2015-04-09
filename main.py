from Simulation.simulation import Simulation
from visual import *
"""
This file works as a interface between
 GUI Simulation and Visualization
"""


def main():
    w = window(menus=False, title="VPython",
               x=0, y=0, width=1920, height=1080)

    display(window=w, x=50, y=30, width=w.width*0.8,
            height=w.height*0.8)

    simu = Simulation()

    simu.load("test_files/simple.txt")

    # Run takes simulationspeed timestep and display update frequency
    # parameters
    # @ simulationspeed: How many calculations per second
    # @ timestep: How much time elapses
    # @ freq: How many calculations between model updation
    simu.run(50, 0.01, 2)

if __name__ == '__main__':
    main()
