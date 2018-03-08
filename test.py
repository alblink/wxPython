# -*- coding:utf-8 -*-
"""

@Time    : 2018/3/8 11:46
@Author  : YeJian
@File    : test.py

"""

import wx


class App(wx.App):

    def OnInit(self):
        frame = wx.Frame(parent=None, title='Bare')
        frame.Show()
        return True


app = App()

app.MainLoop()

