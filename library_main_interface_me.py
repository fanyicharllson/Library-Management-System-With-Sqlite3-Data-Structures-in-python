import sqlite3
import hashlib
import logging
# from admin_interface import Admin_interface






file_handdlers = logging.FileHandler("Application.log")
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(asctime)s: %(name)s %(message)s', handlers=[file_handdlers])




# Function to hash a password using SHA-256
def hash_password(password: str) -> str:
    # Create a new SHA-256 hash object
    sha256 = hashlib.sha256()
    
    # Update the hash object with the bytes of the password
    sha256.update(password.encode('utf-8'))
    
    # Return the hexadecimal representation of the hash
    return sha256.hexdigest()


def Connceting_to_database_admin():
    """Function responsible for connecting to database(recieve the database name) and returning the connection"""
    try:
        conn = sqlite3.connect("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/admin.db")
        logging.info("Admin Database connected Successfully")
    
    except sqlite3.Error as e:
        logging.error(f"Error connecting to admin database: {e}") 
        print(f"An error occurred {e}")
        print(f"Please try again")
        return None
    
    return conn


def Connceting_to_database_member():
    """Function responsible for connecting to database(recieve the database name) and returning the connection"""
    try:
        conn_mem = sqlite3.connect("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/member.db")
        logging.info("Member Database connected Successfully")
    
    except sqlite3.Error as e:
        logging.error(f"Error connecting to member database: {e}") 
        print(f"An error occurred {e}")
        print(f"Please try again")
        return None
    
    return conn_mem


def Global_Function():
    """Global function responsible for taking user and admin names across the application that calls this function"""
    while True:
        try:
            print()  
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            break
        
        except Exception as e:
            logging.error(f"Error in Global Function: {e}")
            print(f"Name and Password Error: {e}") 
            continue
    
    return name, password 

def ForgetPassword(conn, user):
    c = conn.cursor()
    print()
    name = input("Enter your name to modify your password:  ")
    print()
    new_password = input("Enter your new password: ")
    
    if user == "member":
        c.execute("SELECT COUNT(*) FROM members WHERE name=?", (name,))
        if c.fetchone()[0] == 0:
            print()
            print(f"The name: {name} is not found. Please try again.")
            logging.error(f"Password reset failed: Name {name} not found.")
           
            Library_Interface()
        
        new_password_hash = hash_password(new_password) 
        c.execute("UPDATE members SET password=? WHERE name=?", (new_password_hash, name))
        conn.commit()
        print()
        print(f"{name} - member, your password has been reset successfully!")
        logging.info(f"Member Password reset successful.")
        
        
           
    
    
    elif user == "admin":
        c.execute("SELECT COUNT(*) FROM admin WHERE name=?", (name,))
        if c.fetchone()[0] == 0:
            print()
            print(f"The name: {name} is not found, Please try again.")
            logging.error(f"Password reset failed: Name {name} not found.")
           
            Library_Interface()
        
        new_password_hash = hash_password(new_password) 
        c.execute("UPDATE admin SET password=? WHERE name=?", (new_password_hash, name))
        conn.commit()
        print()
        print(f"{name} - admin, your password has been reset successfully!")
        logging.info(f"Admin Password reset successful.")
        
        
    
    else:
        print()
        print("Error: Please try again!")
        Library_Interface()      
    
    
            

def Admin_SignUp(conn):
    """This function is responsible for registering admin into the database and not soppose to be seen by the user"""
    print()
    print("Admin Signing Up...")
    c = conn.cursor()
    
    admin_name = input("Enter admin name: ")
    admin_password = input("Enter admin password: ")
    admin_email = input("Enter admin email: ")
    
    c.execute('SELECT COUNT(*) FROM admin WHERE name = ?', (admin_name,))
    if c.fetchone()[0] > 0:
        print()
        logging.warning("Admin already exists")
        print('Error: An admin already exists.')
        print("please try again")
        
        #************************************
        Library_Interface()
    
    try:
        admin_hash_password = hash_password(admin_password)
        
        c.execute("INSERT INTO admin (name, password, email) VALUES (?, ?, ?)", (admin_name, admin_hash_password, admin_email)) 
        conn.commit()
        logging.info(f"{admin_name} sign up went successfully.")
        print()
        print(f"{admin_name} your sign up was successful.")
        
        # conn.close()
        logging.debug("Member DataBase Closed")
        
        #moving to admin_interface
        # Admin_interface()
    
    except sqlite3.Error as e:
          logging.error(f"Error in Admin_SignUp method: {e}")
          print(f"Error adding amin {e}")
          print("Please try again")
          Library_Interface() 
            
           
         
          

def Admin_SignIn(connection):
    print()
    print("Admin Signing in...")
    c = connection.cursor()
    name, password = Global_Function()
    
    c.execute("SELECT password FROM admin WHERE name=?", (name,))
    
    data = c.fetchone()
    
    if data:
        admin_stored_password_hash = data[0]
        if admin_stored_password_hash == hash_password(password):
             logging.info("Admin Successfully signed in.")
             print()
             print(f"{name} - admin you login Successfully.")
             
            #  #calling admin_interface from separate file
            #  Admin_interface()
       
        else:
           logging.warning("WARNING: Invalid admin password or name")
           print()
           print("WARNING: Incorrect admin password or name")
           print("Please try again!")
        #    Library_Interface()      
        

def Member_SignIn(connection):
    print()
    print("Member signing in...")
    c = connection.cursor()
    print()
    name, password = Global_Function()
    c.execute("SELECT password FROM members WHERE name=?", (name,))
    memberInfo = c.fetchone()
    
   
    if memberInfo:
        stored_hash = memberInfo[0]
        if stored_hash == hash_password(password):
            print()
            logging.info("Member Successfully signed in.")
            print("Logging Successfully")
        
        else:
            print("Invalid password or Name")
            logging.error("Invalid password or name fromMember_SignIn method")
            print()
            print("Please try again")
            Library_Interface()
        
    
    else:
        print("Invalid Member name or password")
        logging.error("Invalid Member name or password in Member_SignIn method")
        print()
        print("Please try again")
        Library_Interface()    
    
    

def Member_SignUp(connection):
    print()
    print("Member signing up...")
    c = connection.cursor()
    print()
    
    name, password_member = Global_Function()
    email = input("Enter your email: ")
    
    # Check if the username already exists
    c.execute('SELECT COUNT(*) FROM members WHERE name = ?', (name,))
    if c.fetchone()[0] > 0:
        print()
        logging.warning("User name already exists")
        print('Error: Username already exists.')
        print("please try again")
        
        #++++++++++++++++++++++++++++++++++
        Library_Interface()
    
    try:
        password_hash = hash_password(password_member)
        
        c.execute("INSERT INTO members (name, password, email) VALUES (?,?,?)", (name, password_hash, email))
        connection.commit()
        logging.info(f"{name} sign up went successfully.")
        print()
        print(f"{name} your sign up was successful.")
       
        
        
    except sqlite3.Error as e:
          logging.error(f"Error in Member_SignUp method: {e}")
          print(f"Error inserting member {e}")
          print("Please try again")
          Library_Interface() 
           
      
def Library_Interface():
    print("\n")
    print("********************************************************")
    print()
    print("      Welcome to the Library Mangement System   ")
    print()
    print("********************************************************")
    
    while True:
        try:
            print("\n")
            print("1) Sign In as Admin")
            print("*****************************")
            print("2) Sign up as Admin")
            print("*****************************")
            print("3) Sign In as Member")
            print("*****************************")
            print("4) Sign Up as Member")
            print("*****************************")
            print("5) Forget Password(Setting New Password)")
            print("*****************************")
            print("6) Exit")
            print("*****************************")
            
            print()
            
            choice = int(input("Enter your choice(1-6): "))
            
            match choice:
                case 1:
                    connection = Connceting_to_database_admin()
                    Admin_SignIn(connection)
                    connection.close()
                    logging.debug("Admin DataBase Closed")
                    
                
                case 2:
                    connection =  Connceting_to_database_admin()
                    Admin_SignUp(connection)
                    connection.close()
                    logging.debug("Admin DataBase Closed")
                
                case 3:
                    connection_member = Connceting_to_database_member()
                    Member_SignIn(connection_member)
                    connection_member.close()
                    logging.debug("Member DataBase Closed")
                
                case 4:
                    connection_member = Connceting_to_database_member()
                    Member_SignUp(connection_member)
                    connection_member.close()
                    logging.debug("Member DataBase Closed")
                
                case 5:
                        print()
                        print("Setting password...")
                        print()
                        print("Answer the question below for security reasons...")
                        print()
                        
                        question = input("Are you a member or an admin? (member/admin): ").lower()
                        if question == "member":
                            print()
                            print("Setting Password for member...")
                            print()
                            conn_member = Connceting_to_database_member()
                            ForgetPassword(conn_member,"member") 
                            conn_member.close()
                            logging.info("Database member closed(forgot password)") 
                        
                        elif question == "admin":
                            print()
                            print("Setting Password for admin...") 
                            print()
                            conn_admin  = Connceting_to_database_admin()
                            ForgetPassword(conn_admin, "admin")
                            conn_admin.close()
                            logging.info("Database admin closed(forgot password)")   
                            
                        else:
                            print()
                            print("Question error! Please enter either a member or admin")
                            Library_Interface()           
                        
                
                case 6:
                    print("\n")
                    print("Existing....")
                    logging.info("Application ended by the user!")
                    quit()
                
                case _:
                    print("\n")
                    print("Invalid Option!")
                    print("Please try again!")
                    continue
                
        except Exception as e:
            print("\n")
            logging.error(f"Error from library interface: {e}")
            print()
            print(f"An Error Occured: {e}")
            
            continue
        
        
        
        
        
"""Main Code running the Library Interface"""
logging.info("Application Started...")

Library_Interface()
    
logging.debug("Application Ended.")
    