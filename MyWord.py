import codecs
import re

'''
This class is used to find lines and it's time from srt file
WorldSearcher class require two parameters, 
'file' represents the directory as string, 
'world' represents the target world as string.


The 'results' function will return a array include all temples with time and sentence.
e.g:
[('00:41:56,540 --> 00:42:00,540\r\n', '龙母非常美丽\r\n'), ('00:51:16,870 --> 00:51:19,250\r\n', '找一座恬静  美丽的小岛\r\n')]


The total attribute is the total of results.
'''
class WordSearcher():
    def __init__(self, file, word):
        self.target_word = word.lower()
        self.target_file = file
        self.time_scale = []
        self.if_illeage()
        self.total = self.time_scale.__len__()
        if self.total != 0:
        #the first time,just for test
            self.time_start = self.start_time()
            self.time_end = self.end_time()
        else:
            self.time_end = 0
            self.time_start = 0

    def if_illeage(self):
        if self.target_word.find('-->') == -1:
            self.search_word()

    def search_word(self):
        file = codecs.open(self.target_file, 'r', 'gb18030')
        judge1 = True
        judge2 = True
        while judge2:
            if judge1 == True:
                pos_time = file.readline()
            else:
                pos_time = pos_line
            while pos_time.find('-->') != -1:
                pos_line = file.readline()
                pos_line = pos_line.lower()
                pattern = '[^a-z]' + self.target_word + '[^a-z]'
                if  re.search(pattern=pattern, string=pos_line):
                    self.time_scale.append((pos_time, ' ' + pos_line + ' '))

                elif pos_line.find('-->') != -1:
                    judge1 = False
                    break
                elif not len(pos_line):
                    judge2 = False
                    break
        file.close()
    def results(self):
        return self.time_scale


    def start_time(self):
        h = int(self.time_scale[0][0][0:2]) * 3600
        m = int(self.time_scale[0][0][3:5]) * 60
        s = h + m + int(self.time_scale[0][0][6:8]) - 5
        return s * 1000

    def end_time(self):
        h = int(self.time_scale[0][0][17:19]) * 3600
        m = int(self.time_scale[0][0][20:22]) * 60
        s = h + m + int(self.time_scale[0][0][23:25]) + 5
        return s * 1000


#Beneath part is for testing
if __name__ == '__main__':
    srt1 = WordSearcher('srtSource/v1.srt', 'queen')
    print(srt1.results(), srt1.total)
    print(srt1.time_start)
    print(srt1.time_end)
