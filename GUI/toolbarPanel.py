import wx

class ToolbarPanel(wx.Panel):
    """
    This implements viewPanel and its functionality
    @param parent
    """
    def __init__(self, parent):
        """
        @param parent: is a wx.Frame instance
        """

        # Self initiate and sizers
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent
        self.controlSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.runButton = wx.Button(self, label="Run")
        self.runButton.Bind(wx.EVT_BUTTON, self.onRunWidget)
        self.controlSizer.Add(self.runButton, 0, wx.CENTER | wx.ALL, 5)

        self.pauseButton = wx.Button(self, label="Pause")
        self.pauseButton.Bind(wx.EVT_BUTTON, self.onPauseWidget)
        self.controlSizer.Add(self.pauseButton, 0, wx.CENTER | wx.ALL, 5)

        self.SetSizer(self.controlSizer)

    def onRunWidget(self, event):
        """Run simulation"""
        pass

    def onPauseWidget(self, event):
        """Pause simulation"""
        pass

if __name__ == '__main__':
    app = wx.App(False)  # Always needs this
    w = MainWindow("Test Frame")
    app.MainLoop()