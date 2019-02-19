import wx

class BasePanel(wx.Panel):
    def __init__(self,parent_frame,panel_stack,size=(300,300)):
        wx.Panel.__init__(self,parent_frame,size=size)
        self.panel_stack=panel_stack
        wx.Panel.Show(self,False)

    def Show(self,bool):
        if len(self.panel_stack):
            wx.Panel.Show(self.panel_stack[-1],False)
        if bool:
            if self in self.panel_stack:
                self.panel_stack.remove(self)
            self.panel_stack.append(self)
        else:
            if self==self.panel_stack[-1]:
                self.panel_stack.remove(self)
        if len(self.panel_stack):
            wx.Panel.Show(self.panel_stack[-1],True)
