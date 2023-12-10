import csv,json,locale
from pyuca import Collator
class convertfile:
    def __init__(self,file):
        self.__file = file
    def read_csv(self):
        results = []
        with open(self.__file,encoding="utf8") as File:
            reader = csv.DictReader(File)
            for row in reader:
                results.append(row)
        File.close()
        return results
    def acumulate_defuntion(self,province):
        result = 0
        for defuntion in self.read_csv():
            if province == defuntion.get('province'):
                result += int(defuntion.get('num_def'))
        return result
    def getvalues(self,key,value_key,key2,value_key2):
        values = []
        for value in self.read_csv():
            if value_key == value.get(key) and value_key2 == value.get(key2):
                values.append({"num_def":value.get('num_def'),
                               "new_cases":value.get('new_cases'),
                               "num_hosp":value.get('num_hosp'),
                               "uci":value.get('num_uci')})
                print("Namber of  new cases: {}\n".format(value.get('new_cases')))
                print("Namber of hospitalized: {}\n".format(value.get('num_hosp')))
                print("Uci number: {}\n".format(value.get('num_uci')))
        return values 
    def getsimpledata(self,key):
        values = []
        for i in self.read_csv():
            values.append(i.get(key))
        locale.setlocale(locale.LC_ALL,'es_Es.UTF-8')
        collator = Collator()
        return sorted(list(set(values)), key=collator.sort_key)
                                   
    def store_txt_file(self,key,key2):
        data = {}
        dates = self.getsimpledata(key)
        province = self.getsimpledata(key2)
        for date in dates:
            print("date: {}\n".format(date))
            data[date] = {}
            for prov in province:
                print("Name of province: {}\n".format(prov))
                data[date][prov] = self.getvalues('date',date,'province',prov)
        with open('data.txt', 'w', encoding='utf-8') as file:
            json.dump(data,file, indent=4, ensure_ascii=False)
        file.close()
    def show_values(self,key,key2):
        self.store_txt_file(key,key2)
        province = self.getsimpledata(key2)
        for prov in province:
            print("Nomber of defuntions from {} are: {}\n".format(prov,self.acumulate_defuntion(prov)))

def exercise1(file,key,key2):
    convert = convertfile(file)
    convert.show_values(key,key2)

if __name__ == "__main__":
    exercise1('Proyecto 3.csv','date','province')