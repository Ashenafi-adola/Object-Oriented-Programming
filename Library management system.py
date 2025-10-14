

class Book:
    def __init__(self, title, author, is_checked_out):
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out

    def is_checked(self):
        pass
    
    def return_book(self):
        pass

    def get_book_details(self):
        pass

class Patrons:
    def __init__(self, name, id, borrowed_book):
        self.name = name
        self.id = id
        self.borrowed_book = borrowed_book

    def borrow_book(self, book):
        pass
    
    def return_book(self, book):
        pass

    def list_borrowed_books(self):
        pass


class Library:
    def __init__(self, patrons, books):
        self.patrons = patrons
        self.books = books

    def add_book(self, book):
        pass 

    def add_patron(self, patron):
        pass

    def find_book(self, title):
        pass

    def lend_book(self, title, patron_id):
        pass

    def accept_return(self, title, patron_id):
        pass

    