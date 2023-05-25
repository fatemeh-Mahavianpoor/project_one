import datetime
import csv
from tempfile import NamedTemporaryFile
import shutil

tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
employer_file='employer_date.csv'
product_enter_file='product_enter_date.csv'
product_exit_file='product_exit_date.csv'


time_module= datetime.datetime.now()
time=(time_module.strftime("%X"))
date=(time_module.strftime("%x"))

class Date:
   

   def employer_enter(self):

        with open(employer_file,'r+',newline='') as f:
            writer=csv.writer(f)
            writer.writerow(['Date','Id','first_name','last_name','Enter_time','Exit_time'])

        user_id_input=input("id: ")

        with open(employer_file,'r') as f:
            reader=csv.reader(f)
            is_user_logged_in = False
        
            for row in reader:
                if user_id_input==row[1]:
                    if date==row[0]:
                        print('You have already entered!')
                        is_user_logged_in = True

        if(not is_user_logged_in):    

            with open('user.csv','r') as file:
                user_info=csv.reader(file)

                for info in user_info:
                    if user_id_input==info[0]:
                        with open(employer_file,'a+',newline='') as f:
                         write=csv.writer(f)
                         write.writerow([date,user_id_input,info[1],info[2],time])
                         print('successfully enterd!')
                        
   def employer_exit(self):

    user_id_input=input('id: ')

    with open(employer_file,'r+',newline='') as f,tempfile:
        reader=csv.reader(f)
        write = csv.writer(tempfile, delimiter=',', quotechar='"')
        
        for row in reader:
            if row[1]==user_id_input:
             row.append(time)    
             write.writerow(row)
            else:    
             write.writerow(row)  


        

    shutil.move(tempfile.name, employer_file)               

   def product_enter(self):
      
        with open(product_enter_file,'r+',newline='') as enterfile:
            writer=csv.writer(enterfile)
            writer.writerow(['Id','product_name','Date','time'])

        product_id_input=input("id: ")

        with open(product_enter_file,'r')as enterfile:
            reader=csv.reader(enterfile)
            is_product_enter=False

            for row in reader:
             if product_id_input == row[0]:
                if date == row[2]:
                    print("You're product have already entered!")
                    is_product_enter=True

        if(not is_product_enter):    

            with open('product.csv','r') as file:
             product_info=csv.reader(file)

             for info in product_info:
                if product_id_input==info[0]:
                    with open(product_enter_file,'a+',newline='') as enterfile:
                        write=csv.writer(enterfile)
                        write.writerow([product_id_input,info[1],date,time])
                        print('successfully enterd!')

   def product_exit(self):
      
        with open(product_exit_file,'r+',newline='') as exitfile:
            writer=csv.writer(exitfile)
            writer.writerow(['Id','product_name','Date','time'])

        product_id_input=input("id: ")

        with open(product_exit_file,'r')as exitfile:
            reader=csv.reader(exitfile)
            is_product_enter=False

            for row in reader:
             if product_id_input == row[0]:
                if date == row[2]:
                    print("You're product have already entered!")
                    is_product_enter=True

        if(not is_product_enter):    

            with open('product.csv','r') as file:
             product_info=csv.reader(file)

             for info in product_info:
                if product_id_input==info[0]:
                    with open(product_exit_file,'a+',newline='') as exitfile:
                        write=csv.writer(exitfile)
                        write.writerow([product_id_input,info[1],date,time])
                        print('successfully enterd!')





# employer=Date()
# employer.product_enter()   