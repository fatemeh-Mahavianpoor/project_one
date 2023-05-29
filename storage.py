
import sqlite3
import functions
from constants.constant import db_names,table_names

# sql_connect=sqlite3.connect(db_names["storage"])
# cursor_sql=sql_connect.cursor()
# cursor_sql.execute(f'''CREATE TABLE {table_names["table3"]}
#                     (storage_name text,
#                     warehouse_products text,
#                     location text,
#                     size integer)''' )

# sql_connect.commit()
# sql_connect.close()


class storage:
     

     def add_storage(self):
      
      sql_connect=sqlite3.connect(db_names["storage"])
      cursor_sql=sql_connect.cursor()



      print("Enter the following storage information to add")  
      storage_name=input('Enter your storage_name:')
      warehouse_products=input('Enter the products in warehouse:')
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

        # show_all_user=input("Do you want to see the whole list of users?")
        # if show_all_user.capitalize()=='Y':
        #     functions.show_all(db_names["storage"],table_names["table3"])
        # elif show_all_user.capitalize()=='N':
        #     filter_item=input("What filter do you want to search based on? name |  warehouse_products | location : ")
            
        #     if filter_item.capitalize()=='Name':
        #             position=input('Enter Name:')
        #             job=position.capitalize()
        #             functions.selection(job,db_names["storage"],table_names["table3"])
                    
        #     elif filter_item.capitalize()=='Warehouse_products':
        #             name=input('Enter your warehouse_products:')
        #             pro_name=name.capitalize()
        #             functions.selection(pro_name,db_names["storage"],table_names["table3"])       
            
        #     elif filter_item.capitalize()=='Location':
        #             name=input('Enter your location:')
        #             pr_name=name.capitalize()
        #             functions.selection(pr_name,db_names["storage"],table_names["table3"])       
                
                show_all_user=input("Do you want to see the whole list of storage?")
                if show_all_user.capitalize()=='Y':
                  functions.show_all(db_names["storage"],table_names["table3"])
                elif show_all_user.capitalize()=='N':
                    filter_item=input("What filter do you want to search based on? name |  warehouse_products | location : ")
                    
                    if filter_item.capitalize()=='Name':
                         nam=input('Enter your Name:')
                         n=nam
                         functions.selection(n,db_names["storage"],table_names["table3"])
                    
                    elif filter_item.capitalize()=='Location':
                         location_in=input('Enter your location:')
                         loc=location_in.capitalize()
                         functions.selection(loc,db_names["storage"],table_names["table3"])
                   
                    elif filter_item.capitalize()=='Warehouse_products':
                         product_name=input('Enter the name of products:')
                         pro_name=product_name.capitalize()
                         functions.selection(pro_name,db_names["storage"],table_names["table3"])
                    

  


p1=storage()
p1.show_storage_list()












# import csv
# file_name='storage.csv'
# class Storage:
#     def store(self):

#         def st():

#             with open(file_name, 'r+',newline='') as outcsv:
#                 writer = csv.DictWriter(outcsv, fieldnames = ["name", "size", "location"])
#                 writer.writeheader()

#             show_list=input('Do you want to see storage list? Y:Yes | N:NO: ')
                
#             if show_list.capitalize()=='Y':
#                 with open(file_name,'r') as outcsv:
#                     data=csv.reader(outcsv)
#                     for row in data:
#                         print(row)

#             elif show_list.capitalize()=='N':
#                 add_storage=input('Do you want to add new storage? Y:Yes | N:NO: ')
                
#                 if add_storage.capitalize()=='Y':
#                     storage_name=input('Enter your storage name:')
#                     n=storage_name.capitalize()
#                     storage_size=input('Enter your storage size:')
#                     storage_location=input('Enter your storage location:')
                    
#                     with open(file_name, 'r+',newline='') as infile:
#                             data= csv.reader(infile)
#                             datawriter=csv.writer(infile)
                            
#                             is_storage_availebl=False

#                             for row in data:
#                                 if n == row[0]:
#                                   is_storage_availebl=True
#                                   break
                                    
#                             if is_storage_availebl:
#                                 print("This storage is already exsict")       
                                    
#                             else:
#                                 datawriter.writerow([n,storage_size.capitalize(),storage_location.capitalize()])
#                                 print("Your storage has been successfully added.")

#                 elif add_storage.capitalize()=='N':
#                     exit=input('Do you wana exit? Y:YES | N:NO ')

#                     if exit.capitalize()=='N':
#                      st()
#                     else:
#                      print("The process is over.") 
