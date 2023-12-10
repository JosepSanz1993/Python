class musica:
    def __init__(self,canço_favorita,grup_canço,estil_canço):
        self.__canço = canço_favorita
        self.__grup = grup_canço
        self.__estil = self.__estil_majuscula(estil_canço)
    def __estil_majuscula(self,estil):
        return estil.title()
    def getcanço(self):
        return self.__canço
    def getgrup(self):
        return self.__grup
    def getestil(self):
        return self.__estil
    def setcanço(self,canço):
        self.__canço = canço
    def setgrup(self,grup):
        self.__grup = grup
    def setestil(self, estil):
        self.__estil = estil
    def musicatoString(self):
        print("Musica:\n")
        print("\t Nom canço: "+self.__canço+"\n")
        print("\t Grup Musical: "+self.__grup+"\n")
        print("\t Estil Musical: "+self.__estil+"\n")

