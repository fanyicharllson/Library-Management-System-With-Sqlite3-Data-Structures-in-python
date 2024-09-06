from datetime import datetime

class BorrowingRecord:
    def __init__(self, record_id, user_id, book_id):
        self.record_id = record_id
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = datetime.now()
        self.return_date = None

    def update_return_date(self):
        self.return_date = datetime.now()
