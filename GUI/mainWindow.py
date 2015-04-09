import wx  # wx.Frame etc
import os  # To get path for "Open file"
from visual import *
from toolbarPanel import ToolbarPanel
# from Simulation.simulation import Simulation
# from Visualization.view import View


class MainWindow(window):
    """
    This class is baseclass for MainWindow. MainWindow panels
    are implemented in their own classes. MainWindow implements
    filemenu and its functionality and sizers for different
    """
    # ID LIST FOR BUTTONS
    ID_RUN_BUTTON = wx.NewId()
    ID_PAUSE_BUTTON = wx.NewId()
    ID_TOOLBAR = wx.NewId()
    simulation = None

    def __init__(self, title):

        # Frame initialization

        # Get local display size
        local_display_size = wx.GetDisplaySize()

        #  Initialize mainwindow with size 0.5 * width
        #  and full height of local display
        window.__init__(self, parent=None, title=title,
                        size=(local_display_size[0]/2,
                              0.8*local_display_size[1]),
                        _make_panel=False)

        self.SetMenubar()
        self.SetToolbar()

        self.win.Centre()

    def SetMenubar(self):
        filemenu = wx.Menu()
        # Adding "About" menuItem and setting event
        menuItem = filemenu.Append(wx.ID_ABOUT, "&About",
                                   "Information about this program")
        self.win.Bind(wx.EVT_MENU, self.OnAbout, menuItem)
        # Adding "Open" and setting event
        menuItem = filemenu.Append(wx.ID_OPEN, "&Open",
                                   "Open simulation state from file")
        self.win.Bind(wx.EVT_MENU, self.OnOpen, menuItem)
        # Adding "Save as" and setting event
        menuItem = filemenu.Append(wx.ID_SAVE, "&Save as",
                                   "Save simulation state to file")
        self.win.Bind(wx.EVT_MENU, self.OnSaveAs, menuItem)
        # Adding "Exit" and setting event
        menuItem = filemenu.Append(wx.ID_EXIT, "&Exit",
                                   "Terminate the program")
        self.win.Bind(wx.EVT_MENU, self.OnExit, menuItem)

        # Implement other wx.Menu instances here

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")  # Adding "filemenu" to menuBar

        # Add other menus to menubar here
        # -------------------------------

        # --------------------------------
        # Adding ready menubar to frame
        self.win.SetMenuBar(menuBar)  # Adding menuBar to frame

    def SetToolbar(self):

        # Init toolbar
        self.toolbar = self.win.CreateToolBar()
        self.toolbar.SetToolBitmapSize((20, 10))  # Button size in pixels?
        # Creating 'RUN' button to toolbar
        runTool = self.toolbar.AddLabelTool(wx.EVT_BUTTON, 'Run Simulation',
                                            wx.Bitmap('run_button.png'))
        self.win.Bind(ID_RUN_BUTTON, self.onRun, runTool)
        # Creating 'Pause' button to toolbar
        pauseTool = self.toolbar.AddLabelTool(wx.EVT_BUTTON,
                                              'Pause Simulation',
                                              wx.Bitmap('pause_button.png'))
        self.win.Bind(ID_PAUSE_BUTTON, self.on, pauseTool)

        self.toolbar.Realize()  # IDIOT U FORGOT TO SHOW IT!!!!!

    def SetStatusbar(self):
        pass

    def OnAbout(self, event):
        """Show about dialog box"""
        # A message dialog box with an OK button.
        # wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog(self.win, "Planet simulator version 1.0",
                               "About Planet simulator", wx.OK)
        dlg.ShowModal()  # Show it
        dlg.Destroy()  # finally destroy it when finished.

    def OnOpen(self, event):
        """ Load state from file """
        self.dirname = ''

        dlg = wx.FileDialog(self.win, "Choose a file",
                            self.dirname, "", "*.*", wx.OPEN)

        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()

            # Now we have path to selected file
            self.simulation = Simulation()
            self.simulation.load(os.path.join(self.dirname, self.filename))
            self.simulation.space.print_elements()
            self.simulation.render()

        dlg.Destroy()

    def OnSaveAs(self, event):
        self.dirname = ''

        saveFileDialog = wx.FileDialog(self.win, "Save simulation file",
                                       self.dirname, "", "*.*", wx.FD_SAVE |
                                       wx.FD_OVERWRITE_PROMPT)

        if saveFileDialog.ShowModal() == wx.ID_OK:
            self.filename = saveFileDialog.GetFilename()
            self.dirname = saveFileDialog.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'w')

            # Now we have bath to selected file
            # simulation.load(f)

            f.close()
        saveFileDialog.Destroy()

    def OnExit(self, event):
        dlg = wx.MessageDialog(self.win,
                               "Do you really want to close this application?",
                               "Confirm Exit",
                               wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            exit()

    def OnRun(self, event):
        """
        When OnRun called TextEntryDialog will pop up
        to ask user simulation run parameters
        @para
        """
        simulation_speed = 0
        simulation_timestep = 0

        # Asking simulation speed
        dlg = wx.TextEntryDialog(None,
                                 "Set simulation speed (seconds/real second)",
                                 "Run")
        dlg.SetValue("100")

        if dlg.ShowModal() == wx.ID_OK:
            simulation_speed = dlg.GetValue()
            if not isinstance(simulation_speed, int):
                pass
                # raise WrongSimulationParameterError("")

        # Asking simulation speed
        dlg2 = wx.TextEntryDialog(None, "Set timestep (seconds)", "Run")
        dlg2.SetValue("1")

        if dlg2.ShowModal() == wx.ID_OK:
            simulation_timestep = dlg2.GetValue()
            if not isinstance(simulation_timestep, int):
                pass
                # raise WrongSimulationParameterError("")
        # try:
        #     # simulation.run(simulation_timestep)
        # except:
        #     pass

    def OnPause(self, event):
        pass

if __name__ == '__main__':
    app = wx.App(False)  # Always needs this
    w = MainWindow("Test Frame")
    app.MainLoop()
