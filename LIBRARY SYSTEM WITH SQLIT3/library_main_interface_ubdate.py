import sqlite3
import hashlib
import logging
from admin_interface import Admin_interface
from member_interface import MemberOption

file_handler = logging.FileHandler("Application.log")
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(asctime)s: %(message)s', handlers=[file_handler])

# Function to hash a password using SHA-256
def hash_password(password: str) -> str:
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()


def connect_to_database(db_path: str):
    try:
        conn = sqlite3.connect(db_path)
        logging.info(f"Connected to database at {db_path} successfully")
        return conn
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database: {e}")
        print(f"An error occurred: {e}")
        return None
 
 
def global_function():
    while True:
        try:
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            return name, password
        except Exception as e:
            logging.error(f"Error in global function: {e}")
            print(f"Error: {e}")

def forget_password(conn, user_type):
    c = conn.cursor()
    print()
    name = input("Enter your name to modify your password: ")
    print()
    new_password = input("Enter your new password: ")

    table_name = "members" if user_type == "member" else "admin"
    c.execute(f"SELECT COUNT(*) FROM {table_name} WHERE name=?", (name,))
    if c.fetchone()[0] == 0:
        print(f"The name: {name} is not found. Please try again.")
        logging.error(f"Password reset failed: Name {name} not found.")
        return

    new_password_hash = hash_password(new_password)
    c.execute(f"UPDATE {table_name} SET password=? WHERE name=?", (new_password_hash, name))
    conn.commit()
    print(f"{name} - {user_type}, your password has been reset successfully!")
    logging.info(f"{user_type.capitalize()} password reset successful.")

def admin_sign_up(conn):
    print()
    print("Admin signing up...")
    c = conn.cursor()
    admin_name = input("Enter admin name: ")
    admin_password = input("Enter admin password: ")
    admin_email = input("Enter admin email: ")

    c.execute('SELECT COUNT(*) FROM admin WHERE name = ?', (admin_name,))
    if c.fetchone()[0] > 0:
        logging.warning("Admin already exists")
        print('Error: An admin already exists. Please try again.')
        return

    try:
        admin_hash_password = hash_password(admin_password)
        c.execute("INSERT INTO admin (name, password, email) VALUES (?, ?, ?)", (admin_name, admin_hash_password, admin_email))
        conn.commit()
        logging.info(f"{admin_name} signed up successfully.")
        print(f"{admin_name}, your sign-up was successful.")
        Admin_interface(admin_name) #from admin interface file
    except sqlite3.Error as e:
        logging.error(f"Error in admin_sign_up: {e}")
        print(f"Error: {e}")

def admin_sign_in(conn):
    print()
    print("Admin signing in...")
    c = conn.cursor()
    name, password = global_function()
    c.execute("SELECT password FROM admin WHERE name=?", (name,))
    data = c.fetchone()

    if data and hash_password(password) == data[0]:
        logging.info("Admin signed in successfully.")
        print(f"{name} - admin, you signed in successfully.")
        Admin_interface(name) #From admin interface file
    else:
        logging.warning("Invalid admin password or name.")
        print("Incorrect admin password or name. Please try again.")

def member_sign_in(conn):
    print()
    print("Member signing in...")
    c = conn.cursor()
    name, password = global_function()
    c.execute("SELECT password FROM members WHERE name=?", (name,))
    data = c.fetchone()

    if data and hash_password(password) == data[0]:
        logging.info("Member signed in successfully.")
        print(f"{name} - member, you signed in successfully.")
        
        MemberOption(name) #calling member menu in member_interface.py
        
    else:
        logging.warning("Invalid member password or name.")
        print("Incorrect member password or name. Please try again.")

def member_sign_up(conn):
    print()
    print("Member signing up...")
    c = conn.cursor()
    name, password_member = global_function()
    email = input("Enter your email: ")

    c.execute('SELECT COUNT(*) FROM members WHERE name = ?', (name,))
    if c.fetchone()[0] > 0:
        logging.warning("Username already exists")
        print('Error: Username already exists. Please try again.')
        return

    try:
        password_hash = hash_password(password_member)
        c.execute("INSERT INTO members (name, password, email) VALUES (?, ?, ?)", (name, password_hash, email))
        conn.commit()
        logging.info(f"{name} signed up successfully.")
        print(f"{name}, your sign-up was successful.")
        
        MemberOption() #calling member menu in member_interface.py
        
    except sqlite3.Error as e:
        logging.error(f"Error in member_sign_up: {e}")
        print(f"Error: {e}")

def library_interface():
    print("\n********************************************************")
    print("      Welcome to the Library Management System Interface")
    print("********************************************************")

    while True:
        try:
            print("\n1) Sign In as Admin")
            print("*****************************")
            print("2) Sign Up as Admin")
            print("*****************************")
            print("3) Sign In as Member")
            print("*****************************")
            print("4) Sign Up as Member")
            print("*****************************")
            print("5) Forget Password (Setting New Password)")
            print("*****************************")
            print("6) Exit")
            print("*****************************")
            

            choice = int(input("Enter your choice (1-6): "))
            
            if choice == 1:
                conn = connect_to_database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/admin.db")
                if conn:
                    admin_sign_in(conn)
                    conn.close()
            elif choice == 2:
                conn = connect_to_database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/admin.db")
                if conn:
                    admin_sign_up(conn)
                    conn.close()
            elif choice == 3:
                conn = connect_to_database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/member.db")
                if conn:
                    member_sign_in(conn)
                    conn.close()
            elif choice == 4:
                conn = connect_to_database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/member.db")
                if conn:
                    member_sign_up(conn)
                    conn.close()
            elif choice == 5:
                print()
                question = input("Are you a member or an admin? (member/admin): ").lower()
                if question in ["member", "admin"]:
                    db_path = "C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/member.db" if question == "member" else "C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/admin.db"
                    conn = connect_to_database(db_path)
                    if conn:
                        forget_password(conn, question)
                        conn.close()
                else:
                    print("Invalid input. Please enter 'member' or 'admin'.")
            elif choice == 6:
                logging.info("Application ended by the user.")
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            logging.error(f"Error in library interface: {e}")
            print(f"An error occurred: {e}")

