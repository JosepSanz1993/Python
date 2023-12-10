import sqlite3
from Interface import sql
class bd(sql):
    def connection(self,datebase):
        conn = sqlite3.connect(datebase)
        cursor = conn.cursor()
        return (cursor,conn)
    def execute_sql(self,cursor,sql):
        cursor.execute(sql)
    def insertfull(self,cursor,sql,data):
        cursor.executemany(sql,data)
    def applychage(self,conn):
        conn.commit()
    def exit(self,conn):
        conn.exit()
    def sqlcreatetable(self,name, values):
        colum = ""
        for key, value in values.items():
            colum = colum+key+" "+value+","+" "
        sql = 'CREATE TABLE {} ({})'.format(name,colum)
        sql = sql.removesuffix(", )")
        return sql+")" 
    def sqlqueryfechall(self,cursor,sql):
        cursor.execute(sql)
        line = cursor.fetchall()
        return line

