import sqlite3
import functions
from constants.constant import db_names,table_names

# sql_connect=sqlite3.connect(db_names["store"])
# cursor_sql=sql_connect.cursor()
# cursor_sql.execute(f'''CREATE TABLE {table_names["table4"]}
#                     (storage_name text,
#                     warehouse_products text,
#                     location text,
#                     storage_size integer
#                     )''' )

# sql_connect.commit()
# sql_connect.close()


class Storage:

    def add_storage(self):
        sql_connect=sqlite3.connect(db_names["store"])
        cursor_sql=sql_connect.cursor()

        print("Enter the following storage information to add")  
        storage_name=input('Enter your storage_name:')
        warehouse_products=input('Enter the products in warehouse:')
        location=input('Enter location:')
        x=input('Enter  storage_space:')
        storage_space=(str(x) + "m")


        cursor_sql.execute("SELECT * FROM  test ")
        items=cursor_sql.fetchall() 

        is_product_avelible=False
    
        for item in items:
                name=(storage_name)
                if item[0]==storage_name:
                 is_product_avelible=True
                 break

        if is_product_avelible:
                print("This id is already exsict")
                
        else:
                list=[storage_name,warehouse_products,location,storage_space]
                functions.add_many(list,db_names["store"],table_names["table4"],len(list))

    def show_list(self):
           
           show_all_storage=input("Do you want to see the whole list of storage?")
           
           if show_all_storage.capitalize()=='Y':
                functions.show_all(db_names["store"],table_names["table4"])
            
           elif show_all_storage.capitalize()=='N':

                filter_item=input("What filter do you want to search based on? storage_name | warhouse_product | location: ")

                if filter_item == "storage_name":

                    store_name=input("write your storege_name: ")
                    store=store_name
                    selection(store)           






# omadam quary selection ro inja faghat bra hamin table neveshtam baz ham hamon error ro dad

def selection(inputx):
 sql_connect=sqlite3.connect("storage.db")
 cursor_sql=sql_connect.cursor()
 
 cursor_sql.execute(f"SELECT storage_name,warehouse_products,location FROM test WHERE storage_name OR warehouse_products OR location=(?)",(inputx,))
 items=cursor_sql.fetchall()
 

 for row in items:

    if inputx == row[0]:
      
      cursor_sql.execute(f"SELECT * FROM test WHERE storage_name=(?)",(inputx,))
      items=cursor_sql.fetchall()
      print(items)
      break
    
    elif inputx == row[1]:
    
      cursor_sql.execute(f"SELECT * FROM test WHERE warehouse_products=(?)",(inputx,))
      items=cursor_sql.fetchall()
      print(items)
      break
    
    elif inputx == row[2]:

      cursor_sql.execute(f"SELECT * FROM test WHERE location=(?)",(inputx,))
      items=cursor_sql.fetchall()
      print(items)
      break    

 sql_connect.commit()
 sql_connect.close()



p1=Storage()
p1.show_list()

