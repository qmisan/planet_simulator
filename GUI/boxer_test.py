#!/usr/bin/python

# toolbar.py

import wx
from toolbarPanel import ToolbarPanel


class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition,
                          wx.Size(350, 250))

        # Filemenu
        filemenu = wx.Menu()
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")  # Adding "filemenu" to menuBar
        self.SetMenuBar(menuBar)  # Adding menuBar to frame
        menuItem = filemenu.Append(wx.ID_EXIT, "&Exit",
                                   "Terminate the program")

        # Toolbar
        tb_panel = ToolbarPanel(self)

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
        # vbox.Add(panel1,1)

        self.Centre()


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'MyFrame')
        frame.Show(True)
        return True

app = MyApp(0)
app.MainLoop()
