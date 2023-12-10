import pandas as pd
lligues = {}
def entradadedades():
    lliga = input("Entra el nom de la lliga:\n")
    url = input("Entra la url (fitxer .json) per a poder aconseguir les dades:\n")
    lligues[lliga] = url
def llegirjson(lliga):
    equips = pd.read_json(lligues.get(lliga))
    return equips
def numeroequips():
    lliga = input("Nom de la lliga:\n")
    print("La {} te {} equips\n".format(lliga,len(llegirjson(lliga)['clubs'])))
def mostrarnomicodi():
    lliga = input("Nom de la lliga:\n")
    for i in llegirjson(lliga)['clubs']:
        if i['code'] !=None:
            print("Equip {} amb codi {}\n".format(i['name'],i['code']))
        else:
            print("Equip {} sense codi\n".format(i['name']))
def guardardadestxt():
    lliga = input("Nom de la lliga:\n")
    file = lliga+".txt"
    with open(file,'w') as f:
        f.write("Lliga {}:\n".format(lliga))
        f.write("\t Nombre de equips --> {}\n".format(numeroequips(lliga)))
        f.write("Equips i codi:\n")
        for i in lliga:
            f.write("\t {} amb codi {}\n".format(i['name'],i['code']))
    f.close()
def sortir():
    print("Usuari garcies per usar l'Aplicació\n")
    return False
def switch(opcio):
    diccionari = {
    "1": "entradadedades()",
    "2": "numeroequips(lliga)",
    "3": "mostrarnomicodi(lliga)",
    "4": "guardardadestxt(lliga)",
    "5": "sortir()"
    }
    return eval(diccionari.get(opcio))

while(True):
    print("""Selecciona una opción:
    1) Afegir dades de la lliga
    2) Mostrar nombre d'equips de la lliga
    3) Mostrar els equips amb el seu codi de la lliga
    4) Guardar informacio a un fitxer de text
    5) Sortir""")
    opcio = input()
    try:
        continuar = switch(opcio)
        if continuar == False:
            break
    except Exception as op:
        print("Selecciona una opcio válida")