class Date():
    def __init__(self, month,day,year):
        self.__month = month
        self.__day = day
        self.__year = year
        
    def setMonth(self, newMonth):
        self.__month=newMonth
        
    def setDay(self, newDay):
        self.__day=newDay
        
    def setYear(self, newYear):
        self.__year=newYear    
        
    def getMonth(self):
        return self.__month
    def getDay(self):
        return self.__day
    def getYear(self):
        return self.__year 
        
    def toString(self):
        print(self.__month,"\\",self.__day,"\\",self.__year,end=" ")
