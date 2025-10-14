class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def is_checked(self):
        self.is_checked_out = True
    
    def return_book(self):
        self.is_checked_out = False

    def get_book_details(self):
        print(f"Book title {self.title} \nBook Author {self.author} \nBook is checked {self.is_checked_out}")

class Patrons:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_book = []

    def borrow_book(self, book):
        self.borrowed_book.append(book)
        book.is_checked()
    
    def return_book(self, book):
        self.borrowed_book.remove(book)
        book.return_book()

    def list_borrowed_books(self):
        for book in self.borrowed_book:
            print(f"Book {book.title} Author {book.author}")


class Library:
    def __init__(self):
        self.patrons = []
        self.books = []

    def add_book(self, book):
        self.books.append(book) 

    def add_patron(self, patron):
        self.patrons.append(patron)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                print(f'Book {book.title} Author {book.author}')

    def lend_book(self, book, patron_id):
        for patron in self.patrons:
            if patron.id == patron_id:
                patron.borrow_book(book)
                self.books.remove(book)

    def accept_return(self, book, patron_id):
        for patron in self.patrons:
            if patron.id == patron_id:
                patron.return_book(book)
                self.books.append(book)

library = Library()

while True:
    print("________main page________")
    print("|  1. Add patron         |")
    print("|  2. Add Book           |")
    print("|  3. Find Book          |")
    print("|  4. Lend Book          |")
    print("|__5. Accept Book________|")