# -*- coding:utf-8 -*-
"""

@Time    : 2018/3/9 18:59
@Author  : YeJian
@File    : 2.7MessageDialog.py

"""

import wx





if __name__ == "__main__":
    app = wx.PySimpleApp()



    # 消息对话框
    # dlg = wx.MessageDialog(None, "Is this explanation OK?",
    #                       'A Message Box',
    #                       wx.YES_NO | wx.ICON_QUESTION)
    # retCode = dlg.ShowModal()
    # if (retCode == wx.ID_YES):
    #     print('yes')
    # else:
    #     print('no')
    # dlg.Destroy()


    # 文本输入对话框
    # dlg = wx.TextEntryDialog(None,
    #                          "Who is buried in Grant's tomb?",
    #                          "A Question",
    #                          "Caty Grant"
    #                          )
    #
    # if dlg.ShowModal() == wx.ID_OK:
    #     response = dlg.GetValue()
    #     print(response)
    #     dlg.Destroy()



    # 从一个列表中选择
    dlg = wx.SingleChoiceDialog(None,
                                "What version of Python are you using?",
                                "Singel Choice",
                                ['1.5.2', '2.0', '2.1.3', '2.2', '2.3.1', '5.1.2'])
    if dlg.ShowModal() == wx.ID_OK:
        response = dlg.GetStringSelection()
        print(response)
        dlg.Destroy()






