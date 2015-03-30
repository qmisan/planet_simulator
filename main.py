from GUI.mainWindow import *
import wx

"""
This file works as a interface between
 GUI Simulation and Visualization
"""


def main():
    app = wx.App(False)  # Always needs this
    MainWindow("Planet simulator")
    app.MainLoop()

if __name__ == '__main__':
    main()
