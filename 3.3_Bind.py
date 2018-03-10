# -*- coding:utf-8 -*-
"""

@Time    : 2018/3/10 18:55
@Author  : YeJian
@File    : ttt.py

"""

import wx


class MenuEventFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Menus", pos=wx.DefaultPosition, size=(300, 200))
        menuBar = wx.MenuBar()
        menu = wx.Menu()
        menuitem = menu.Append(-1, "&Exit")
        menuBar.Append(menu, "&File")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnCloseMe, menuitem)

    def OnCloseMe(self, event):
        self.Close(True)


if __name__ == '__main__':
    app = wx.App()
    frame = MenuEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()




