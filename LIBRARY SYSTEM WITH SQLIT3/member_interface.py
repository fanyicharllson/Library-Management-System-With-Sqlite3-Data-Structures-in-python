import logging
from library import database

file_handler = logging.FileHandler("Application.log")
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s', handlers=[file_handler])


class MemeberInterface:
    def __init__(self):
        pass

    def saving_book_to_db(self, books_list, name):
        connection = database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/borrowed.db")
        
        if connection:
            c = connection.cursor()
            c.execute("SELECT COUNT(*) FROM borrow WHERE borrower_name=?", (name,))
            if c.fetchone()[0] > 0:
                logging.warning(f"{name} borrow failed!")
                print(f'Warning: {name}, you cannot borrow again! Repay the previous book you borrowed first.')
                return False  # Indicate failure

            try:
                c.executemany("INSERT INTO borrow (borrowed_book, author, genre, borrower_name) VALUES (?,?,?,?)", books_list)
                connection.commit()
                return True  # Indicate success
            except Exception as e:
                logging.error(f"Error: {e}")
                print(f"Error: {e}")
                return False  # Indicate failure
            finally:
                connection.close()  # Ensure the connection is closed
        return False  # Return False if connection fails

    def borrow_book(self, name):
        print("\nBorrowing book...")
        
        conn = database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/book.db")

        try:
            if conn:
                c = conn.cursor()
                book_title = input(f"{name}, enter the book title you want to borrow: ")
                c.execute("SELECT COUNT(*) FROM books WHERE title=?", (book_title,))
                if c.fetchone()[0] == 0:
                    print(f"{name}, the Book: {book_title} is not found in the library. Please try again.")
                    logging.error(f"Book borrowing failed: Book {book_title} not found.")
                    return
                
                c.execute("SELECT * FROM books WHERE title=?", (book_title,))
                borrowed_book = c.fetchone()

                borrow_tuple = (borrowed_book[1], borrowed_book[2], borrowed_book[3], name)
                
                # Now creating a list to hold multiple tuples
                borrow_list = [borrow_tuple]  # Assuming multiple entries will be added here

                if self.saving_book_to_db(borrow_list, name):  # Pass the list of tuples
                    c.execute("DELETE FROM books WHERE title=?", (book_title,))
                    conn.commit()
                    print(f"{name}, you successfully borrowed {book_title} from the library.")
                    logging.info(f"Book borrowing succeeded: Book {book_title} borrowed by {name}.")
                else:
                    print(f"Failed to borrow {book_title}. Please try again later.")
            else:
                print("Failed to connect to the book database in borrow_book method.")
        except Exception as e:
            logging.error(f"Error in member_interface: {e}")
            print(f"Error in member_interface: {e}")
        finally:
            if conn:
                conn.close()  # Ensure the connection is closed even in case of an error
    
    def adding_borrowed_book(self, return_book_list):
        conn = database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/book.db")
        try:
             if conn:
                 c = conn.cursor()
                 c.executemany("INSERT INTO books (title, author, genre, name_admin) VALUES (?, ?, ?, ?)", return_book_list)
                 conn.commit()
                 return True
             else:
                 print("Failed to connect to book database in adding_borrowed_book method")
                 return False
        
        except Exception as e:
               logging.error(f"Error in member_interface: {e}")
               print(f"Error in member_interface: {e}")
               return False
        
        finally:
            conn.close()       
            
                                  

    def return_book(self):
        print()
        print("Returning Book...")
        print("\n")
        
        conn  = database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/borrowed.db")
        try:
            if conn:
                c = conn.cursor()
                borrower_name = input("Enter your name to return book: ")
                borrower_book = input("Enter the title of the return book: ")
                
                c.execute("SELECT COUNT(*) FROM borrow WHERE borrowed_book=? AND borrower_name=? ", (borrower_book, borrower_name))
                
                if c.fetchone()[0] == 0:
                     print(f"The name: {borrower_name} did not borrow any book: '{borrower_book}'. Please try again.")
                     logging.error(f"Password returned failed: Name {borrower_name} not found.")
                     return
                
                c.execute("SELECT * FROM borrow WHERE borrower_name=?", (borrower_name,))
                borrowed_book = c.fetchone()

                borrow_tuple = (borrowed_book[1], borrowed_book[2], borrowed_book[3], "Returned Book")
                borrow_list = [borrow_tuple]
                
                if self.adding_borrowed_book(borrow_list):
                    c.execute("DELETE FROM borrow WHERE borrowed_book=? AND borrower_name=?", (borrower_book, borrower_name)) 
                    conn.commit()
                    logging.info(f"The name: {borrower_name} returned {borrower_book} - book successfully.")
                    print(f"The name: {borrower_name} returned {borrower_book} - book successfully.")
                
                else:
                    print(f"Failed to return the book: {borrower_book}. Please try again.") 
            
            else:
                print("Failed to connect to borrow book database. Please try again.")           
               
        except Exception as e:
            logging.error(f"Error in return_book method: {e}")
            print(f"Error in return_book method: {e}")
            
        finally:
            conn.close()
         
                    


def MemberOption(name=None):
    print("\n")
    logging.debug("Entering Member interface........")

    print("*********************************************")
    print("        Welcome Member Interface.......")
    print("*********************************************")
    print("\n")

    print("Select from the menu below")

    print("1) Borrow Book...")
    print("2) Return Book...")
    print("3) Return...")

    mem_interface = MemeberInterface()

    try:
        option = int(input("Enter your option:  "))
        
        match option:
            case 1:
                mem_interface.borrow_book(name)
            case 2:
                mem_interface.return_book()
            case 3:
                print("Returning...")
                return
            case _:
                print(f"Invalid option, you entered {option}! Try again.")
    except Exception as e:
        logging.error("Error in member_interface: " + str(e))
        print(f"Invalid Option. Please try again! Error: {e}")
