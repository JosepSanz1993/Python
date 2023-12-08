class dades_personals:
    def __init__(self,nom_cognoms,dni,poblacio,pais):
        self.__nom_cognoms = self.__comprovacio_primera_lletra_majuscula(nom_cognoms)
        self.__dni = self.__comprovacio_dni(dni)
        self.__poblacio = self.__comprovacio_primera_lletra_majuscula(poblacio)
        self.__pais = self.__comprovacio_tot_majuscula(pais)
    def __comprovacio_primera_lletra_majuscula(self,text):
        if text.istitle()==False:
           result = text.title()
        else:
            result = text
        return result
    def __comprovacio_tot_majuscula(self,text):
        if text.isupper()==False:
           result = text.upper()
        else:
            result = text
        return result
    def __demanar_dni(self):
        digit = str(input("Torna afegir els 8 digits del dni:\n"))
        lletra = input("Afegeix la lletra en majuscula:\n")
        dni = digit+lletra
        return dni
    def __comprovacio_dni(self, dni):
        mida = len(dni)
        digits = dni.split(dni[mida-1])[0]
        if mida !=9:
            print("EL DNI te 9 caracters\n")
            dni = self.__demanar_dni()
            self.__comprovacio_dni(dni)
        elif digits.isdigit() == False:
            print("Els 8 primers caracteres tenen que ser numerics\n")
            dni = self.__demanar_dni()
            self.__comprovacio_dni(dni)
        elif dni[mida-1].isalpha()== False and dni[mida-1].isupper()== False:
            print("L'ultim caracter te que ser una lletra en majuscula\n")
            dni = self.__demanar_dni()
            self.__comprovacio_dni(dni)    
        return dni
    def getnomcognoms(self):
        return self.__nom_cognoms
    def getdni(self):
        return self.__dni
    def getpoblacio(self):
        return self.__poblacio
    def getpais(self):
        return self.__pais
    def setnomcognoms(self,nom):
        self.__nom_cognoms = self.__comprovacio_primera_lletra_majuscula(nom)
    def setdni(self,dni):
        self.__dni = self.__comprovacio_dni(dni)
    def setpoblacio(self,poblacio):
        self.__poblacio = self.__comprovacio_primera_lletra_majuscula(poblacio)
    def setpais(self,pais):
        self.__pais = self.__comprovacio_tot_majuscula(pais)
    def dadespersonalstoString(self):
        print("Dades Personals:\n")
        print("\t Nom i Cognoms: "+self.__nom_cognoms+"\n")
        print("\t Dni: "+self.__dni+"\n")
        print("\t Poblacio: "+self.__poblacio+"\n")
        print("\t Pais: "+self.__pais+"\n")



