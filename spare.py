# -*- coding:utf-8 -*-
"""

@Time    : 2018/3/8 11:59
@Author  : YeJian
@File    : spare.py

"""

#!/usr/bin/env python

import wx


class Frame(wx.Frame):
    pass


class App(wx.App):

    def OnInit(self):
        self.frame=Frame(parent=None, title='Spare')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()

