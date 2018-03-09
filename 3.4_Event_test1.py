# -*- coding:utf-8 -*-
"""

@Time    : 2018/3/9 20:01
@Author  : YeJian
@File    : 3.4_test1.py

"""

# 绑定多个鼠标事件

import wx

class MouseEventFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Frame With Button", size=(300, 100))
        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel, label="Not Over", pos=(100, 15))
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick, self.button)  # 绑定按钮事件
        self.button.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)  # 绑定鼠标位于其上事件
        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)  # 绑定鼠标离开事件

    def OnButtonClick(self, event):
        self.panel.SetBackgroundColour("Green")
        self.panel.Refresh()

    def OnEnterWindow(self, event):
        self.button.SetLabel("Over Me!")
        event.Skip()

    def OnLeaveWindow(self, event):
        self.button.SetLabel("Not Over")
        event.Skip()


if __name__ == '__main__':
    # app = wx.PySimpleApp()  报错，替换成 app = wx.App()即可
    app = wx.App()
    frame = MouseEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()


'''
MouseEventFrame包含了一个位于中间的按钮。在其上敲击鼠标将导致框
架的背景色改变为绿色。#1绑定了鼠标敲击事件。当鼠标指针位于这个按钮上
时，按钮上的标签将改变，这用#2绑定。当鼠标离开这个按钮时，标签变回原
样，这用#3绑定。
通过观察上面的鼠标事件例子，我们引出了在wxPython中的事件处理的一
些问题。#1中，按钮事件由附着在框架上的按钮触发，那么wxPython怎么知道
在框架对象中查找绑定而不是在按钮对象上呢？在#2和#3中，鼠标的进入和离
开事件被绑定到了按钮，为什么这两个事件不能被绑到框架上呢。这些问题将
通过检查wxPython用来决定如何响应事件的过程来得到回答
'''

