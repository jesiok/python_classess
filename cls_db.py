import sqlite3
import pandas as pd
from pandas.core.frame import DataFrame


# c:/Python/BED/example.sqlite
# wszedzie dodawc poprze args, tak bezpieczniej i baardziej prawidlowo

class DB_class():
# INICJALIZACJA: 
# db = DB_class(db='browser_ads.db')
    
# TO DO, przy SQLu dodać param    
    def __init__(self,path_db):
        self.db = path_db
        self.connection = sqlite3.connect(path_db)
        self.cursor = self.connection.cursor() 
    # def __enter__(self):
    #     return self

## select
    def select_to_df_by_pandas(self,sql):
        """
        input:
            sql
            np.df = db.select_to_df_by_pandas("select * from tbl_browser_adv_summary")
        output:
            df
        
        """

        df = pd.read_sql_query(sql, self.connection)
        return df

    def select_to_df_by_fetchall(self,sql):
        self.cursor.execute(sql)
        c = self.cursor.fetchall()
        df = pd.DataFrame(c)
        return df
        # info fetchone - zwraca jedna linijka, jako tuple, fetchall zwraca liste

    def select_by_fetchall(self,sql):
        """
        input:
            sql
        output:
            list
        """

        self.cursor.execute(sql)
        c = self.cursor.fetchall()
        return c

## insert     

    def insert(self,sql):
        """
        input: sql
        output: lastrow id

        # Przykladowe zastosowanie:

        db = DB_class(db='DB_browser_adv.db')
        db.insert("INSERT INTO tbl_browser_adv_summary (TASK, WEBSITE) VALUES ('test3','interia_test')")
        df = db.select_to_df_by_pandas("select * from tbl_browser_adv_summary")
        
        """
        self.cursor.execute(sql)
        id = self.cursor.lastrowid
        self.connection.commit()
        return id  
    
    def insert_many(self,sql):
        self.cursor.executemany(sql) 
        rowcount = self.cursor.rowcount
        self.connection.commit()
        return rowcount   


    
    def insert_df(self, table_name , df, if_exists="replace", index=False):
        """
        input: 
            table_name, 
            df,
            if_exists = "replace" "apend"
            index = False

        output:
            --
        """

        df.to_sql(table_name, self.connection, if_exists=if_exists, index=False)
        self.connection.commit()
        self.connection.close()


## update    
    def update(self,sql):
        self.cursor.execute(sql)
        rowcount = self.cursor.rowcount
        self.connection.commit()
        return rowcount  

## delete        
    def delete(self,sql):
        """
        input:
            sql np. "delete from tbl_name"
        output:
        """
        self.cursor.execute(sql)
        rowcount = self.cursor.rowcount
        self.connection.commit()   
     
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
