import wx
import MainWindow()

class ViewPanel(wx.Panel):
    """
    This implements viewPanel and its functionality
    @param parent
    """
    def __init__(self, parent):
        """
        @param parent: is a wx.Frame instance
        """

        # Self initiate and sizer
        wx.Panel.__init__(self, parent=parent)
        sizer = wx.BoxSizer(wx.HORIZONTAL)



if __name__ == '__main__':
    app = wx.App(False)  # Always needs this
    w = MainWindow("Test Frame")
    app.MainLoop()