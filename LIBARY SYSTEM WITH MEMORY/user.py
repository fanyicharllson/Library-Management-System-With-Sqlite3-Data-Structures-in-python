class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def get_details(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Email: {self.email}"

    def is_admin(self):
        return False


class Admin(User):
    def is_admin(self):
        return True

    def add_book(self, library, book):
        library.add_book(book)

    def remove_book(self, library, book_id):
        library.remove_book(book_id)

    def update_book(self, library, book_id, new_title=None, new_author=None, new_genre=None):
        library.update_book(book_id, new_title, new_author, new_genre)

    def manage_members(self, library, user):
        library.add_user(user)


class Member(User):
    def borrow_book(self, library, book_id):
        print(f"User Id in memeber class: {self.user_id}")
        return library.borrow_book(self.user_id, book_id)

    def return_book(self, library, book_id):
        return library.return_book(self.user_id, book_id)
