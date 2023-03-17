import sqlite3

class DatabaseHandler:
    def __init__(self,dbName):
        self.__dbName=dbName
        self.__dbConn = sqlite3.connect(self.__dbName+".db")
        self.__cur = self.__dbConn.cursor()

    def initDatabase(self):
        self.__cur.execute('Create table If not exists users (user_id integer PRIMARY KEY autoincrement , first_name text not null, last_name text not null)')

    def new_user(self,firstname,lastname):
        self.__cur.execute("insert into users(first_name,last_name) values (:name,:family)",{"name":firstname,"family":lastname})

    def list_user(self):
        self.__cur.execute('select * from users')
        return self.__cur.fetchall()

    def update_user(self,updateDict,userId):
        for updateColumn in updateDict:
            newValue = updateDict[updateColumn]
            self.__cur.execute('update users set ' + updateColumn +"='" + newValue + "' where user_id =" + str(userId))

    def delete_user(self,uid):
        self.__cur.execute("delete from users where user_id=:uid",{"uid":uid})

    def  __del__(self):
        self.__dbConn.commit()