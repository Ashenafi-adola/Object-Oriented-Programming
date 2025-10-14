from classes import *

library = Library()

while True:
    print(" _______main page________")
    print("|  1. Add patron         |")
    print("|  2. Add Book           |")
    print("|  3. Find Book          |")
    print("|  4. Lend Book          |")
    print("|  5. Accept Book        |")
    print("|  6. Get Book Details   |")
    print("|  7. Borrowed Books     |")
    print("|________________________|")
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
            library.lend_book(get_book(library.books),get_patron(library.patrons).id)
        case 5:
            library.accept_return(get_book(library.books),get_patron(library.patrons).id)
        case 6:
            get_book(library.books).get_book_details()
        case 7:
            get_patron(library.patrons).list_borrowed_books()