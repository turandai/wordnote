import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title='wordnote',size=(300,300),style=wx.CLOSE_BOX | wx.MINIMIZE_BOX)
        self.Show(True)
        self.Centre()
        self.init_main_panel()
        self.main_panel.Show(True)
        self.init_recite_panel()
        self.recite_panel.Show(False)

        # menu
        menubar = wx.MenuBar()
        file_menu = wx.Menu()
        file_item = wx.MenuItem(file_menu, id=wx.ID_ANY, text='See All')
        file_menu.Append(file_item)
        menubar.Append(file_menu, 'Word')
        self.SetMenuBar(menubar)

    def init_main_panel(self):
        self.main_panel=wx.Panel(self,size=(300,300))

    #button
        main_button_panel=wx.Panel(self.main_panel,pos=(0,0),size=(300,300))
        button_add=wx.Button(main_button_panel,label='Add',pos=(192,156))
        button_recite=wx.Button(main_button_panel,label='Recite',pos=(25,230))
        button_evaluate=wx.Button(main_button_panel,label='Evaluate',pos=(192,230))
        main_button_panel.Bind(wx.EVT_BUTTON,self.main_react_button_add,button_add)
        main_button_panel.Bind(wx.EVT_BUTTON,self.main_react_button_recite,button_recite)
        main_button_panel.Bind(wx.EVT_BUTTON,self.main_react_button_evaluate,button_evaluate)
    #enter text
        self.main_new_word_text=wx.TextCtrl(self.main_panel,size=(150,25),pos=(22,154))
    #read data
        with open('/Users/turan/Documents/study/programming/pc/wordnote/data.txt','r') as data:
            self.all_word=data.readlines()
            print(self.all_word)
    #other
        heading=wx.StaticText(self.main_panel,label='welcome to\n          wordnote',pos=(12,5))
        heading.SetForegroundColour((120,120,120))
        heading_font=wx.Font(35,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)
        heading.SetFont(heading_font)
        wx.StaticLine(self.main_panel,pos=(10,120),size=(280,10))

    def main_react_button_add(self,event):
        new_word=self.main_new_word_text.GetLineText(0).strip().lower()
        if new_word.isalpha() and new_word+'\n' not in self.all_word:
            print(new_word+' is added')
            self.all_word.append(new_word+'\n')
            with open('/Users/turan/Documents/study/programming/pc/wordnote/data.txt','w') as data:
                data.writelines(self.all_word)
            print(self.all_word)

    def main_react_button_recite(self,event):
        self.main_panel.Show(False)
        self.recite_panel.Show(True)

    def main_react_button_evaluate(self,event):
        print('evaluate')

    def init_recite_panel(self):
        self.recite_panel=wx.Panel(self,size=(300,300))
    #button
        recite_button_panel=wx.Panel(self.recite_panel,pos=(-1,130))
        buttons=[]
        button_no=wx.Button(recite_button_panel,label='No')
        button_yes=wx.Button(recite_button_panel,label='Yes')
        button_spell=wx.Button(recite_button_panel,label='Spell')
        buttons.append(button_no)
        buttons.append(button_yes)
        buttons.append(button_spell)
        sizer=wx.BoxSizer(wx.HORIZONTAL)
        for i in range(0,len(buttons)):
            sizer.Add(buttons[i],flag=wx.ALL,border=8)
        recite_button_panel.SetSizer(sizer)
        sizer.Fit(recite_button_panel)
        recite_button_panel.Bind(wx.EVT_BUTTON,self.recite_react_button_no,button_no)
        recite_button_panel.Bind(wx.EVT_BUTTON,self.recite_react_button_yes,button_yes)
        recite_button_panel.Bind(wx.EVT_BUTTON,self.recite_react_button_spell,button_spell)

    def recite_react_button_no(self,event):
        print('no')

    def recite_react_button_yes(self,event):
        print('yes')

    def recite_react_button_spell(self, event):
        print('spell')

