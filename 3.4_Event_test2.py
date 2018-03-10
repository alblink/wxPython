# -*- coding:utf-8 -*-
"""

@Time    : 2018/3/9 20:23
@Author  : YeJian
@File    : 3.4_test2.py

"""

# 同时相应鼠标按下和按钮敲击

import wx


class DoubleEventFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame With Button', size=(300, 100))
        self.panel = wx.Panel(self, -1)
        self.button = wx.Button(self.panel, -1, 'Click Me', pos=(100, 15))
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick, self.button)    # 1 绑定按钮敲击事件                           
        self.button.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)  # 2 绑定鼠标左键按下事件

    def OnButtonClick(self, event):
        self.panel.SetBackgroundColour("Green")
        self.panel.Refresh()

    def OnMouseDown(self, event):
        self.button.SetLabel("Again!")
        event.Skip()  # 3 确保继续处理   


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = DoubleEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()


"""
#1 这行绑定按钮敲击事件到OnButtonClick()处理器，这个处理器改变框架
的背景色。
#2 这行绑定鼠标左键按下事件到OnMouseDown()处理器，这个处理器改变
按钮的标签文本。由于鼠标左键按下事件不是命令事件，所以它必须被绑定到
按钮（self.button.Bind）而非框架（self.Bind）。

当用户在按钮上敲击鼠标时，通过直接与底层操作系统交互，鼠标左键按
下事件首先被产生。通常情况下，鼠标左键按下事件改变按钮的状态，随着鼠
标左键的释放，产生了wx.EVT_BUTTON敲击事件。由于行#3的Skip()语
句，DoubleEventFrame维持处理。没有Skip()语句，事件处理规则发现在#2创建
的绑定，而在按钮能产生wx.EVT_BUTTON事件之前停止。由于Skip()的调
用，事件处理照常继续，并且按钮敲击被创建。
记住，当绑定低级事件时如鼠标按下或释放，wxPython期望捕获这些低级
事件以便生成进一步的事件，为了进一步的事件处理，你必须调用Skip()方
法，否则进一步的事件处理将被阻止。
"""
