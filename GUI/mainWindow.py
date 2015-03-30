import wx  # wx.Frame etc
import os  # To get path for "Open file"


class MainWindow(wx.Frame):

    # ID LIST FOR BUTTONS
    ID_RUN_BUTTON = wx.NewId()
    ID_PAUSE_BUTTON = wx.NewId()
    ID_TOOLBAR = wx.NewId()

    def __init__(self, title):

        # Frame initialization

        # Get local display size
        local_display_size = wx.GetDisplaySize()

        #  Initialize mainwindow with size 0.5 * width
        #  and full height of local display
        wx.Frame.__init__(self, parent=None, title=title,
                          size=(local_display_size[0]/2,
                                0.8*local_display_size[1]), pos=(0, 0))

        #  Setting up the menu.
        #  --------------------------------
        filemenu = wx.Menu()

        # Adding "About" menuItem and setting event
        menuItem = filemenu.Append(wx.ID_ABOUT, "&About",
                                   "Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, menuItem)

        # Adding "Open" and setting event
        menuItem = filemenu.Append(wx.ID_OPEN, "&Open",
                                   "Open simulation state from file")
        self.Bind(wx.EVT_MENU, self.OnOpen, menuItem)

        # Adding "Save as" and setting event
        menuItem = filemenu.Append(wx.ID_SAVE, "&Save as",
                                   "Save simulation state to file")
        self.Bind(wx.EVT_MENU, self.OnSaveAs, menuItem)

        # Adding "Exit" and setting event

        menuItem = filemenu.Append(wx.ID_EXIT, "&Exit",
                                   "Terminate the program")
        self.Bind(wx.EVT_MENU, self.OnExit, menuItem)
        # filemenu.Append()
        # filemenu.Append()

        # Implement other wx.Menu instances here

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")  # Adding "filemenu" to menuBar

        # Add other menus to menubar here
        # -------------------------------

        # --------------------------------

        # Adding ready menubar to frame
        self.SetMenuBar(menuBar)  # Adding menuBar to frame

        # Creating ToolBar
        self.toolbar = self.CreateToolBar()
        self.toolbar.SetToolBitmapSize((20, 10))  # Button size in pixels?
        # Creating 'RUN' button to toolbar. Bitmap needs path from main
        toolItem = self.toolbar.AddLabelTool(self.ID_RUN_BUTTON,
                                             'Run Simulation',
                                             wx.Bitmap('GUI/run_button.png'))
        self.Bind(wx.EVT_MENU, self.OnRun, toolItem)

        # Creating 'Pause' button to toolbar. Bitmap needs path from main
        toolItem = self.toolbar.AddLabelTool(
                                             self.ID_PAUSE_BUTTON,
                                             'Pause Simulation',
                                             wx.Bitmap('GUI/pause_button.png'))
        self.Bind(wx.EVT_MENU, self.OnPause, toolItem)

        self.toolbar.Realize()  # IDIOT U FORGOT TO SHOW IT!!!!!

        # Creating 'Pause' button to toolbar

        # Making frame visible
        self.Show(True)

    def OnAbout(self, event):
        """Show about dialog box"""
        # A message dialog box with an OK button.
        # wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog(self, "Planet simulator version 1.0",
                               "About Planet simulator", wx.OK)
        dlg.ShowModal()  # Show it
        dlg.Destroy()  # finally destroy it when finished.

    def OnOpen(self, event):
        """ Load state from file """
        self.dirname = ''

        dlg = wx.FileDialog(self, "Choose a file",
                            self.dirname, "", "*.*", wx.OPEN)

        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')

            # Now we have bath to selected file
            # simulation.load(f)

            f.close()
        dlg.Destroy()

    def OnSaveAs(self, event):
        self.dirname = ''

        saveFileDialog = wx.FileDialog(self, "Save simulation file",
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
        self.Close(True)

    def OnRun(self, event):
        simulation_speed = 0
        simulation_timestep = 0

        # Asking simulation speed
        dlg = wx.TextEntryDialog(None,
                                 "Set parameters for simulation",
                                 "Run")
        dlg.SetValue("Simulation Speed")

        if dlg.ShowModal() == wx.ID_OK:
            simulation_speed = dlg.GetValue()

        # Asking timestep
        dlg2 = wx.TextEntryDialog(None,
                                  "Still need timestep",
                                  "Run")
        dlg2.SetValue("Simulation Timestep")

        if dlg2.ShowModal == wx.ID_OK:
            simulation_timestep = dlg2.GetValue()
            dlg2.Destroy()
        print("Speed:" + str(simulation_speed) + "\nStep:"
              + str(simulation_timestep))

    def OnPause(self, event):
        pass

if __name__ == '__main__':
    app = wx.App(False)  # Always needs this
    w = MainWindow("Test Frame")
    app.MainLoop()
