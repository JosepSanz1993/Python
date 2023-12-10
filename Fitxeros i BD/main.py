from sql import bd
from musiclist import musiclist
from sql import sqlite3
list = musiclist()
basedade = bd()
languages = ['Spanish','English','Portuguese','French']
#create connection
m_music = basedade.connection('music.bd')
cursor = m_music[0]
conn = m_music[1]
#create table
try:
    table = basedade.sqlcreatetable("Music",{"Topic":"text",
                                        "Author":"text",
                                        "Other Author":"text",
                                        "Year":"int",
                                        "Weeks":"int",
                                        "Country":"text",
                                        "Continent":"text",
                                        "Language":"text"})
    basedade.execute_sql(cursor,table)
    basedade.applychage(conn)
    print("The table Music is created now\n")
except sqlite3.OperationalError:
    print("The table exist\n")
#insert all data
try:
    insert = []
    sql = 'INSERT INTO Music values(?,?,?,?,?,?,?,?)'
    l_music = list.chargejsonvalues()
    for i in l_music:
        insert.append((str(i.getname()),str(i.getauthor()),
                       str(i.getotherauthor()),int(i.getyear()),
                       int(i.getweek()),str(i.getcountry()),
                       str(i.getcontinet()),str(i.getlenguage())))
    basedade.insertfull(cursor,sql,insert)
    basedade.applychage(conn)
    print("Dades insertated\n")
except sqlite3.OperationalError: 
    print("Dades exist\n")
try:
    sql = "Select min(year) as min_year from music"
    old_year = basedade.sqlqueryfechall(cursor,sql)[0][0]
    sql = "Select topic from music Where Year = {}".format(old_year)
    print("The oldest song on the list is: {}\n".format(basedade.sqlqueryfechall(cursor,sql)[0][0]))
    sql = "Select author, count(author) as total from music group by author order by total desc"
    print("The most repeated artist is: {}\n".format(basedade.sqlqueryfechall(cursor,sql)[0][0]))
    sql = "Select country, count(country) as total from music group by country order by total desc"
    print("The country with the most artists is: {}\n".format(basedade.sqlqueryfechall(cursor,sql)[0][0]))
    for i in languages:
        sql = "Select language, count(language) from music Where language = '{}'".format(i)
        l_lenguage = basedade.sqlqueryfechall(cursor,sql)[0][0]
        n_lenguage = basedade.sqlqueryfechall(cursor,sql)[0][1]
        print("In {} there are {} songs".format(l_lenguage,n_lenguage))
    sql = "Select continent, count(continent) as total from music group by continent order by total desc"
    print("The continent with the most appears is: {}\n".format(basedade.sqlqueryfechall(cursor,sql)[0][0]))
    sql = "Select max(weeks) from music"
    The_most_weeks = basedade.sqlqueryfechall(cursor,sql)[0][0]
    sql = ("Select topic from music where weeks = {}").format(The_most_weeks)
    topic = basedade.sqlqueryfechall(cursor,sql)[0][0]
    print("The song with The most number 1 percent for year is: {}\n".format(topic))
except sqlite3.OperationalError:
    print("Error Query")

try:
    sql = "Drop table music"
    basedade.execute_sql(cursor,sql)
    print("Table Deleted\n")
except sqlite3.OperationalError:
    print("Table not exist\n")
basedade.exit()