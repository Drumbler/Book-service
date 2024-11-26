import os
from book import BookStatus
from book_repo import book_repository
from exceptions import BookIsMissing, BookIsOnTheShelf, BookNotFound, InvalidYear


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_books():
    clear()
    if not book_repository.books:
        print("\nNo books found.")
    for book in book_repository.get_books():
        print(book)


def add_book():
    clear()
    try:
        title = input("Enter title: ")
        author = input("Enter author: ")
        year = int(input("Enter publication year: "))
        book_repository.add_book(title, author, year)
    except ValueError:
        print("\nInvalid input.")
        return
    except InvalidYear:
        print("\nInvalid year. Book cannot be from the future")
        return
    print()
    print(f"book '{title}' added successfully")
    print()
    input("Press any key to continue...")
    clear()


def remove_book():
    clear()
    display_books()
    print()
    try:
        book_to_delete_id = int(input("Enter book to delete: "))
    except ValueError:
        print("\nInvalid book id. Please enter a valid integer.")
        return
    deleted_book = book_repository.get_books()[-1].title
    try:
        book_repository.remove_book(book_to_delete_id)
    except BookNotFound:
        print("\nBook not found.")
        return
    print(f"Book '{deleted_book}' successfully deleted")
    print()
    input("Press any key to continue...")
    clear()


def alter_book():
    clear()
    display_books()
    try:
        book_to_alter_id = int(
            input("Enter book id to take/return it to/from shelf: "))
    except ValueError:
        print("\nInvalid book id. Please enter a valid integer.")
        return
    altered_book = book_repository.get_books()[-1].title
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
    if status == BookStatus.IN_STOCK:
        print(f"Book '{altered_book}' successfully returned")
    elif status == BookStatus.OUT_OF_STOCK:
        print(f"Book '{altered_book}' successfully taken")
    print()
    input("Press any key to continue...")
    clear()


def find_book():
    search_query = input("Enter a search query: ")
    print("\n")
    books = book_repository.find_book(search_query)
    if not books:
        print("No books found.")
        return
    print("Search results:")
    for book in books:
        print(book)
    print()
    input("Press any key to continue...")
    clear()


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
