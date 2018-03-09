# -*- coding:utf-8 -*-
"""

@Time    : 2018/3/9 20:39
@Author  : YeJian
@File    : 3.4_Event_test3.py

"""

import wx
class TwoButtonEvent(wx.PyCommandEvent):    #1 定义事件
    def __init__(self, evtType, id):
        wx.PyCommandEvent.__init__(self, evtType, id)
        self.clickCount = 0

    def GetClickCount(self):
        return self.clickCount
    def SetClickCount(self, count):
        self.clickCount = count

myEVT_TWO_BUTTON = wx.NewEventType() #2 创建一个事件类型
EVT_TWO_BUTTON = wx.PyEventBinder(myEVT_TWO_BUTTON, 1)  #3 创建一个绑定器对象


class TwoButtonPanel(wx.Panel):
    def __init__(self, parent, id=-1, leftText="Left", rightText="Right"):
        wx.Panel.__init__(self, parent, id)
        self.leftButton = wx.Button(self, label=leftText)
        self.rightButton = wx.Button(self, label=rightText,
        pos=(100,0))
        self.leftClick = False
        self.rightClick = False
        self.clickCount = 0
#4 下面两行绑定更低级的事件
        self.leftButton.Bind(wx.EVT_LEFT_DOWN, self.OnLeftClick)
        self.rightButton.Bind(wx.EVT_LEFT_DOWN, self.OnRightClick)
    def OnLeftClick(self, event):
        self.leftClick = True
        self.OnClick()
        event.Skip()    #5 继续处理


    def OnRightClick(self, event):
        self.rightClick = True
        self.OnClick()
        event.Skip()    #6 继续处理

    def OnClick(self):
        self.clickCount += 1
        if self.leftClick and self.rightClick:
            self.leftClick = False
            self.rightClick = False
            evt = TwoButtonEvent(myEVT_TWO_BUTTON, self.GetId()) #7 创建自定义事件
            evt.SetClickCount(self.clickCount)  # 添加数据到事件
            self.GetEventHandler().ProcessEvent(evt)    #8 处理事件


class CustomEventFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Click Count: 0',
        size=(300, 100))
        panel = TwoButtonPanel(self)
        self.Bind(EVT_TWO_BUTTON, self.OnTwoClick, panel) #9 绑定自定义事件

    def OnTwoClick(self, event):    #10 定义一个事件处理器函数
        self.SetTitle("Click Count: %s" % event.GetClickCount())

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CustomEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()



"""
说明：
    #1 这个关于事件类的构造器声明为wx.PyCommandEvent的一个子
类。 wx.PyEvent和wx.PyCommandEvent是wxPython特定的结构，你可以用来创
建新的事件类并且可以把C++类和你的Python代码连接起来。如果你试图直接
使用wx.Event，那么在事件处理期间wxPython不能明白你的子类的新方法，因

为C++事件处理不了解该Python子类。如果你wx.PyEvent，一个对该Python实例
的引用被保存，并且以后被直接传递给事件处理器，使得该Python代码能被使
用。
    #2 全局函数wx.NewEventType()的作用类似于wx.NewId()；它返回一个唯
一的事件类型ID。这个唯一的值标识了一个应用于事件处理系统的事件类型。
    #3 这个绑定器对象的创建使用了这个新事件类型作为一个参数。这第二个
参数的取值位于[0,2]之间，它代表wxId标识号，该标识号用于
wx.EvtHandler.Bind()方法去确定哪个对象是事件的源。
    #4 为了创建这个新的更高级的命令事件，程序必需响应特定的用户事件，
例如，在每个按钮对象上的鼠标左键按下。依据哪个按钮被敲击，该事件被绑
定到OnLeftClick()和OnRightClick()方法。处理器设置了布尔值，以表明按键是
否被敲击。
    #5 #6 Skip()的调用允许在该事件处理完成后的进一步处理。在这里，这个
新的事件不需要skip调用；它在事件处理器完成之前被分派了(self.OnClick())。
但是所有的鼠标左键按下事件需要调用Skip()，以便处理器不把最后的按钮敲
击挂起。这个程序没有处理按钮敲击事件，但是由于使用了Skip()，wxPython
在敲击期间使用按钮敲击事件来正确地绘制按钮。如果被挂起了，用户将不会
得到来自按钮按下的反馈。
    #7 如果两个按钮都被敲击了，该代码创建这个新事件的一个实例。事件类
型和两个按钮的ID作为构造器的参数。通常，一个事件类可以有多个事件类
型，尽管本例中不是这样。
    #8 ProcessEvent()的调用将这个新事件引入到事件处理系统
中，ProcessEvent()的说明见3.4.1节。GetEventHandler()调用返回wx.EvtHandler
的一个实例。大多数情况下，返回的实例是窗口部件对象本身，但是如果其它
的wx.EvtHandler()方法已经被压入了事件处理器堆栈，那么返回的将是堆栈项
的项目。
    #9 该自定义的事件的绑定如同其它事件一样，在这里使用#3所创建的绑定
器。
    #10 这个例子的事件处理器函数改变窗口的标题以显示敲击数。
至此，你的自定义的事件可以做任何预先存在的wxPython事件所能做的
事，比如创建不同的窗口部件，它们响应同样的事件。创建事件是wxPython的
定制的一个重要部分。
"""

