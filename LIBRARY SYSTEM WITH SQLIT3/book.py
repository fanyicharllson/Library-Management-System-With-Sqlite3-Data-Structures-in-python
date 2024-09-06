import logging


file_handler = logging.FileHandler("Application.log")
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(asctime)s: %(message)s', handlers=[file_handler])


class Book:
    def __init__(self, title, author, genre, admin_name):
        self.title = title
        self.author = author
        self.genre = genre
        self.admin_name = admin_name #The admin who added book
    
    def getting_book(self):
         try:
             print()
             print("Getting book...")
             print()
             number_of_books = int(input("How many books do you want to add? "))
             if number_of_books <= 0:
                    print()
                    print("Error: Book number cannot be negative or zero! Please try again.")
                   
             elif number_of_books >= 1:
                    books = []
                    for num_books in range(number_of_books):
                        print()
                        print(f"Entering book {num_books + 1} infomation...")
                        print()
                        self.title = input("Enter title for book {}: ".format(num_books + 1))
                        self.author = input("Enter author of the book {}: ".format(num_books + 1))
                        self.genre = input("Enter genre of the book {}: ".format(num_books + 1))
                        
                        book_tuple = (self.title, self.author, self.genre, self.admin_name)
                        books.append(book_tuple)
                    
                    return books, number_of_books   
             else:
                 print()
                 logging.info("Error: Invalid number of books from the class library")
                 print("Error: Invalid number of book") 
                 
         except Exception as e:
             logging.error(f"Error: {e}")
             print(f"Error: {e}")
    
    def updating_book(self):
        print()
        print("Updating book...")
        logging.info("Updating book in book class...")  
        
        try:
            book_title = input("Enter the book title: ")
            print()
            
            choice_update = input ("Enter the feature of the book you want to update(author, title, genre):  ").lower()
            if choice_update in ["title", "author", "genre"]:
                print()
                choice_update_type = input(f"Enter new {choice_update} of this book title {book_title}:  ")
                
                return book_title, choice_update, choice_update_type
                
            else:
                print("ERROR: Please enter either 'title' or 'author' or 'genre'! Please try again!")
                logging.error("Invalid from update_method in book class!")
            
        except Exception as e:
           print()
           logging.error("Invalid update argument from the user", e)
           print("Invalid update input, please try again!", e)          
    
    
    

                
        