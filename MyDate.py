import datetime

class Date():

    def __init__(self,load=''):
        self.__leap_year=False
        if load!='':
            self.__date=load
        else:
            time=datetime.datetime.now()
            self.__date=str(time)[:10].replace('-','')
        self.year=int(self.__date[:4])
        self.month=int(self.__date[4:6])
        self.day=int(self.__date[6:])
        if (self.year%4==0 and self.year%100!=0) or self.year%400==0:
            self.__leap_year=True
            feb=29
        feb=28
        self.table=[31,feb,31,30,31,30,31,31,30,31,30,31]


    def __sub__(self,other):
        difference=0
        dif_year=self.year-other.year
        dif_month=self.month-other.month
        dif_day=self.day-other.day
        #print(dif_year,dif_month,dif_day)
        if dif_year!=0:
            difference+=dif_year*365
            if dif_year>0 and other.is_leap_year:
                difference+=1
            elif dif_year<0 and self.is_leap_year():
                difference-=1
        if dif_month!=0:
            if dif_month>0:
                for i in range(other.month,self.month):
                    difference+=other.table[i-1]
            else:
                for i in range(self.month,other.month):
                    difference-=self.table[i-1]
        if dif_day!=0:
            difference+=dif_day
        return difference


    def get_date(self):
        return self.__date

    def is_leap_year(self):
        return self.__leap_year
