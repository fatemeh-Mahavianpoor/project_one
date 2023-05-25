
import category,employer_category

class User():
    def __init__(self,first_name,last_name,id,role):
        self.first_name=first_name
        self.last_name=last_name
        self.id=id
        self.role=role

class Admin(User):
 
 log_in=False

 def login(self):
    self.username = "fatemeh"
    self.password = "23454fg"
    user_name=input("Enter your username: ") 

    if user_name==self.username:
  
     pas=input("Enter your password: ")
     if pas==self.password:
      print("You're logged in!")
      Admin.log_in=True

     else:
      print("your password is false") 

    else:
      print("your username is false")  


 def acsses_product(cls):
   
  if cls. log_in: 
    category.repeat()

  else:
    print("You're not logged in!") 

 def acsses_employer(cls):
   
   if cls.log_in==True:
    employer_category.repeat_em()

   else:
    print("You're not logged in!")

    
class Employer(User):
  
  def branch_employer(self):
    pass
    
class Customer(User):
    pass



p1=Admin('mary','nadi','1234','admin')
# p1.login()
# p1.acsses_product()
p1.acsses_employer()





