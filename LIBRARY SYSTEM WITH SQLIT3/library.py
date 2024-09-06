import sqlite3
import logging
from book import Book
from admin import Admin
from member import Member

file_handler = logging.FileHandler("Application.log")
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(asctime)s: %(message)s', handlers=[file_handler])
 


def database(db_name: str):
    try:
        conn = sqlite3.connect(db_name)
        logging.info(f" Database connection established at {db_name} in library.py file")
        return conn    
    except sqlite3.Error as e:
           logging.error(f"Error connecting to database at {db_name}", e)
           print()
           print("An error occurred! Please try again")
           return None


class Library:
    def add_book_to_library(self, admin_name):
        connection = database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/book.db")
        if connection:
            c = connection.cursor()
            #creating book object from Book class
            book1 = Book(None, None, None, admin_name)
            books, number_of_books  = book1.getting_book()
            try:
                c.executemany("INSERT INTO books (title, author, genre, name_admin) VALUES (?,?,?,?)", books)
                connection.commit()
                logging.info(f"Your book record of {number_of_books} has been added to the database successfully.")
                print()
                print(f"Your book record of {number_of_books} has been added.")
                print(f'{c.rowcount} records inserted successfully.')
                connection.close()
            except Exception as e:
                print()
                logging.error(f"Error from library.py: {e}")
                print(f"Error: {e}") 
                
        else:
            logging.info(f"Error: Database connection failed!")
            print("Error: Database connection failed")
                       
            
            
    def remove_book_from_library(self, admin_name):
        print()
        print("Removing book from library...")
        connection = database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/book.db")
        if connection:
            c = connection.cursor()
            print()
            title_book = input("Enter the title of the book you want to remove: ")
            print()
            c.execute("SELECT COUNT(*) FROM books WHERE title=?", (title_book,))
            if c.fetchone()[0] == 0:
                print(f"The Book title: {title_book} is not found. Please try again.")
                logging.error(f"Book removed failed: Book title {title_book} not found.")
                return
        
        c.execute("DELETE FROM books WHERE title=?", (title_book,))
        connection.commit()
        connection.close()
        print(f"The Book title: {title_book} and it contents has been remove succesfully by {admin_name}")
        logging.error(f"Book {title_book} has been removed by {admin_name} - admin.")
   
    
    def get_book_details(self):
         print()
         print("Book details recently added to the library and the admin who added them...")
         logging.info("Book details recently added to the library")
         print()
         connection = database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/book.db")
         if connection:
            c = connection.cursor()
            
            c.execute("SELECT * FROM books")
            result = c.fetchall()
            connection.close()
            for row in result:
                    print(f"Book index in library: {row[0]}")
                    print(f"Book title in library: {row[1]}")
                    print(f"Book author in library: {row[2]}")
                    print(f"Book genre in library: {row[3]}")
                    print(f"The admin name who added the book in the library: {row[4]}")   
                    print()
    
    def update_book(self, admin_name):
         connection = database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/book.db")
         if connection:
            c = connection.cursor()
            
            #creating book object
            book1 = Book(None, None, None,  admin_name)
            book_title, choice_of_update, new_feature = book1.updating_book()
            
            c.execute("SELECT COUNT(*) FROM books WHERE title=?", (book_title,)) 
            if c.fetchone()[0] == 0:
                print(f"The book: {book_title} is not found in the library. Please try again.")
                logging.error(f"Book reset failed:  {book_title} not found in the database.")
                return
            
            c.execute(f"UPDATE books SET {choice_of_update}=? WHERE title=? ", (new_feature, book_title))
            connection.commit()
            print(f"The book title {book_title}, its {choice_of_update} has been updated to {new_feature} by {admin_name}")
            logging.info(f"The Book title {book_title}, its {choice_of_update} , has been updated successfully to {new_feature}, by {admin_name}")
            
            
    
    def adding_admin(self, admin_name):
        conn = database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/admin.db") 
        try:
            if conn:
                c = conn.cursor()
                admin1 =  Admin(None, None, None, admin_name)
                list_admin = admin1.getting_admin_info()
                
                c.executemany("INSERT INTO admin (name, password, email) VALUES (?,?,?)", list_admin)
                conn.commit()
                print()
                print(f"{admin_name.capitalize()}, the admins you included has been added successfully!")
                logging.info(f"Added admins successfully by {admin_name}")
                
                
        except Exception as e:
            logging.error(f"Error: {e}")
            print(f"Error: {e}")            
             
                        
    
    def add_member_to_library(self):
         conn = database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/member.db")
         try:
            if conn:
                c = conn.cursor()
                mem = Member() #creating member instance and calling the get_memeber method
                mem_lists = mem.get_member()
                c.executemany("INSERT INTO members (name, password, email) VALUES (?,?,?)", mem_lists)
                
                conn.commit()
                logging.info(f"The members you included  has been added to the database successfully.")
                print()
                print(f"Memebers has been added successfully.")
                print(f'{c.rowcount} records inserted successfully.')
                conn.close()
                
         except Exception as e:
            print()
            print(f"Error: {e}") 
            logging.error("Error in library.py, line 145: {e}")       
        
    
    
    def remove_member_from_library(self, admin_name):
        conn = database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/member.db")
        if conn:
            try:
                c = conn.cursor()
                print()
                member_name = input(f"Dear {admin_name.capitalize()}, enter the name of the member to be removed: ")
                c.execute(f"SELECT COUNT(*) FROM members WHERE name=?", (member_name,))
                if c.fetchone()[0] == 0:
                    print()
                    print(f"Oops sorry {admin_name}, such member is not found in the library. Please try again!")
                    logging.error("No found member to be removed by the admin!")
                    return
                
                c.execute("DELETE FROM members WHERE name=?", (member_name,))
                conn.commit()
                conn.close()
                print(f"The Member: {member_name} and it info has been remove succesfully from library by {admin_name}")
                logging.error(f"Member {member_name} has been removed by {admin_name} - admin.")
                
            
            except Exception as e:
                logging.warning(f"Error in Library.py: {e}") 
                print()
                print(f"Error: {e}, please try again!") 
        
        else:
            print("Connection problem!")
            logging.warning(f"Connection problem in Library.py")          
                
        
