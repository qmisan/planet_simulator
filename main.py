from Simulation.simulation import Simulation
from GUI.mainWindow import MainWindow
from visual import *
"""
This file works as a interface between
 GUI Simulation and Visualization
"""


def main():
	# Main window for simulatos
    w = MainWindow("Planet Simulator")


    # Run takes simulationspeed timestep and display update frequency
    # parameters
    # @ simulationspeed: How many calculations per second
    # @ timestep: How much time elapses
    # @ freq: How many calculations between model updation
    # simu.run(50, 0.1, 2)

if __name__ == '__main__':
    main()
