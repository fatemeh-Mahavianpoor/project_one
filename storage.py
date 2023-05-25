import csv
file_name='storage.csv'
class Storage:
    def store(self):

        def st():

            with open(file_name, 'r+',newline='') as outcsv:
                writer = csv.DictWriter(outcsv, fieldnames = ["name", "size", "location"])
                writer.writeheader()

            show_list=input('Do you want to see storage list? Y:Yes | N:NO: ')
                
            if show_list.capitalize()=='Y':
                with open(file_name,'r') as outcsv:
                    data=csv.reader(outcsv)
                    for row in data:
                        print(row)

            elif show_list.capitalize()=='N':
                add_storage=input('Do you want to add new storage? Y:Yes | N:NO: ')
                
                if add_storage.capitalize()=='Y':
                    storage_name=input('Enter your storage name:')
                    n=storage_name.capitalize()
                    storage_size=input('Enter your storage size:')
                    storage_location=input('Enter your storage location:')
                    
                    with open(file_name, 'r+',newline='') as infile:
                            data= csv.reader(infile)
                            datawriter=csv.writer(infile)
                            
                            is_storage_availebl=False

                            for row in data:
                                if n == row[0]:
                                  is_storage_availebl=True
                                  break
                                    
                            if is_storage_availebl:
                                print("This storage is already exsict")       
                                    
                            else:
                                datawriter.writerow([n,storage_size.capitalize(),storage_location.capitalize()])
                                print("Your storage has been successfully added.")

                elif add_storage.capitalize()=='N':
                    exit=input('Do you wana exit? Y:YES | N:NO ')

                    if exit.capitalize()=='N':
                     st()
                    else:
                     print("The process is over.") 
