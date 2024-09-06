import logging
from basiclogging import create_basic_logging
from library import Library


logging = create_basic_logging()

#Library objct to use in this admin_interface file
library = Library()


class Admin:
    def __init__(self):
        pass
    def add_book(self, admin_name):
        """Method calling the add_book method in Library class from library.py"""
        library.add_book_to_library(admin_name)
    
    def remove_book(self, admin_name):
        library.remove_book_from_library(admin_name)
    def update_book(self, admin_name):
        library.update_book(admin_name)
    
    def add_member(self):
        library.add_member_to_library()
    
    def view_book_details(self):
        library.get_book_details()
    
    def remove_member(self, admin_name):
        library.remove_member_from_library(admin_name);
     
    def add_admin(self, admin_name):
        library.adding_admin(admin_name)


def Admin_interface(admin_name):
    
    logging.info("Admin Interface started...")
    
    print()
    print("Welcome to Admin Interface......")
    print()
    
    print("1) Add book to Library")
    print("************************************")
    print("2) Remove book from Library")
    print("************************************")
    print("3) Update book in the Library")
    print("************************************")
    print("4) Add member to the Library")
    print("************************************")
    print("5) Remove member from the Library")
    print("************************************")
    print("6) Add admin to the Library")
    print("************************************")
    print("7) View book details")
    print("************************************")
    print("8) Log Out")
    print("************************************")
    
    
    #creating admin object
    admin = Admin()
    
    option = int(input("Enter option(1-8): "))
    
    match option:
        case 1:
            admin.add_book(admin_name)
            
        case 2:
            admin.remove_book(admin_name)
    
        case 3:
            admin.update_book(admin_name)
    
        case 4:
            admin.add_member()
    
        case 5:
            admin.remove_member(admin_name)
        
        case 6:
            admin.add_admin(admin_name)
        
        case 7:
            admin.view_book_details()    
            
        case 8:
            print()
            print(f"{admin_name} - (Admin) Log Out!")
            logging.info(f"The admin {admin_name} Log Out!")
            quit()
        
        case _:
            print()
            print("Invalid option")
            print("Try again!")
            Admin_interface()
    
    if isinstance(option, str):
        print()
        print("Invalid option! Pleas enter option from (1-7)")
        logging.warning("The user entered a string in the admin_interface menu option.")
        