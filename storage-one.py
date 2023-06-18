
import sqlite3
import functions
from constants.constant import db_names,table_names

# sql_connect=sqlite3.connect(db_names["storage"])
# cursor_sql=sql_connect.cursor()
# cursor_sql.execute(f'''CREATE TABLE {table_names["table4"]}
#                     (location text,
#                     storage_name text,
#                     warehouse_products text,
#                     storage_size integer)''' )

# sql_connect.commit()
# sql_connect.close()



class storage:
     

     def add_storage(self):
      
      sql_connect=sqlite3.connect(db_names["storage"])
      cursor_sql=sql_connect.cursor()



      print("Enter the following storage information to add")  
      sn=input('Enter your storage_name:')
      storage_name=str(sn)
      wp=input('Enter the products in warehouse:')
      warehouse_products=str(wp)
      location=input('Enter location:')
      x=input('Enter  storage_space:')
      storage_space=(str(x) + "m")
    
      
      
      cursor_sql.execute("SELECT * FROM storage ")
      items=cursor_sql.fetchall() 

      is_product_avelible=False
  
      for item in items:
            if item[1]==storage_name:
              is_product_avelible=True
              break

      if is_product_avelible:
            print("This id is already exsict")
            
      else:
            list=[storage_name,warehouse_products,location,storage_space]
            functions.add_many(list,db_names["storage"],table_names["table3"],len(list))



     def show_storage_list(self):
    
                
                show_all_user=input("Do you want to see the whole list of storage?")
                if show_all_user.capitalize()=='Y':
                  functions.show_all(db_names["storage"],table_names["table3"])
                elif show_all_user.capitalize()=='N':
                    filter_item=input("What filter do you want to search based on? name |  warehouse_products | location : ")
                    
                    if filter_item.capitalize()=='Name':
                         nam=input('Enter your Name:')
                         n=nam.capitalize()
                         functions.selection(n,db_names["storage"],table_names["table3"])
                    
                    elif filter_item.capitalize()=='Location':
                         location_in=input('Enter your location:')
                         loc=location_in.capitalize()
                         functions.selection(loc,db_names["storage"],table_names["table3"])
                   
                    elif filter_item.capitalize()=='Warehouse_products':
                         product_name=input('Enter the name of products:')
                         pro_name=product_name.capitalize()
                         functions.selection(pro_name,db_names["storage"],table_names["table3"])
                    

  


# p1=storage()
# p1.show_storage_list()



