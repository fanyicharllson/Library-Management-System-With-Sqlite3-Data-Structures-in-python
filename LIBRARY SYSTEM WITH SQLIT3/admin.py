import logging
import hashlib

file_handler = logging.FileHandler("Application.log")
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(asctime)s: %(message)s', handlers=[file_handler])

class Admin:
    def __init__(self, name, password, email, admin_name):
        self.name = name
        self.password = password
        self.email = email
        self.admin_name = admin_name #person who added admin
   
   
   #Function to hash a password using SHA-256
    def hash_password(self, password: str) -> str:
        sha256 = hashlib.sha256()
        sha256.update(password.encode('utf-8'))
        return sha256.hexdigest()
     
    
    
    def getting_admin_info(self):
        print()
        print("Adding admin...\n")
        
        try:
            number_admin = int(input(f"{self.admin_name.capitalize()} enter the number of admin you want to add: "))
            admins = []
            for admin in range(number_admin):
                print()
                print(f"Entering admin number {admin + 1} information... ")
                
                self.name = input("Enter the admin number {} name: ".format(admin + 1))
                
                self.password = input("Enter the admin number {} password : ".format(admin + 1))
                password_hash = self.hash_password(self.password)
                
                self.email = input("Enter the admin number {} email: ".format(admin + 1))
                
                admins_tuples = (self.name, password_hash, self.email)
                admins.append(admins_tuples)
            return admins 
        except Exception as e:
            logging.error(f"Error in admin.py:  {e}") 
            print("Invalid admin number! Try again.")  
            
        
            
        
        
        
