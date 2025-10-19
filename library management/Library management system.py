from classes import *
import os
import time, pickle
file_name = "Patrons_list.pkl"
second_file = "Books_list.pkl"
try:
    with open(file_name, 'rb') as file:
        patrons = pickle.load(file)
except:
    patrons = []

try:
    with open(second_file, 'rb') as file:
        books = pickle.load(file)
except:
    books = []
library = Library()
library.patrons = patrons
library.books = books

while True:
    os.system('cls')
    print(" _______main page________")
    print("|  1. Add patron         |")
    print("|  2. Add Book           |")
    print("|  3. Find Book          |")
    print("|  4. Lend Book          |")
    print("|  5. Accept Book        |")
    print("|  6. Get Book Details   |")
    print("|  7. Borrowed Books     |")
    print("|  8. save data          |")
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
        case 8:
            with open(file_name, 'wb') as file:
                pickle.dump(library.patrons, file)
            with open(second_file, 'wb') as file:
                pickle.dump(library.books, file)
            break
        case _:
            print("Invalid input")
    time.sleep(2)