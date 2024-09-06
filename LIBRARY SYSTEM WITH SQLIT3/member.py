import logging
from admin import Admin

file_handler = logging.FileHandler("Application.log")
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(asctime)s: %(message)s', handlers=[file_handler])


class Member:
    def __init__(self,name= None, password= None, email= None):
        self.name = name
        self.password = password
        self.email = email
        self.admin_instance = Admin(None, None, None, None) #admin instance
    
    def get_member(self):
        print()
        print("Adding Member...\n")
        
        try:
            number_member = int(input("Enter the number of member you want to add: "))
            members = []
            for member in range(number_member):
                print()
                print(f"Entering member number {member + 1} information... ")
                
                self.name = input("Enter member number {} name: ".format(member + 1))
                
                self.password = input("Enter member number {} password : ".format(member + 1))
                
                # logging.info()
                logging.info("\nCalling the class Admin method: hash_password")
                
                password_hash = self.admin_instance.hash_password(self.password)  #calling hash_password method in admin.py
                
                logging.debug("Done calling hash_password in admin.py. class Admin")
                
                self.email = input("Enter member number {} email: ".format(member + 1))
                
                member_tuples = (self.name, password_hash, self.email)
                members.append(member_tuples)
            return members 
        
        except Exception as e:
            logging.error(f"Error in member.py:  {e}") 
            print("Invalid member number! Try again.")  
            
        
          
        
        