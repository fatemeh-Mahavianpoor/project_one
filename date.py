import datetime 
import sqlite3
import functions
from constants.constant import db_names,table_names





time_module= datetime.datetime.now()

timer=(time_module.strftime("%X"))
date=(time_module.strftime("%x"))


class Date:


    def enter_product(self):

        id=input('Enter product_id:')

        sql_connect=sqlite3.connect(db_names["product"])
        cursor_sql=sql_connect.cursor()
       
        cursor_sql.execute("SELECT * FROM products ")
        table=cursor_sql.fetchall() 
        
        for item in table:
                product_id=int(id)
                if item[1]==product_id:
                    
                    sql_connect=sqlite3.connect(db_names["date"])
                    cursor_sql=sql_connect.cursor()
                    cursor_sql.execute("SELECT * FROM product_enter_date ")
                    items=cursor_sql.fetchall()

                    for row in items:
                        if date == row[1] and row[0]==product_id :
                            print("You're product have already entered!") 
                            break
                    else:
                        list=[id,date,item[2],timer]
                        
                        functions.add_many(list,db_names["date"],table_names["table5"],len(list))
                        break

    def exit_product(self):
         
        id=input('Enter product_id:')

        sql_connect=sqlite3.connect(db_names["product"])
        cursor_sql=sql_connect.cursor()
       
        cursor_sql.execute("SELECT * FROM products ")
        table=cursor_sql.fetchall() 
        
        for item in table:
                product_id=int(id)
                if item[1]==product_id:
                    
                    sql_connect=sqlite3.connect(db_names["date"])
                    cursor_sql=sql_connect.cursor()
                    cursor_sql.execute("SELECT * FROM product_enter_date ")
                    items=cursor_sql.fetchall()

                    for row in items:
                        if date == row[1] and row[0]==product_id :
                            print("You're product have already entered!") 
                            break
                    else:
                        list=[id,date,item[2],timer]
                        
                        functions.add_many(list,db_names["date"],table_names["table7"],len(list))
                        break
                                  
    def enter_user(self):
        
        
        id=input('Enter user_id:')

        sql_connect=sqlite3.connect(db_names["user"])
        cursor_sql=sql_connect.cursor()
       
        cursor_sql.execute("SELECT * FROM employers ")
        table=cursor_sql.fetchall() 
        
        for item in table:
                user_id=int(id)
                if item[1]==user_id:

                    
                    sql_connect=sqlite3.connect(db_names["date"])
                    cursor_sql=sql_connect.cursor()
                    cursor_sql.execute("SELECT * FROM user_date ")
                    items=cursor_sql.fetchall()

                    for row in items:
                        if  date == row[0] and row[1]==user_id:
                            print("You're employer have already entered!")
                            break
                    else:
                        list=[date,id,item[2],item[3],timer,'']
                        functions.add_many(list,db_names["date"],table_names["table6"],len(list))
                        break         
            
    def exit_user(self):
            
        id=input('Enter user_id:')
    

                    
        sql_connect=sqlite3.connect(db_names["date"])
        cursor_sql=sql_connect.cursor()
        cursor_sql.execute("SELECT * FROM user_date ")
        cursor_sql.fetchall()         
        time=timer
        day=date
        li=(time,day,id)
        update(li,db_names["date"],table_names["table6"])
                    


def update(list,db,table):


    sql_connect=sqlite3.connect(db)
    cursor_sql=sql_connect.cursor()
    sql_update_query=(f"UPDATE {table} SET Exit_time =(?) WHERE Date =(?) AND Exit_time='' AND user_id=(?) ") 
    cursor_sql.execute(sql_update_query,list)
    cursor_sql.execute(f"SELECT rowid, * FROM {table}")
    sql_connect.commit()
    sql_connect.close()


                        
# l=[(1,),(2,),(3,)]                            
# functions.delete_items(l,db_names["date"],table_names["table6"])                        

                                 

# product=Date()
# product.exit_user()




