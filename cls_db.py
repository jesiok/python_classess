import sqlite3
import pandas as pd
from pandas.core.frame import DataFrame


# c:/Python/BED/example.sqlite
# wszedzie dodawc poprze args, tak bezpieczniej i baardziej prawidlowo

class DB_class():
# INICJALIZACJA: 
# db = DB_class(db='browser_ads.db')
    
# TO DO, przy SQLu dodać param    
    def __init__(self,db):
        self.db = db
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor() 
    # def __enter__(self):
    #     return self

## select
    def select_to_df_by_pandas(self,sql):
        # Przykladowe zastosowanie:
        # db = DB_class(db='DB_browser_adv.db')
        # df = db.select_to_df("select * from tbl_browser_adv_summary")
        df = pd.read_sql_query(sql, self.connection)
        return df

    def select_to_df_by_fetchall(self,sql,args):
        self.cursor.execute(sql,args)
        c = self.cursor.fetchall()
        df = pd.DataFrame(c)
        return df
        # info fetchone - zwraca jedna linijka, jako tuple, fetchall zwraca liste

    def select_by_fetchall(self,sql,args):
        self.cursor.execute(sql)
        c = self.cursor.fetchall()
        return c

## insert     

    def insert(self,sql):
        # Przykladowe zastosowanie:
        # db = DB_class(db='DB_browser_adv.db')
        # db.insert("INSERT INTO tbl_browser_adv_summary (TASK, WEBSITE) VALUES ('test3','interia_test')")
        # df = db.select_to_df_by_pandas("select * from tbl_browser_adv_summary")
        self.cursor.execute(sql)
        id = self.cursor.lastrowid
        self.connection.commit()
        return id  
    
    def insert_many(self,sql,args):
        self.cursor.executemany(sql,args) 
        rowcount = self.cursor.rowcount
        self.connection.commit()
        return rowcount   

## update    
    def update(self,sql,args):
        self.cursor.execute(sql)
        rowcount = self.cursor.rowcount
        self.connection.commit()
        return rowcount  

## delete        
    def delete(self):
        pass   
     
## drop    
    def drop(self):
        pass 

## create
    def create(self,db_name,sql):
        # sql = f"""CREATE TABLE IF NOT EXISTS {db_name} (
        #     "ID"	INTEGER,
        #     "SYMBOL"	TEXT,
        #     "PRICE"	TEXT,
        #     "PERC"	TEXT,
        #     "TIME"	TEXT,
        #     "PROCESS_DATE"	TEXT,
        #     "PROCESS_DATETIME"	TEXT,
        #     PRIMARY KEY("ID")
        #     """
        self.cursor.execute(sql)
        self.connection.commit()
        
    # def __exit__(self,db,query,db_name):
    #     return self
    
# __exit__
# __enter__
# __repr__
# __new__

    def __del__(self):
        if self.connection != None:
            self.connection.close()
        #if self.cursor != None:
         #   self.cursor.close()

## tests
# db = DB_class(db='DB_browser_adv.db')
# db.insert("INSERT INTO tbl_browser_adv_summary (TASK, WEBSITE) VALUES ('test3','interia_test')")
# df = db.select_to_df_by_pandas("select * from tbl_browser_adv_summary")
# print(df)
