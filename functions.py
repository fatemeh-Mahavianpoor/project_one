import sqlite3
from constants.constant import qustion_mark_generator,table_names,db_names


def add_many(list,db_name,table,number_values):
      
    sql_connect=sqlite3.connect(db_name)
    cursor_sql=sql_connect.cursor()
    cursor_sql.executemany(f"INSERT INTO {table} VALUES({qustion_mark_generator(number_values)})",(list,))
    cursor_sql.execute(f"SELECT rowid, * FROM {table}")
    sql_connect.commit()
    sql_connect.close()



def show_all(db_name,table):
 
 sql_connect=sqlite3.connect(db_name)
 cursor_sql=sql_connect.cursor()
 
 cursor_sql.execute(f"SELECT rowid, * FROM {table}")
 table_list=cursor_sql.fetchall()

 for item in table_list:
  print(item)

 sql_connect.commit()
 sql_connect.close()   


def delete_items(idlist,db_name,table):

      sql_connect=sqlite3.connect(db_name)
      cursor_sql=sql_connect.cursor()
      cursor_sql.executemany(f"DELETE from {table} WHERE rowid=?",idlist)
      sql_connect.commit()
      sql_connect.close()





def selection(data,db_name,table):
 sql_connect=sqlite3.connect(db_name)
 cursor_sql=sql_connect.cursor()
 sql_connect.row_factory = sqlite3.Row
 cursor =sql_connect.execute(f'select * from {table}')
 row = cursor.fetchone()
 names =row.keys()
 cloumn_one=names[0]
 cloumn_two=names[1]
 cloumn_three=names[2]
 
 cursor_sql.execute(f"SELECT {cloumn_one},{cloumn_two},{cloumn_three} FROM {table} WHERE {cloumn_one}=(?) OR {cloumn_two}=(?) OR {cloumn_three}=(?)",(data,data,data))
 table_list=cursor_sql.fetchall()
 

 for row in table_list:

    if data == row[0]:
      
      cursor_sql.execute(f"SELECT * FROM {table} WHERE {cloumn_one}=(?)",(data,))
      table_list=cursor_sql.fetchall()
      print(table_list)
      break
    
    elif data == row[1]:
    
      cursor_sql.execute(f"SELECT * FROM {table} WHERE {cloumn_two}=(?)",(data,))
      table_list=cursor_sql.fetchall()
      print(table_list)
      break
    
    elif data == row[2]:

      cursor_sql.execute(f"SELECT * FROM {table} WHERE {cloumn_three}=(?)",(data,))
      table_list=cursor_sql.fetchall()
      print(table_list)
      break    

 sql_connect.commit()
 sql_connect.close()






                      


