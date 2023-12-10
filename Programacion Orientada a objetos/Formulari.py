from Dadespersonals import dades_personals
from Musica import musica
class formulari(dades_personals,musica):
    def __init__(self,data=[]):
        dades_personals.__init__(self,data[0],data[1],data[2],data[3])
        musica.__init__(self,data[4],data[5],data[6])
    def formularitoString(self):
        dades_personals.dadespersonalstoString(self)
        musica.musicatoString(self)





    





