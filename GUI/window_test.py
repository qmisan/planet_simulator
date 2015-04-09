from visual import *
import wx


class Window(window):
    def __init__(self):
        local_display_size = wx.GetDisplaySize()
        window.__init__(self, parent=None, title="Test Frame",
                        size=(local_display_size[0]/2,
                              0.8*local_display_size[1]),
                        _make_panel=False)
        self.win.Centre()
        panel = wx.Panel(self.win, -1)
        scene = display(window = panel)
        
        panel.SetBackgroundColour("YELLOW")

        panel2 = wx.Panel(self.win, -1)
        panel2.SetBackgroundColour("BLUE")
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(panel, 1, wx.EXPAND)
        sizer.Add(panel2, 1, wx.EXPAND)

        sizer.Add((-1,500))
        self.win.SetSizer(sizer)


if __name__ == '__main__':
    app = wx.App(False)  # Always needs this
    Window()
    app.MainLoop()
