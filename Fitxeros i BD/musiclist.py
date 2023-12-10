from music import music
import json
class musiclist():
    def chargejsonvalues(self,):
        musiclist = []
        cadena_json = json.load(open('music.json',encoding="utf8"))
        for i in cadena_json['list_of_music']:
            musiclist.append(music(i['Topic'],i['Mean Author'],
                                  i['Other Author'],i['Year'],
                                   i['Weeks'],i['Country'],
                                    i['Language'],i['Continent']))
        return musiclist

    