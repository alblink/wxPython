# -*- coding:utf-8 -*-
"""

@Time    : 2018/3/8 15:12
@Author  : YeJian
@File    : chongdingxiang.py

"""

# !/usr/bin/env python
import wx
import sys


class Frame(wx.Frame):
    def __init__(self, parent, id, title):
        print('Frame __init__')
        wx.Frame.__init__(self, parent, id, title)


class App(wx.App):

    def __init__(self, redirect=True, filename=None):
        print('App __init__')
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        print('OnInit')
        self.frame = Frame(parent=None, id=-1, title='Startup')  # 创建框架
        self.frame.Show()
        self.SetTopWindow(self.frame)
        sys.stderr.write("A pretend error message")
        return True

    def OnExit(self):
        print('OnExit')


if __name__ == '__main__':
    app = App(redirect=True)  # 文本重定向从这开始
    print('before MainLoop')
    app.MainLoop()
    print('after MainLoop')

