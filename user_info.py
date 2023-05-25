
import csv

file_name='user.csv'

def user_info():

    with open(file_name,'r+',newline='') as file:
        writer = csv.DictWriter(file, fieldnames = ["id",'personal_code',"first_name", "last_name", "role"])
        writer.writeheader()

        show_list=input('Do you want to see user list? Y:Yes | N:NO: ')

        if show_list.capitalize()=='Y':
            with open(file_name,'r') as file:
                data=csv.reader(file)
                for row in data:
                    print(row)

        elif show_list.capitalize()=='N':

                    add_user=input('Do you want to add new user? Y:Yes | N:NO: ')

                    if add_user.capitalize()=='Y':
                            user_id=input('Enter user_id:')
                            user_personal_code=input('Enter personal_code:')
                            first_name=input('Enter first_name:')
                            last_name=input('Enter last_name:')
                            user_role=input('Enter role: admin | employer: ')


                            with open(file_name, 'r+',newline='') as infile:
                                    data= csv.reader(infile)
                                    datawriter=csv.writer(infile)
                                    
                                    is_user_availebl=False

                                    for row in data:
                                            if user_id == row[0]:
                                             is_user_availebl=True
                                             break
                                            
                                    if is_user_availebl:
                                            print("This user is already exsict")

                                    else:
                                            datawriter.writerow([user_id,user_personal_code,first_name.capitalize(),last_name.capitalize(),user_role.capitalize()])
                                            print("Your user has been successfully added.")
                    
                    elif add_user.capitalize()=='N':
                            exit=input('Do you wana exit? Y:YES | N:NO ')

                            if exit.capitalize()=='N':
                             user_info()
                            else:
                             print("The process is over.")
                           

                              
