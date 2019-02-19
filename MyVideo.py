import wx
import wx.media

'''
VPanel include a wx.media.MediaCtrl, which use load method to input video

'''
class VPanel(wx.Panel):
    def __init__(self,parent, file, word_info):
        super(VPanel, self).__init__(parent)
        self.parent = parent
        self.vc = wx.media.MediaCtrl(self)
        self.vc.Load(file)
        self.vc.Seek(word_info.time_start)
        self.vc.Play()
        sizer = wx.BoxSizer()
        sizer.Add(self.vc)
        self.SetSizer(sizer)
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.time_check)
        self.shut_down_time = word_info.time_end
        self.timer.Start(100)
        print('aaa')

    def time_check(self, e):
        if self.vc.Tell() > self.shut_down_time:
            self.vc.Stop()
            self.timer.Stop()
            self.Parent.Show(False)
            self.parent.Destroy()

class VideoPlayer(wx.Frame):
    def __init__(self, file, word_info):
        super(VideoPlayer, self).__init__(None)
        self.main_panel = VPanel(self, file, word_info)
        self.Show(1)







#beneth part is used to test
if __name__ == '__main__':
    import MyWorld
    app = wx.App()
    frame = wx.Frame(None)
    VPanel(frame, '/Users/taiyintao/Documents/pythonProjects/worldNote/videoSource/v2.m4v', MyWorld.WorldSearcher('srtSource/v1.srt', 'queen'))
    frame.Show(1)
    app.MainLoop()
