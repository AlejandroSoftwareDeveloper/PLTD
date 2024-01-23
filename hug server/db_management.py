import sqlite3

create_table_query = (
'''
CREATE TABLE IF NOT EXISTS RegisterUser 
(uuid INTEGER PRIMARY KEY AUTOINCREMENT,
FechaInicial DATE NULL,
FechaFinal DATE NULL)
'''
)

class Connection:
    def __init__(self,dbtoconnect):
        self.db = dbtoconnect
        self.conn = None
    def openconn(self):
        try:
            self.conn = sqlite3.connect(self.db)
        except:
            print("La conexion fallo revise los parametros de la funcion.")

    def create_table(self,query = str):
        if query is not None:
            self.execute_query(query)
        else:
            print("La query esta vacia.")

    def execute_query(self,query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor
    
    def execute_query_with(self,query,params):
        cursor = self.conn.cursor()
        cursor.execute(query,params)
        return cursor
        
    def get_all_data(self,table_name = None):
        query = "SELECT * FROM " + table_name
        cursor = self.conn.cursor()
        cursor.execute(query)
        print(cursor.fetchall())
        
    def close(self):
        self.conn.commit()
        self.conn.close()
        
    def insert(self,lista):
        cursor = self.conn.cursor()
        cursor.executemany('''INSERT INTO RegisterUser(uid,FechaInicial,FechaFinal) VALUES (?,?,?)''',lista)

connetion = Connection('register_user.sqlite')
connetion.openconn()
connetion.create_table(create_table_query)
connetion.get_all_data("RegisterUser")
connetion.close()

