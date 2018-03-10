# -*- coding:utf-8 -*-
"""

@Time    : 2018/3/10 21:13
@Author  : YeJian
@File    : 11.11_Sizer.py

"""

import wx
class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Real World Test")
        panel = wx.Panel(self)
        # First create the controls
        topLbl = wx.StaticText(panel, -1, "Account Information")#1 创建窗口部件
        topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        nameLbl = wx.StaticText(panel, -1, "Name:")
        name = wx.TextCtrl(panel, -1, "");
        addrLbl = wx.StaticText(panel, -1, "Address:")
        addr1 = wx.TextCtrl(panel, -1, "");
        addr2 = wx.TextCtrl(panel, -1, "");
        cstLbl = wx.StaticText(panel, -1, "City, State, Zip:")
        city = wx.TextCtrl(panel, -1, "", size=(150,-1));
        state = wx.TextCtrl(panel, -1, "", size=(50,-1));
        zip = wx.TextCtrl(panel, -1, "", size=(70,-1));
        phoneLbl = wx.StaticText(panel, -1, "Phone:")
        phone = wx.TextCtrl(panel, -1, "");
        emailLbl = wx.StaticText(panel, -1, "Email:")
        email = wx.TextCtrl(panel, -1, "");
        saveBtn = wx.Button(panel, -1, "Save")
        cancelBtn = wx.Button(panel, -1, "Cancel")
        # Now do the layout.
        # mainSizer is the top-level one that manages everything
    #2 垂直的sizer
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(topLbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(panel), 0,
                wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        # addrSizer is a grid that holds all of the address info
    #3 地址列
        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)
        addrSizer.Add(nameLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(name, 0, wx.EXPAND)
        addrSizer.Add(addrLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)

        addrSizer.Add(addr1, 0, wx.EXPAND)
    #4 带有空白空间的行
        addrSizer.Add((10,10)) # some empty space
        addrSizer.Add(addr2, 0, wx.EXPAND)
        addrSizer.Add(cstLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        # the city, state, zip fields are in a sub-sizer
    #5 水平嵌套
        cstSizer = wx.BoxSizer(wx.HORIZONTAL)
        cstSizer.Add(city, 1)
        cstSizer.Add(state, 0, wx.LEFT|wx.RIGHT, 5)
        cstSizer.Add(zip)
        addrSizer.Add(cstSizer, 0, wx.EXPAND)
    #6 电话和电子邮箱
        addrSizer.Add(phoneLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(phone, 0, wx.EXPAND)
        addrSizer.Add(emailLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(email, 0, wx.EXPAND)
        # now add the addrSizer to the mainSizer
    #7 添加Flex sizer
        mainSizer.Add(addrSizer, 0, wx.EXPAND|wx.ALL, 10)
        # The buttons sizer will put them in a row with resizeable
        # gaps between and on either side of the buttons
    #8 按钮行
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(saveBtn)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(cancelBtn)
        btnSizer.Add((20,20), 1)
        mainSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
        panel.SetSizer(mainSizer)

        # Fit the frame to the needs of the sizer.  The frame will
        # automatically resize the panel as needed.  Also prevent the
        # frame from getting smaller than this size.
        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)
app = wx.PySimpleApp()
TestFrame().Show()
app.MainLoop()


"""
    #1 代码的第一部分是创建使用在窗口中的窗口部件，它们在这行开始。我
们在增加sizer前将它们全部创建。
    #2 在这个布局中的主sizer是mainSizer，它是一个竖直的box sizer。被添加
到mainSizer的第一个元素是顶部的静态文本标签和一个static line。
    #3 在box sizer中接下来的元素是addrSizer，它是一个flex grid sizer，它有两
列，它两列用于容纳其余的地址信息。addrSizer的左列被设计用于静态文本标
签，而右列用于得到文本控件。这意味着标签和控件需要被交替的添加，以保
证grid的正确。你可以看到nameLbl, name, addrLbl, 和addr1是首先被添加到该
flex grid中的四个元素。
    #4 这接下来的行是不同的，因为这第二个地址行没有标签，一个(10,10)尺
寸的空白块被添加，然后是addr2控件。
    #5 接下来的行又有所不同，包括“City, State, Zip”的行要求三个不同的文本
控件，基于这种情况，我们创建了一个水平的box sizer：cstSizer。这三个控件
被添加给cstSizer，然后这个box sizer被添加到addrSizer。
    #6 电话和电子邮箱行被添加到flex sizer。
    #7 有关地址的flex sizer被正式添加到主sizer。
    #8 按钮行作为水平box sizer被添加，其中有一些空白元素以分隔按钮。
在调整了sizer（mainSizer.Fit(self)）和防止框架变得更小之后
（mainSizer.SetSizeHints(self)），元素的布局就结束了。
在读这接下来的段落或运行这个例子之前，请试着想出该框架将会如何在
水平和竖直方向上响应增长。
如果该窗口在竖直方向上的大小改变了，其中的元素不会移动。这是因为
主sizer是一个垂直的box sizer，你是在它的主方向上改变尺寸，它没有一个顶
级元素是以大于0的比列被添加的。如果这个窗口在水平方向被调整尺寸，由
于这个主sizer是一个垂直的box sizer，你是在它的次方向改变尺寸，因此它的
所有有wx.EXPAND标记的元素将水平的伸展。这意味着顶部的标签不增长，
但是static line和子sizer将水平的增长。用于地址的flex grid sizer指定列1是可增
长的，这意味着包含文本控件的第二列将增长。在“City, State, Zip” 行内，比列
为1的city元素将伸展，而state和ZIP控件将保持尺寸不变。按钮将保持原有的尺
寸，因为它们的比列是0，但是按钮所在行的空白空间将等分地占据剩下的空
间，因为它们每个的比列都是1。
"""
