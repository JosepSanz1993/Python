class music:
    def __init__(self,name,mean_author,other_author,year,week,country,lenguage,continet):
        self.__name = name
        self.__author = mean_author
        self.__other_Author = other_author
        self.__year = year
        self.__week = week
        self.__country = country
        self.__lenguage = lenguage
        self.__continet = continet
    def getname(self):
        return self.__name
    def getyear(self):
        return self.__year
    def getweek(self):
        return self.__week
    def getcountry(self):
        return self.__country
    def getlenguage(self):
        return self.__lenguage
    def getcontinet(self):
        return self.__continet
    def getauthor(self):
        return self.__author
    def getotherauthor(self):
        return self.__other_Author
    
