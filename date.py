import datetime
import sqlite3
import functions
from constants.constant import db_names,table_names




time_module= datetime.datetime.now()
time=(time_module.strftime("%X"))
date=(time_module.strftime("%x"))

class Date:


    def enter_product(self):

        id=input('Enter product_id:')

        sql_connect=sqlite3.connect(db_names["product"])
        cursor_sql=sql_connect.cursor()
       
        cursor_sql.execute("SELECT * FROM products ")
        items=cursor_sql.fetchall() 
        
        for item in items:
                product_id=int(id)
                if item[1]==product_id:
                    
                    sql_connect=sqlite3.connect(db_names["date"])
                    cursor_sql=sql_connect.cursor()
                    cursor_sql.execute("SELECT * FROM product_enter_date ")
                    items=cursor_sql.fetchall()

                    for row in items:
                        if date == row[1]:
                            print("You're product have already entered!") 
                            break
                    else:
                        list=[id,date,item[2],time]
                        functions.add_many(list,db_names["date"],table_names["table5"],len(list))

    def exit_product(self):
         
        id=input('Enter product_id:')

        sql_connect=sqlite3.connect(db_names["product"])
        cursor_sql=sql_connect.cursor()
       
        cursor_sql.execute("SELECT * FROM products ")
        items=cursor_sql.fetchall() 
        
        for item in items:
                product_id=int(id)
                if item[1]==product_id:
                    
                    sql_connect=sqlite3.connect(db_names["date"])
                    cursor_sql=sql_connect.cursor()
                    cursor_sql.execute("SELECT * FROM product_exit_date ")
                    items=cursor_sql.fetchall()

                    for row in items:
                        if date == row[1]:
                            print("You're product have already entered!") 
                            break
                    else:
                        list=[id,date,item[2],time]
                        functions.add_many(list,db_names["date"],table_names["table7"],len(list))
                                  
    def enter_user(self):
        
        
        id=input('Enter product_id:')

        sql_connect=sqlite3.connect(db_names["user"])
        cursor_sql=sql_connect.cursor()
       
        cursor_sql.execute("SELECT * FROM employers ")
        table=cursor_sql.fetchall() 
        
        for item in table:
                product_id=int(id)
                if item[1]==product_id:

                    
                    sql_connect=sqlite3.connect(db_names["date"])
                    cursor_sql=sql_connect.cursor()
                    cursor_sql.execute("SELECT * FROM user_date ")
                    items=cursor_sql.fetchall()

                    for row in items:
                        if  date == row[0] and item[1]==product_id:
                            print("You're employer have already entered!")
                            break
                else:
                    list=[date,id,item[2],item[3],time,'']
                    functions.add_many(list,db_names["date"],table_names["table6"],len(list))
                    break         
        
                                    
   

    def exit_user(self):
            
        id=input('Enter product_id:')

        sql_connect=sqlite3.connect(db_names["user"])
        cursor_sql=sql_connect.cursor()
       
        cursor_sql.execute("SELECT * FROM employers ")
        table=cursor_sql.fetchall() 
        
        for item in table:
                product_id=int(id)
                if item[1]==product_id:

                    
                    sql_connect=sqlite3.connect(db_names["date"])
                    cursor_sql=sql_connect.cursor()
                    cursor_sql.execute("SELECT * FROM user_date ")
                    items=cursor_sql.fetchall()

                    for row in items:
                        if  date == row[0] and item[1]==product_id:
                            data = (time,product_id)
                            sql_update_query =(f"""UPDATE user_date SET Exit_time =''
                              WHERE user_id ={product_id} """)
                            cursor_sql.execute(sql_update_query, data)
                            break
                        
# li=[(1,),(2,),(3,),(4,)]                            
# functions.delete_items("23456",db_names["date"],table_names["table6"])                        

#  Update TABLE_NAME set name = '',id = cast(NULLIF(id,'') as NVARCHAR)

                                 

product=Date()
product.exit_user()







