from Date import Date 
class Student():
    def __init__(self, name,date,score):
        self.__name = name
        self.__date = date
        self.__score = score
        
    def setName(self, newName):
        self.__name=newName
    def setDate(self, newDate):
        self.__date=newDate
    def setScore(self, newScore):
        self.__score=newScore    
        
    def getName(self):
        return self.__name
    def getDate(self):
        return self.__date
    def getScore(self):
        return self.__score 
        
    def toString(self):
        print (self.getName(),end=" ")
        (self.getDate().toString())
        print (self.getScore())
