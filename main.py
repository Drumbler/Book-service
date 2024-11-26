import os
from book import BookStatus
from book_repo import book_repository
from exceptions import BookIsMissing, BookIsOnTheShelf, BookNotFound


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_books():
    print("\n")
    for book in book_repository.get_books():
        print(book)


def add_book():
    last_id = book_repository.get_books()[-1].book_id
    new_id = str(int(last_id) + 1)
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = input("Enter publication year: ")
    book_repository.add_book(new_id, title, author, year)
    clear()


def remove_book():
    try:
        book_to_delete_id = int(input("Enter book to delete: "))
    except ValueError:
        print("\nInvalid book id. Please enter a valid integer.")
        return
    try:
        book_repository.remove_book(book_to_delete_id)
    except BookNotFound:
        print("\nBook not found.")


def alter_book():

    try:
        book_to_alter_id = int(
            input("Enter book id to take/return it to/from shelf: "))
    except ValueError:
        print("\nInvalid book id. Please enter a valid integer.")
        return
    print("Possible statuses: \n1. 'In-stock'\n2. 'Out-of-stock'")
    status = input("Enter new status: ")
    book_status = {
        "1": BookStatus.IN_STOCK,
        "2": BookStatus.OUT_OF_STOCK,
    }.get(status, None)
    if book_status is None:
        print("\nInvalid status. Please enter a valid integer (1 or 2).")
        return
    try:
        book_repository.alter_book(book_to_alter_id, book_status)
    except BookNotFound:
        print("Book not found")
    except BookIsOnTheShelf:
        print("Book is already on the shelf")
    except BookIsMissing:
        print("Book is already taken")


def find_book():
    search_query = input("Enter a search query: ")
    print("\n")
    books = book_repository.find_book(search_query)
    if not books:
        print("No books found.")
        return
    for book in books:
        print(book)
# добавить поиск по наличию 

def main():
    book_repository.load_books()
    while True:
        print()
        print("1. Display all books")
        print("2. Add a new book")
        print("3. Remove a book")
        print("4. Take a book(change the status of the book)")
        print("5. Find a book")
        print("0. Exit")
        print()

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\nInvalid choice. Please enter a number.")
            continue

        match(choice):
            case 1:
                display_books()
            case 2:
                add_book()
            case 3:
                remove_book()
            case 4:
                alter_book()
            case 5:
                find_book()
            case 0:
                print("\nExiting...")
                return
            case _:
                print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
