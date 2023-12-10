from Exercise1 import Collator,locale
from graphics import graphic
import json
days = []
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
y_def = 0
y_case = 0
y_hosp = 0 
y_uci = 0
file = 'data.txt'
def generatedays():
    global days
    i = 0
    while i<31:
        if i <9:
            string = "2021-05-0"+str(i+1)
        else:
            string = "2021-05-"+str(i+1)
        days.append(string)
        i+=1
def getprovince():
    prov = []
    with open('prov.json','r',encoding='utf-8') as file:
        data = json.load(file)
        prov.extend(data['prov'])
    file.close()
    locale.setlocale(locale.LC_ALL,'es_Es.UTF-8')
    collator = Collator()
    return sorted(list(set(prov)), key=collator.sort_key)
def get_dic(f_file,key):
    global days
    prov = getprovince()
    result = {}
    values = []
    for i in prov:
        result[i] = []
    with open(f_file,'r',encoding='utf-8') as file:
        data = json.load(file)
        for i in days:
            for j in prov:
                for z in data[i][j]:
                    values.append(int(z.get(key)))
                result[j].extend(values)
                values = []
    file.close()
    return result
def exit():
    return False
def switch(optio):
    dictionary = {
        "1": "exercise2_graphics_def()",
        "2": "exercise2_graphics_case()",
        "3": "exercise2_graphics_hosp()",
        "4": "exercise2_graphics_uci()",
        "5": "exit()"
    }
    return eval(dictionary.get(optio))

def exercise2_graphics_def():
    global x, y_def
    g = graphic('Defuntions',x,y_def)
    return ('def',g)
def exercise2_graphics_case():
    global x, y_case
    g = graphic('New Cases',x,y_case)
    return ('case',g)
def exercise2_graphics_hosp():
    global x, y_hosp
    g = graphic('Hospitalized',x,y_hosp)
    return ('hosp',g)
def exercise2_graphics_uci():
    global x, y_uci
    g = graphic('UCI',x,y_uci)
    return ('uci',g)
def ini():
    global y_def,y_case,y_hosp,y_uci
    global file
    generatedays()
    y_def = get_dic(file,'num_def')
    y_case = get_dic(file,'new_cases')
    y_hosp = get_dic(file,'num_hosp')
    y_uci = get_dic(file,'uci')
if __name__ =="__main__":
    ini()
    while(True):
        print("""Select une option:
        1) Defuntions
        2) New Cases
        3) Number of Hospited
        4) Number of UCI
        5) Exit""")
        optio = input()
        try:
            next = switch(optio)
            if next == False:
                break
            elif next[0] =='def':
                names_coord = ['Days of March 2021','Number of defuntions']
                next[1].bar_graphic(names_coord[0],names_coord[1])
            elif next[0] =='case':
                names_coord = ['Days of March 2021','Number of new cases']
                next[1].bar_graphic(names_coord[0],names_coord[1])
            elif next[0] =='hosp':
                names_coord = ['Days of March 2021','Number of hospitalized']
                next[1].bar_graphic(names_coord[0],names_coord[1])
            elif next[0] =='uci':
                names_coord = ['Days of March 2021','Number uci patients']
                next[1].bar_graphic(names_coord[0],names_coord[1])
        except Exception as op:
            print("To Select una correct optio")

