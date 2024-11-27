import os
from book import BookStatus
from book_repo import book_repository
from exceptions import BookIsMissing, BookIsOnTheShelf, BookNotFound, InvalidYear


def clear():
    '''
    Function to clear the console window
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def display_books():
    '''
    Function to display all books from the library
    If the library is empty, it prints a message indicating that no books are found
    Prints a list of books with their information
    '''
    clear()
    found = False
    for book in book_repository.get_books():
        print(book)
        found = True
    if not found:
        print("\nNo books found.")


def add_book():
    '''
    Function to add a book to the library
    The user is required to enter: book title, author, and publication year
    The book is added with the status "In stock" ("in-stock")
    '''
    clear()
    title = input("Enter title: ")
    if not title:
        print("\nTitle cannot be empty.\n")
        input("Press enter to continue...")
        return
    author = input("Enter author: ")
    if not author:
        print("\nAuthor cannot be empty.\n")
        input("Press enter to continue...")
        return
    try:
        year = int(input("Enter publication year: "))
    except ValueError:
        print("\nInvalid input.")
        return
    if year < 0:
        print("\nPlease enter a valid year.")
        return
    try:
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
    input("Press enter to continue...")
    clear()


def remove_book():
    '''
    Function to remove a book from the library
    The user is required to enter only the book ID
    '''
    clear()
    # For convenience, a list of all books is displayed before selecting the book ID
    display_books()
    print()
    try:
        book_to_delete_id = int(input("Enter book id to delete: "))
    except ValueError:
        print("\nInvalid book id. Please enter a valid integer.")
        return
    try:
        deleted_book = book_repository.remove_book(book_to_delete_id)
    except BookNotFound:  # Error handling in case the user enters a non-existent ID
        print("\nBook not found.")
        return
    print(f"Book '{deleted_book.title}' successfully deleted")
    print()
    input("Press enter to continue...")
    clear()


def alter_book():
    '''
    Function to change the status of a book
    ("in stock"/"out of stock")
    '''
    clear()
    display_books()
    try:
        book_to_alter_id = int(
            input("Enter book id to take/return it to/from shelf: "))
    except ValueError:  # Error handling in case the user enters a non-integer value
        print("\nInvalid book id. Please enter a valid integer.")
        return
    print("Possible statuses: \n1. 'Return to the shelf'\n2. 'Take from the shelf'")
    status = input("Enter new status: ")
    book_status = {
        "1": BookStatus.IN_STOCK,
        "2": BookStatus.OUT_OF_STOCK,
    }.get(status, None)
    if book_status is None:
        print("\nInvalid status. Please enter a valid integer (1 or 2).")
        return
    try:
        altered_book = book_repository.alter_book(
            book_to_alter_id, book_status)
    except BookNotFound:  # Error handling if the provided ID does not match any book in memory
        print("Book not found")
    except BookIsOnTheShelf:  # Error handling if the book is being returned to the shelf again
        print("Book is already on the shelf")
    except BookIsMissing:  # Error handling if the book is being taken from the shelf again
        print("Book is already taken")
    if status == BookStatus.IN_STOCK:
        print(f"Book '{altered_book.title}' successfully returned")
    elif status == BookStatus.OUT_OF_STOCK:
        print(f"Book '{altered_book.title}' successfully taken")
    print()
    input("Press enter to continue...")
    clear()


def find_book():
    '''
    Function to search for books based on a given query
    '''
    clear()
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
    input("Press enter to continue...")
    clear()


def main():
    '''
    Main loop, main menu, where you can choose one of 6 actions
    All added books will have status 'in-stock' by default
    '''
    book_repository.load_books()
    while True:
        print()
        print("1. Display all books")
        print("2. Add a new book")
        print("3. Remove a book")
        print("4. Take a book/return a book(change the status of the book)")
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
