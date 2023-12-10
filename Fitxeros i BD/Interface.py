from abc import abstractmethod
from abc import ABCMeta
class sql(metaclass=ABCMeta):
    @abstractmethod
    def connection(database):
        pass
    @abstractmethod
    def execute_sql(cursor,sql):
        pass
    @abstractmethod
    def insertfull(cursor,sql,data):
        pass
    @abstractmethod
    def applychage(conn):
        pass
    @abstractmethod
    def exit(conn):
        pass
    @abstractmethod
    def sqlcreatetable(name,values):
        pass
    @abstractmethod
    def sqlqueryfechall(cursor,sql):
        pass
