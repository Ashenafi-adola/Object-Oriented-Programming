from .classes import Book, Patrons, Library
library = Library()
def create_patron():
    name = input("Enter Patron's Name: ")
    id = input("Enter Patron's ID: ")
    return Patrons(name,id)

def new_book():
    titleauthor = input("Enter Book's Title: ")
    author = input("Enter Book's Author: ")
    return Book(titleauthor,author)

def get_book(books):
    title = input("Enter the Book title: ")
    for book in books:
        if book.title == title:
            return book
        
def get_patron(patrons):
    id = input("Enter the Patron's ID: ")
    for patron in patrons:
        if patron.id == id:
            return patron.id


while True:
    print("________main page________")
    print("|  1. Add patron         |")
    print("|  2. Add Book           |")
    print("|  3. Find Book          |")
    print("|  4. Lend Book          |")
    print("|__5._Accept_Book________|")
    choice = int(input("ENTER YOUR CHOICE: "))
    match choice:
        case 1:
            library.add_patron(create_patron())
        case 2:
            library.add_book(new_book())
        case 3:
            title = input("Enter the book title: ")
            library.find_book(title)
        case 4:
            library.lend_book(get_book(library.books),get_patron(library.patrons))
        case 5:
            library.accept_return(get_book(library.books),get_patron(library.patrons))