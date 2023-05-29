import csv

employer_file='employer_date.csv'
salary_file='salary.csv'
user_file='user.csv'

class Staff:
    
    def calculate_salary(self):

      with open(salary_file,'r+',newline='') as salary_csv:
         write=csv.DictWriter(salary_csv, fieldnames=["personal code","salary"])
         write.writeheader()

      user_id=input('id: ')

      person_day=0
      with open(employer_file,'r',newline='') as filecsv:
         reader=csv.reader(filecsv)

         for row in reader:
            if user_id==row[1]:
               person_day+=1

      daily_salary=5000
      present_day=person_day

      salary=(daily_salary * present_day)

   
      with open(user_file,'r+',newline='') as user_info:
         reader= csv.reader(user_info)
         for row in reader:
               if user_id == row[0]:
                  Personal_code = row[1]

                  with open(salary_file,'r') as read:
                     reader=csv.reader(read)

                     is_exsict=False

                     for row in reader:
                        if Personal_code==row[0]: 
                           print('This id has already exisct!')
                           is_exsict=True
                     
                     if( not is_exsict):   
                           with open(salary_file,"a+",newline='') as write:
                              writer=csv.writer(write)
                              writer.writerow([Personal_code,salary])
          
    def user_see_salary(self):

      user_input =input("enter your personal code: ")

      with open(salary_file,'r') as read:
         reader=csv.reader(read)
         for row in reader:
            if user_input == row[0]:
                  print(row[1])

            





