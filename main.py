from Simulation.simulation import Simulation
from GUI.mainWindow import MainWindow
from visual import *
"""
This file works as a interface between
 GUI Simulation and Visualization
"""


def main():
    w = MainWindow("Planet Simulator")

    display(window=w, x=50, y=30, width=w.width*0.8,
            height=w.height*0.8)

    simu = Simulation()

    simu.load("test_files/simple.txt")

    # Run takes simulationspeed timestep and display update frequency
    # parameters
    # @ simulationspeed: How many calculations per second
    # @ timestep: How much time elapses
    # @ freq: How many calculations between model updation
    simu.run(50, 0.1, 2)

if __name__ == '__main__':
    main()
