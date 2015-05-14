import wx  # wx.Frame etc
import os  # To get path for "Open file"
from visual import *
from toolbarPanel import ToolbarPanel
from Simulation.simulation import Simulation
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
    screen_size = wx.GetDisplaySize()

    # Simulation
    simulation = None
    simulation_speed = 0
    simulation_timestep = 0
    frequency = 0

    # Flags
    toolbarheight = 10
    state_saved = False
    scene = None
    simulation_stopped = False

    # Datapanel
    datapanel = None

    def __init__(self, title):

        # Frame initialization
        # Get local display size NOTE: Local display size not needed if always fullscreen
        # local_display_size = wx.GetDisplaySize()
        # print(local_display_size)
        # Initialize mainwindow
        window.__init__(self, title="Planet Simulator", _make_panel=True, width = self.screen_size[0],
                        height = self.screen_size[1] ) # kw _make_panel=False

        # Set icon
        self.win.SetIcon(wx.Icon('planet.ico', wx.BITMAP_TYPE_ICO))
        # Makes program constant fullscreen
        self.fullscreen = True

        self.SetMenubar()
        self.SetToolbar()
        self.SetDisplay()
        self.SetStart()
        self.SetCheckBox()
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

        # labelTool = toolbar.AddCheckTool(wx.ID_ANY,
        #                                  'Labels on simulation')

        # self.win.Bind(wx.EVT_CHECKBOX, self.ShowOrHideLabels)

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
            self.SetDataPanel()

            # Makes display for visualization
            # TODO: Need to dock display to mainWindow
            # self.SetDisplay()

            # Make visuals to all elements and add them rendering space
            # self.simulation.make_visuals()
            # self.simulation.render()
            # rate =
        self.state_saved = True
        self.simulation_stopped = False
        dlg.Destroy()
        while(True):
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

        if not self.simulation_stopped == True:
            self.simulation_speed = 0
            self.simulation_timestep = 0

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
                self.simulation_speed = int(dlg.GetValue())
                if not isinstance(self.simulation_speed, int):
                    pass
                    # raise WrongSimulationParameterError("")

            # Asking simulation speed
            dlg2 = wx.TextEntryDialog(None, "Set timestep (seconds)", "Run")
            dlg2.SetValue("1")

            if dlg2.ShowModal() == wx.ID_OK:
                self.simulation_timestep = int(dlg2.GetValue())
                if not isinstance(self.simulation_timestep, int):
                    pass
                    # raise WrongSimulationParameterError("")

            # Asking rendering frequency
            dlg3 = wx.TextEntryDialog(None, "Set rendering frequency", "Run")
            dlg3.SetValue("2")

            if dlg3.ShowModal() == wx.ID_OK:
                self.frequency = int(dlg3.GetValue())
                if not isinstance(self.frequency, int):
                    pass
                    # raise WrongSimulationParameterError("")

            self.simulation.run(self.simulation_speed, self.simulation_timestep, self.frequency)

        # If simulation is only stopped
        else:
            self.simulation.run(self.simulation_speed, self.simulation_timestep, self.frequency)

    def OnPause(self, event):
        if self.simulation == None or self.simulation_stopped == True:
            pass
        else:
            self.simulation.stop()


    def SetDisplay(self):
        # Display
        self.scene = display(window=self, width=0.8*self.screen_size[0],
                             height = 0.8*self.screen_size[1], autoscale=True)

    def SetStart(self):
        # Backgroundcolor to white
        # self.scene.background(color.white)

        # Text
        text(text='Welcome to planet simulator!',
             align='center', depth=-0.3, color=color.green)
        planet1 = sphere(pos=(5,-5,-5))
        planet1.material = materials.emissive
        planet1.color = color.yellow
        planet2 = sphere(pos=(-5,-5,-5),material=materials.earth)

    def OnCenter(self, event, element):
        self.simulation.center(element)


    def SetCheckBox(self):
        # Set checkbox to ask if user wants labels in run
        # NOTE: This could be in toolbar
        print(self.screen_size)
        cb = wx.CheckBox(self.panel, label="Labels", pos=(200,int(self.screen_size[1]*0.83)))


        cb.Bind(wx.EVT_CHECKBOX, self.ShowOrHideLabels)

    def ShowOrHideLabels(self, event):
        sender = event.GetEventObject()
        isChecked = sender.GetValue()
        if not self.simulation == None:
            if isChecked:
                self.labels = True
                for element in self.simulation.space.element_list:
                    element.visual.label.visible = True
            else:
                self.labels = False
                for element in self.simulation.space.element_list:
                        element.visual.label.visible = False

    def SetDataPanel(self):
        # Delete old
        if not self.datapanel == None:
            self.datapanel.Destroy()
            self.datapanel = None

        self.datapanel = wx.Panel(self.win,
                                  pos=(0.8*int(self.screen_size[0]),0),
                                  size=(0.2*self.screen_size[0],
                                  0.8*self.screen_size[1]))

        self.datapanel.SetBackgroundColour("RED")
        sizer = wx.BoxSizer(wx.VERTICAL)
        box = wx.StaticBox(self.datapanel,label="self.Datapanel",pos=(5,5),size=(240,0))
        st = wx.StaticText(self.datapanel,label="Information about elements in space\n(Press element to center it on scene)")

        L = 100

        i = 0
        for element in self.simulation.space.element_list:
            button = wx.Button(self.datapanel,-1,label=element.label+"\nMass: "+str(element.mass),
                                pos = (0,i*100+L))
            # sizer.Add(button, wx.EXPAND|wx.ALL)
            def OnButton(self, event, center_element=element):
                print("U pressed:"+element.label)
                self.simulation.center(element)

            button.Bind(wx.EVT_BUTTON, OnButton)

            i = i+1
        box.size = (240,i*100+L+20)
        # self.datapanel.SetSizer(sizer)
        # self.datapanel.Fit()
        self.datapanel.Show()


