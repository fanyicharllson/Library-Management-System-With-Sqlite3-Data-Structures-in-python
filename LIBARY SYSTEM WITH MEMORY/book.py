class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = True

    def get_details(self):
        return (f"Book ID: {self.book_id}, Title: {self.title}, "
                f"Author: {self.author}, Genre: {self.genre}, Available: {self.is_available}")

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        self.is_available = True
