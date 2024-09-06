from user import Admin, Member
from book import Book
from library import Library

# name = "pages"
# name.capitalize()

def main():
    library = Library()

    # Create Admin
    admin = Admin(None, "Alice", "alice@library.com")

    # Create some books
    book1 = Book(None, "1984", "George Orwell", "Dystopian")
    book2 = Book(None, "To Kill a Mockingbird", "Harper Lee", "Fiction")

    # Admin adds books to the library
    admin.add_book(library, book1)
    admin.add_book(library, book2)

    # Create a member
    member = Member(None, "Bob", "bob@library.com")
    library.add_user(member)

    # Member borrows a book
    success = member.borrow_book(library, 1)
    if success:
        print(f"{member.name} successfully borrowed {book1.title}")
    else:
        print(f"{member.name} could not borrow {book1.title}")

    # Search for a book by title
    found_books = library.search_books(title="1984")
    for book in found_books:
        print(book.get_details())

    # Member returns a book
    success = member.return_book(library, 1)
    if success:
        print(f"{member.name} successfully returned {book1.title}")
    else:
        print(f"{member.name} could not return {book1.title}")

if __name__ == "__main__":
    main()
