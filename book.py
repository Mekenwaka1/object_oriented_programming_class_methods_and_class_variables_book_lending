import random
from datetime import datetime

class Book:
    on_shelf = []
    on_loan = []
    due_date = None

    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def borrow(self):
        is_book_lent_out = self.lent_out()
        if is_book_lent_out == True:
            return False
        else:
            self.due_date = self.current_due_date()
            if Book in self.on_shelf: 
                self.on_shelf.remove(Book)
            self.on_loan.append(Book)
            return True

    def return_to_library(self):
        is_book_lent_out = self.lent_out()
        if is_book_lent_out == False:
            return False
        else:
            self.on_loan.remove(Book)
            self.on_shelf.append(Book)
            self.due_date = None
            return True
            
    def lent_out(self):
        if Book in self.on_loan:
            return True
        else:
            return False

    @classmethod
    def create(cls, title, author, ISBN):
        new_book = Book(title, author, ISBN)
        cls.on_shelf.append(new_book)
        return new_book

    @classmethod
    def current_due_date(cls):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14 # two weeks expressed in seconds  
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)

    @classmethod
    def overdue_books(self, cls):
        books_that_are_due = []
        now = datetime.now()

        for book in self.on_loan:
            if book.due_date < now:
                books_that_are_due.append(book)
        
        return books_that_are_due


    @classmethod
    def browse(cls):
        return random.choice(cls.on_shelf)


sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")
# print(Book.browse().title) # "Sister Outsider" (this value may be different for you)
# print(Book.browse().title) # "Ain't I a Woman?" (this value may be different for you)
print(len(Book.on_shelf)) # 3
print(len(Book.on_loan)) # 0
print(sister_outsider.lent_out()) # False
print(sister_outsider.borrow()) # True
print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 1
# print(sister_outsider.lent_out()) # True
# print(sister_outsider.borrow()) # False
print(sister_outsider.due_date) # 2017-02-25 20:52:20 -0500 (this value will be different for you)
# print(len(Book.overdue())) # 0
# print(sister_outsider.return_to_library()) # True
# print(sister_outsider.lent_out()) # False
print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 0