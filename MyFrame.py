import wx
import MyPanel
import MyDate
import MyCalculator
import os
import MyWord
import MyVideo

class MainFrame(wx.Frame):

    def __init__(self):

        '''
        whole class parameters:
            main_panel
            recite_panel
            evaluate_panel
            main_new_word_text
            all_word
            word_number
            panel_stack
        '''

        wx.Frame.__init__(self,None,title='WordNote',size=(300,300),style=wx.CLOSE_BOX | wx.MINIMIZE_BOX)

        self.panel_stack=[]
        self.all_word=[]
        self.word_number=0
####################################### store the video and srt source by arrays
        self.all_source=[]
        self.all_srt=[]
#######################################

        # read data
        with open('data.txt', 'r') as data:
            for line in data.readlines():
                line=line.split()
                line[1]=int(line[1])
                line[2]=int(line[2])
                line[4]=MyCalculator.fade(float(line[4]),MyDate.Date()-MyDate.Date(line[3]))
                self.all_word.append(line)
            self.all_word.sort(key=lambda x:x[4])
            print(self.all_word)

####################################### add source to arrays when class initing
        with open('source.txt', 'r') as source:
            for line in source.readlines():
                self.all_source.append(line[0:line.__len__()-1])
                self.all_srt.append(line[0:line.__len__()-4]+'srt')
            print(self.all_source)
            print(self.all_srt)
#######################################

        self.init_menu()
        
        self.init_main_panel()
        
        panel=wx.Panel(self)
        panel.Bind(wx.EVT_KEY_UP,self.react_key)
        
        self.init_recite_panel()
        
        self.init_evaluate_panel()

        self.Show(True)
        self.Centre()

    def __del__(self):
        with open('data.txt', 'w') as data:
            for line in self.all_word:
                for i in range(5):
                    data.write(str(line[i]))
                    if i == 4:
                        data.write('\n')
                    else:
                        data.write(' ')



    def react_key(self,event):
        print(event)
        if event.GetKeyCode()==27:
            self.panel_stack[-1].Show(False)

    def init_menu(self):


        menubar = wx.MenuBar()
        file_menu = wx.Menu()
        file_item = wx.MenuItem(file_menu, id=wx.ID_ANY, text='See All')
        file_menu.Append(file_item)
        menubar.Append(file_menu, 'Word')
        self.SetMenuBar(menubar)

#main panel
    def init_main_panel(self):
        self.main_panel=MyPanel.BasePanel(self,self.panel_stack)


    #button
        main_button_panel=wx.Panel(self.main_panel,pos=(0,0),size=(300,300))
        button_add=wx.Button(main_button_panel,label='Add',pos=(192,156))
        button_recite=wx.Button(main_button_panel,label='Recite',pos=(25,230))
        button_evaluate=wx.Button(main_button_panel,label='Evaluate',pos=(192,230))

####################################### add source button
        button_expend_source = wx.Button(main_button_panel, label='Add Video', pos=(25,200))
        main_button_panel.Bind(wx.EVT_BUTTON, self.main_react_button_add_video, button_expend_source)
#######################################

        main_button_panel.Bind(wx.EVT_BUTTON,self.main_react_button_add,button_add)
        main_button_panel.Bind(wx.EVT_BUTTON,self.main_react_button_recite,button_recite)
        main_button_panel.Bind(wx.EVT_BUTTON,self.main_react_button_evaluate,button_evaluate)
    #enter text
        self.main_new_word_text=wx.TextCtrl(self.main_panel,size=(150,25),pos=(22,154))
    #other
        bmp=wx.Bitmap('heading.png',wx.BITMAP_TYPE_ANY)
        bmp.SetSize((350,150))
        heading=wx.StaticBitmap(self.main_panel,-1,bmp)
        heading.Center(dir=wx.HORIZONTAL)

        wx.StaticLine(self.main_panel,pos=(10,120),size=(280,10))

        self.main_panel.Show(True)

####################################### add source function
    def main_react_button_add_video(self,e):
        wx.MessageBox('Please put the srt file in the same direction as video\'s.\nAnd use the same name besides suffix', 'You Need To Know', wx.OK)
        dlg = wx.FileDialog(self, message="Choose a media file", defaultDir=os.getcwd(), defaultFile="", )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            if path not in self.all_source:
                self.all_source.append(path)
                self.all_srt.append(path[0:-4]+'.srt')
                print(path)
                file = open('source.txt', 'w')
                for line in self.all_source:
                    file.write(line + '\n')
            else:
                wx.MessageBox('The file have been added already!', 'WARNING', wx.OK)
        dlg.Destroy()
#######################################

    def main_react_button_add(self,event):
        new_word=self.main_new_word_text.GetLineText(0).strip().lower()
        added=False
        for word in self.all_word:
            if word[0]==new_word:
                added=True
                break
        if new_word.isalpha() and not added:
            print(new_word+' is added')
            date_now=MyDate.Date()
            self.all_word.append([new_word,0,0,date_now.get_date(),0])
            print(self.all_word)

    def main_react_button_recite(self,event):
        self.recite_panel.Show(True)

    def main_react_button_evaluate(self,event):
        self.evaluate_panel.Show(True)

#recite panel
    def init_recite_panel(self):
        self.recite_panel=MyPanel.BasePanel(self,self.panel_stack)
    #button
        recite_button_panel=wx.Panel(self.recite_panel,size=(300,300))
        button_no=wx.Button(recite_button_panel,label='No',pos=(30,190))
        button_yes=wx.Button(recite_button_panel,label='Yes',pos=(192,190))

####################################### play video button
        button_video=wx.Button(recite_button_panel,label='video', pos=(30,230))
        recite_button_panel.Bind(wx.EVT_BUTTON,self.recite_react_button_video,button_video)
#######################################

        recite_button_panel.Bind(wx.EVT_BUTTON,self.recite_react_button_no,button_no)
        recite_button_panel.Bind(wx.EVT_BUTTON,self.recite_react_button_yes,button_yes)
        wx.StaticLine(self.recite_panel,pos=(10,120),size=(280,10))
    #word
        word_panel=wx.Panel(self.recite_panel,size=(300,180))
        #word_panel.SetBackgroundColour('black')
        recite_font=wx.Font(45,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)
        self.word=wx.StaticText(word_panel,label=self.all_word[self.word_number][0])
        self.word.SetForegroundColour((120,120,120))
        self.word.SetFont(recite_font)
        self.word.CenterOnParent()

    def recite_react_button_no(self,event):
        self.all_word[self.word_number][2]+=1
        self.all_word[self.word_number][3]=MyDate.Date().get_date()
        self.all_word[self.word_number][4]=MyCalculator.update(self.all_word[self.word_number][4],-1)
        self.word_number+=1
        if self.word_number>=len(self.all_word):
            self.word_number=0
        self.word.SetLabel(self.all_word[self.word_number][0])
        self.word.CenterOnParent()
        print(self.all_word)

    def recite_react_button_yes(self,event):
        self.all_word[self.word_number][1]+=1
        self.all_word[self.word_number][3]=MyDate.Date().get_date()
        self.all_word[self.word_number][4]=MyCalculator.update(self.all_word[self.word_number][4],5)
        self.word_number+=1
        if self.word_number>=len(self.all_word):
            self.word_number=0
        self.word.SetLabel(self.all_word[self.word_number][0])
        self.word.CenterOnParent()
        print(self.all_word)

####################################### play video function
    def recite_react_button_video(self, e):
        times = 0
        while self.all_source.__len__() > 0:
            word = MyWord.WordSearcher(self.all_srt[times], self.word.Label)

            if word.total != 0:
                MyVideo.VideoPlayer(self.all_source[times], word)
                break
            elif self.all_srt[times] == self.all_srt[-1]:
                wx.MessageBox('Sorry, we can\'t find this word in your videos, \nplease expend your video repertory and try again', 'ops!', wx.OK)
                self.main_react_button_add_video(wx.EVT_BUTTON)
                break
            times += 1
        if self.all_source.__len__() == 0:
            self.main_react_button_add_video(wx.EVT_BUTTON)
#######################################

#evaluate panel
    def init_evaluate_panel(self):
        self.evaluate_panel=MyPanel.BasePanel(self,self.panel_stack)


