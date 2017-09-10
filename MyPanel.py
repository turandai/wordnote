import wx

class FullWindowPanel(wx.Panel):
    def __init__(self,parent_frame,panel_stack):
        wx.Panel.__init__(self,parent_frame,size=(300,300))
        self.panel_stack=panel_stack
        wx.Panel.Show(self,False)

    def Show(self,bool):
        if len(self.panel_stack):
            wx.Panel.Show(self.panel_stack[-1],False)
        if bool:
            if self in self.panel_stack:
                self.panel_stack.remove(self)
            self.panel_stack.append(self)
            print(self.panel_stack)
        else:
            if self == self.panel_stack[-1]:
                self.panel_stack.remove(self)
            print(self.panel_stack)
        if len(self.panel_stack):
            wx.Panel.Show(self.panel_stack[-1],True)