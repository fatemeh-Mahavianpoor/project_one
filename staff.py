import sqlite3
import time
import functions
from constants.constant import db_names,table_names


# sql_connect=sqlite3.connect(db_names["staff"])
# cursor_sql=sql_connect.cursor()
# cursor_sql.execute(f'''CREATE TABLE {table_names["table8"]}
                    
#                     (month text,
#                      employer_id integer,
#                      personal_code integer,
#                      salary integer)''' )

# sql_connect.commit()
# sql_connect.close()

# sql_connect=sqlite3.connect(db_names["staff"])
# cursor_sql=sql_connect.cursor()
# cursor_sql.execute(f'''DROP TABLE {table_names["table8"]}''')

# sql_connect.commit()
# sql_connect.close()

month = time.strftime("%m")
monthly=month
                
    
def calculate_salary():

      sql_connect=sqlite3.connect(db_names["date"])
      cursor_sql=sql_connect.cursor()
      cursor_sql.execute("SELECT * FROM user_date ")
      items=cursor_sql.fetchall()

      user_id=input('id: ')
      id=int(user_id)

      person_day=0

      for row in items:
         if id == row[1]:
            person_day+=1
      
      
      sql_connect=sqlite3.connect(db_names["user"])
      cursor_sql=sql_connect.cursor()
      cursor_sql.execute(f"SELECT * FROM employers WHERE employer_id={id} ")
      table=cursor_sql.fetchall()

      for num in table:

            daily_salary=num[6]
            present_day=person_day
            salary=daily_salary * present_day

      sql_connect=sqlite3.connect(db_names["staff"])
      cursor_sql=sql_connect.cursor()
      cursor_sql.execute(F"SELECT * FROM salary  WHERE employer_id={id} AND month <> {month}")
      cursor_sql.fetchall()

      li=[monthly,id,num[5],salary]
      functions.add_many(li,db_names["staff"],table_names["table8"],len(li))


          


calculate_salary()




