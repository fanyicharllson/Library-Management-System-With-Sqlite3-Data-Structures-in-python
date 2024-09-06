from book import Book
from borrowing_record import BorrowingRecord

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.borrowing_records = []
        self.next_book_id = 1
        self.next_user_id = 1
        self.next_record_id = 1

    def add_book(self, book):
        print(book.book_id)
        book.book_id = self.next_book_id
        self.books.append(book)
        self.next_book_id += 1

    def remove_book(self, book_id):
        self.books = [book for book in self.books if book.book_id != book_id]

    def update_book(self, book_id, new_title=None, new_author=None, new_genre=None):
        for book in self.books:
            if book.book_id == book_id:
                if new_title:
                    book.title = new_title
                if new_author:
                    book.author = new_author
                if new_genre:
                    book.genre = new_genre

    def search_books(self, title=None, author=None, genre=None):
        results = []
        for book in self.books:
            if (title and title.lower() in book.title.lower()) or \
               (author and author.lower() in book.author.lower()) or \
               (genre and genre.lower() in book.genre.lower()):
                results.append(book)
        return results

    def add_user(self, user):
        user.user_id = self.next_user_id
        self.users.append(user)
        self.next_user_id += 1

    def remove_user(self, user_id):
        self.users = [user for user in self.users if user.user_id != user_id]

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def borrow_book(self, user_id, book_id):
        user = self.find_user(user_id)
        if user and not user.is_admin():
            for book in self.books:
                if book.book_id == book_id and book.is_available:
                    book.borrow_book()
                    record = BorrowingRecord(self.next_record_id, user_id, book_id)
                    self.borrowing_records.append(record)
                    self.next_record_id += 1
                    return True
        return False

    def return_book(self, user_id, book_id):
        for record in self.borrowing_records:
            if record.user_id == user_id and record.book_id == book_id and not record.return_date:
                record.update_return_date()
                for book in self.books:
                    if book.book_id == book_id:
                        book.return_book()
                        return True
        return False
