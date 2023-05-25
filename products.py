
import sqlite3
import functions
from constants.constant import db_names,table_names




class Products:
     

     def add_products(self):
      
      sql_connect=sqlite3.connect(db_names['product'])
      cursor_sql=sql_connect.cursor()



      print("Enter the following product information to add")  
      product_category=input('Enter product_category:')
      product_id=input('Enter product_id:')
      product_name=input('Enter your product name:')
      product_quantity=input('Enter quantity:')
      product_price=input('Enter price:')
      product_description=input('Enter product_description:')
      
      
      cursor_sql.execute("SELECT * FROM products")
      items=cursor_sql.fetchall() 

      is_product_avelible=False
  
      for item in items:
            id=int(product_id)
            if item[1]==id:
              is_product_avelible=True
              break

      if is_product_avelible:
            print("This id is already exsict")
            
      else:
            list=[(product_category),(product_id),(product_name),(product_quantity),(product_price),(product_description)]
            functions.add_many(list,db_names['product'],table_names['table1'],len(list))

     def show_product_list(self):       
            

               show_all_products=input("Do you want to see the whole list of products?")
               if show_all_products.capitalize()=='Y':
                functions.show_all(db_names['product'],table_names['table1'])
               elif show_all_products.capitalize()=='N':
                    filter_item=input("What filter do you want to search based on? category | id | name: ")
                    if filter_item.capitalize()=='Category':
                         category_name=input('Enter product_category:')
                         category=category_name
                         functions.selection(category,db_names['product'],table_names['table1'])
                         
                    elif filter_item=='id':
                         id=input('Enter product_id:')
                         id_num=int(id)
                         functions.selection(id_num,db_names['product'],table_names['table1'])
                    elif filter_item.capitalize()=='Name':
                         name=input('Enter your product name:')
                         pro_name=name
                         functions.selection(pro_name,db_names['product'],table_names['table1'])



  
p1= Products()
p1.show_product_list()


# functions.row(db_names['product'],table_names['table1'])
