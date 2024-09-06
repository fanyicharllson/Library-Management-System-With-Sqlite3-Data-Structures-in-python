import logging


file_handler = logging.FileHandler("Application.log")
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(asctime)s: %(message)s', handlers=[file_handler])


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
    
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
                        
                        book_tuple = (self.title, self.author, self.genre)
                        books.append(book_tuple)
                    
                    return books    
             else:
                 print()
                 logging.info("Error: Invalid number of books from the class library")
                 print("Error: Invalid number of book") 
                 
         except Exception as e:
             logging.error(f"Error: {e}")
             print(f"Error: {e}")


b1 = Book(None, None, None)
b = b1.getting_book()  
print(b)           
             
                       
            
                   
        