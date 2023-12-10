import json
from graphics import graphic
f_file = 'data.txt'
values = {}
index = []
value_def = []
value_case = []
value_hosp = []
value_uci = []
prov = []
def getkeys(data):
    return data.keys()
def ini_dic():
    global values
    with open(f_file,'r',encoding='utf-8') as file:
        data = json.load(file)
        date_keys = getkeys(data)
        for i in date_keys:
            for j in data.get(i):
                values[j] = 0
    file.close()

def get_values(key):
    global values
    with open(f_file,'r',encoding='utf-8') as file:
        data = json.load(file)
        date_keys = getkeys(data)
        for i in date_keys:
            for j in data.get(i):
                for z in data[i][j]:
                    values[j] = values[j] + int(z.get(key))
    file.close()

def get_nicknames():
    global index
    with open('prov.json','r',encoding='utf-8') as file:
        data = json.load(file)
        nick = data.get('nickname')
    file.close()
    for i in index:
        del nick[i]
    return nick

def get_list():
    global values,index
    names = values.keys()
    value = []
    i = 0
    for key in names:
        if values.get(key)!=0:
            value.append(values.get(key))
        else:
            index.append(i)
        i=+1
    return value
def exit():
    return False
def switch(optio):
    dictionary = {
        "1": "exercise3_graphics_def()",
        "2": "exercise3_graphics_case()",
        "3": "exercise3_graphics_hosp()",
        "4": "exercise3_graphics_uci()",
        "5": "exit()"
    }
    return eval(dictionary.get(optio))

def exercise3_graphics_def():
    global value_def,prov
    get_values('num_def')
    value_def = get_list()
    g = graphic('Namber of Defuntion for province',value_def,prov)
    return ('def',g)
def exercise3_graphics_case():
   global value_case, prov
   get_values('new_cases')
   value_case = get_list()
   g = graphic('Namber of New Cases',value_case,prov)
   return ('case',g)
def exercise3_graphics_hosp():
    global value_hosp,prov
    get_values('num_hosp')
    value_hosp = get_list()
    g = graphic('Namber of Hospitalized Patients',value_hosp,prov)
    return ('hosp',g)
def exercise3_graphics_uci():
    global value_uci,prov
    get_values('uci')
    value_uci = get_list()
    g = graphic('Namber of Uci Patients',value_uci,prov)
    return ('uci',g)

if __name__ =="__main__":
    ini_dic()
    prov = get_nicknames()
    while(True):
        print("""Select une option:
        1) Number total of Defuntions for province
        2) New Cases total for province
        3) Number total of Hospited for province
        4) Number total of UCI for province
        5) Exit""")
        optio = input()
        try:
            next = switch(optio)
            if next == False:
                break
            elif next[0] =='def':
                next[1].cheese_graphic()
            elif next[0] =='case':
                next[1].cheese_graphic() 
            elif next[0] =='hosp':
                next[1].cheese_graphic()
            elif next[0] =='uci':
                next[1].cheese_graphic()   
        except Exception as op:
            print("To Select una correct optio")
