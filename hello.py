# -*- coding:utf-8 -*-
"""

@Time    : 2018/3/8 12:04
@Author  : YeJian
@File    : hello.py

"""


#!/usr/bin/env python
"""Hello, wxPython! program."""

import wx


class Frame(wx.Frame):  # 2wx.Frame子类
    """Frame class that displays an image."""
    def __init__(self, image, parent=None, id=-1,
                 pos=wx.DefaultPosition, title='Hello, wxPython!'):  # 3图像参数
        """Create a Frame instance and display image."""

        # 4显示图像
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        panel = wx.Panel(self)
        self.bmp = wx.StaticBitmap(parent=panel, bitmap=temp)
        self.SetClientSize(size)


class App(wx.App):  # 5wx.App子类
    """Application class."""
    def OnInit(self):
        # create a image object
        # 6图形处理
        image = wx.Image('234.jpg', wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


def main():  # 7
    app = App()
    app.MainLoop()


if __name__ == '__main__':
    main()

