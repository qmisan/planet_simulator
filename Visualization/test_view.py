import wx
from view import View


def test():
    """
    Testing function for view.py
    """
    local_display_size = wx.GetDisplaySize()
    frame = wx.Frame(parent=None, title="TestFrame",
                     size=(local_display_size[0]/2,
                           0.8*local_display_size[1]), pos=(0, 0))
    view = View(frame)
    view.show()
    frame.Show()

if __name__ =="__main__":
    app = wx.App()
    test()
    app.MainLoop()
