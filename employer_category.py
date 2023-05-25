import sqlite3
import functions
from constants.constant import db_names,table_names

# functions.create_table(db_names["employer"],table_names["table2"])



class employer_info:
     

     def add_employer(self):
      
      sql_connect=sqlite3.connect(db_names["employer"])
      cursor_sql=sql_connect.cursor()



      print("Enter the following employer information to add")  
      job_position=input('Enter job_position:')
      employer_id=input('Enter employer_id:')
      employer_name=input('Enter your employer_name:')
      product_quantity=input('Enter quantity:')
      product_price=input('Enter price:')
      product_description=input('Enter product_description:')
      
      
      cursor_sql.execute("SELECT * FROM employers ")
      items=cursor_sql.fetchall() 

      is_product_avelible=False
  
      for item in items:
            id=int(employer_id)
            if item[1]==id:
              is_product_avelible=True
              break

      if is_product_avelible:
            print("This id is already exsict")
            
      else:
            list=[job_position,employer_id,employer_name,(product_quantity),(product_price),(product_description)]
            functions.add_many(list,db_names["employer"],table_names["table2"])

     def show_employer_list(self):       
            
               show_all_products=input("Do you want to see the whole list of employers?")
               if show_all_products.capitalize()=='Y':
                functions.show_all(db_names["employer"])
               elif show_all_products.capitalize()=='N':
                    filter_item=input("What filter do you want to search based on? job position | id | name: ")
                    if filter_item.capitalize()=='Job position':
                         job_position=input('Enter Job position:')
                         category=job_position
                         functions.selection(category,db_names["employer"])
                         
                    elif filter_item=='id':
                         id=input('Enter employer_id:')
                         id_num=int(id)
                         functions.selection(id_num,db_names["employer"])
                    elif filter_item.capitalize()=='Name':
                         name=input('Enter your employer name:')
                         pro_name=name
                         functions.selection(pro_name,db_names["employer"])



  

p1=employer_info()
p1.add_employer()



