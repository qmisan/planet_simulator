#!/usr/bin/python

# toolbar.py
from visual import *
import wx
from toolbarPanel import ToolbarPanel


class MyWindow(window):

    def __init__(self, title):
        # Window init
        window.__init__(self, title=title)

        # Filemenu
        self.SetMenubar()  # Adding menuBar to frame


        # Toolbar
        tb_panel = ToolbarPanel(self)
        tb_panel.SetBackgroundColour("#BABABA")

        # View
        panel1 = wx.Panel(self, -1)
        panel1.SetBackgroundColour("BLUE")

        # Databar
        panel2 = wx.Panel(self, -1)
        panel2.SetBackgroundColour("RED")
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(panel1, 3, wx.EXPAND)
        hbox2.Add(panel2, 1, wx.EXPAND)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(tb_panel, 0)
        vbox.Add(hbox2, 1, wx.EXPAND)
        self.SetSizer(vbox)

        self.Centre()

    def SetMenubar(self):

        #File menu for basic menu functionality
        filemenu = wx.Menu()

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


        # Help menu for about and information about documentation
        helpmenu = wx.Menu()
        # Adding "About" menuItem and setting event
        menuItem = helpmenu.Append(wx.ID_ABOUT, "&About",
                                   "Information about this program")
        self.win.Bind(wx.EVT_MENU, self.OnAbout, menuItem)
        
        # NOTE: Implement other wx.Menu instances here
        
        # Creating the menubar.
        menuBar = wx.MenuBar()
        # Adding menus
        menuBar.Append(filemenu, "&File")
        menuBar.Append(helpmenu, "&Help")

        # Add other menus to menubar here
        # -------------------------------

        # --------------------------------
        # Adding ready menubar to frame
        self.win.SetMenuBar(menuBar)  # Adding menuBar to frame


    def SetToolbar(self):

        # Init toolbar
        toolbar = self.win.CreateToolBar()
        toolbar.SetToolBitmapSize((20, self.toolbarheight))  # Button size in pixels?
        # qtool = toolbar.AddLabelTool(wx.ID_ANY,'Quit',wx.Bitmap('run_button.png'))
        # Creating 'RUN' button to toolbar
        runTool = toolbar.AddLabelTool(wx.ID_ANY,
                                       'Run Simulation',
                                       wx.Bitmap('GUI/run_button.png'))
        self.win.Bind(wx.EVT_TOOL, self.OnRun, runTool)
 
        # Creating 'Pause' button to toolbar
        pauseTool = toolbar.AddLabelTool(wx.ID_ANY,
                                              'Pause Simulation',
                                              wx.Bitmap('GUI/pause_button.png'))
        self.win.Bind(wx.EVT_TOOL, self.OnPause, pauseTool)

        toolbar.Realize()  # IDIOT U FORGOT TO SHOW IT!!!!!

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
        # TODO: If simulation already loaded ask if want open new one without saving dialog
        # if not self.simulation == None:

        self.dirname = ''

        dlg = wx.FileDialog(self.win, "Choose a file",
                            self.dirname, "", "*.*", wx.OPEN)

        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()


            # Now we have path to selected file
            self.simulation = Simulation(self)
            self.simulation.load(os.path.join(self.dirname, self.filename))
            self.simulation.space.print_elements()

            # Makes display for visualization
            # TODO: Need to dock display to mainWindow
            # self.SetDisplay()

            # Make visuals to all elements and add them rendering space
            # self.simulation.make_visuals()
            # self.simulation.render()
            # rate = 
        self.state_saved = True
        dlg.Destroy()
        while(1):
            rate(100)

    def OnSaveAs(self, event):

        # TODO: DialogBox to ask if user wants to save already saved material
        # MessageBox telling that state has already been saved
        # Asks if user wants to save to different location
        # if self.isSaved == True:
        #     pass

        self.dirname = ''

        saveFileDialog = wx.FileDialog(self.win, "Save simulation file",
                                       self.dirname, "", "*.*", wx.FD_SAVE |
                                       wx.FD_OVERWRITE_PROMPT)

        if saveFileDialog.ShowModal() == wx.ID_OK:
            self.filename = saveFileDialog.GetFilename()
            self.dirname = saveFileDialog.GetDirectory()

            # Save state
            self.simulation.save(os.path.join(self.dirname, self.filename))
            self.state_saved = True

        # Destroy file dialog
        saveFileDialog.Destroy()

    def OnExit(self, event):

        # Save before exit dialog
        if self.state_saved == False:
            dlg = wx.MessageDialog(self.win,
                                   "Do you want to save it?",
                                   "State not saved",
                                   wx.YES | wx.NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            dlg.Destroy()
            if result == wx.ID_YES:
                print("I WENT HERE")
                self.OnSaveAs(wx.EVT_MENU)

        else:
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

        if self.simulation == None:
            dlg5 = wx.MessageDialog(self.win,
                                   "No loaded simulation state present!",
                                    "Error running simulation!",
                                    wx.OK)
            dlg5.ShowModal()
            dlg5.Destroy()
            return

        # Asking simulation speed
        dlg = wx.TextEntryDialog(None,
                                 "Set simulation speed (seconds/real second)",
                                 "Run")
        dlg.SetValue("100")

        if dlg.ShowModal() == wx.ID_OK:
            simulation_speed = int(dlg.GetValue())
            if not isinstance(simulation_speed, int):
                pass
                # raise WrongSimulationParameterError("")

        # Asking simulation speed
        dlg2 = wx.TextEntryDialog(None, "Set timestep (seconds)", "Run")
        dlg2.SetValue("1")

        if dlg2.ShowModal() == wx.ID_OK:
            simulation_timestep = int(dlg2.GetValue())
            if not isinstance(simulation_timestep, int):
                pass
                # raise WrongSimulationParameterError("")

        # Asking rendering frequency
        dlg3 = wx.TextEntryDialog(None, "Set rendering frequency", "Run")
        dlg3.SetValue("2")

        if dlg3.ShowModal() == wx.ID_OK:
            frequency = int(dlg3.GetValue())
            if not isinstance(frequency, int):
                pass
                # raise WrongSimulationParameterError("")

        self.simulation.run(simulation_speed, simulation_timestep, frequency)



if __name__ == '__main__':
    _app = wx.App()
    w = MyWindow("Test")
    _app.MainLoop()


