import json
import os
from typing import Iterable
from book import Book, BookStatus
from exceptions import BookNotFound, BookIsMissing, BookIsOnTheShelf, InvalidYear
from datetime import datetime


class BookRepository:

    '''
    The BookRepository model has a private dictionary __books, where books are stored
    initially loaded from data.json file (if any books exist in the data.json file),
    and pre-loaded into memory for their writing to data.json
    '''

    __books: dict[int, Book]

    def __init__(self):  # class initialization
        self.__books = {}

    # Search for a book in the __books dictionary by ID
    def find_book_by_id(self, book_id: int) -> Book:
        book = self.__books.get(book_id, None)
        if book is None:  # Error handling, in case when the book was not found in the __books dictionary
            raise BookNotFound
        return book

    def load_books(self):  # Function to load books from data.json into the __books dictionary
        if not os.path.exists("database/data.json"):
            return

        with open("database/data.json", 'r', encoding='utf-8') as file:
            books = [Book(
                book_id=data['book_id'],
                title=data['title'],
                author=data['author'],
                year=data['year'],
                status=BookStatus(data['status'])
            ) for data in json.load(file)]
        self.__books = {book.book_id: book for book in books}

    # Function that returns an iterator object with book data
    def get_books(self) -> Iterable[Book]:
        return self.__books.values()

    def save_books(self):  # Method to save the books stored in __books to data.json
        data = [book.to_dict() for book in book_repository.__books.values()]
        with open("database/data.json", 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    # Method to add a book to the __books dictionary
    def add_book(self, title: str, author: str, year: int):
        if not title or not author:  # Input validation, in case when the user left the title or author field empty
            raise ValueError("All fields must be filled")
        # Input validation, in case when the user entered a string instead of an integer in the Year field
        if not isinstance(year, int):
            raise ValueError("Year must be a valid integer")
        if year > datetime.now().year:  # Book publication year validation
            raise InvalidYear("Book cannot be from the future")
        new_id = max(self.__books.keys()) + 1 if len(self.__books) > 0 else 0
        new_book = Book(new_id, title, author, year, BookStatus.IN_STOCK)
        self.__books[new_id] = new_book
        self.save_books()

    # Method to remove a book from __books, after removal, changes are saved immediately to data.json
    def remove_book(self, book_to_remove_id: int) -> Book:
        book_to_delete = self.find_book_by_id(book_to_remove_id)
        del self.__books[book_to_remove_id]
        self.save_books()
        return book_to_delete

    # Method to change the status of a book
    def alter_book(self, book_to_alter_id: int, status: BookStatus) -> Book:
        book_to_alter = self.find_book_by_id(book_to_alter_id)
        if (status == BookStatus.OUT_OF_STOCK and  # Input validation, in case when the user entered the same book status
                book_to_alter.status == BookStatus.OUT_OF_STOCK):
            raise BookIsMissing
        elif (status == BookStatus.IN_STOCK and
              book_to_alter.status == BookStatus.IN_STOCK):
            raise BookIsOnTheShelf
        book_to_alter.update_status(status)
        self.save_books()
        return book_to_alter

    # Method to search for a book by user query
    def find_book(self, search_query) -> list[Book]:
        result = []
        search_lower = search_query.lower()
        for book in self.__books.values():
            if (search_lower in book.title.lower() or
                search_lower in book.author.lower() or
                    str(book.year) == search_lower):
                result.append(book)
        return result


book_repository = BookRepository()
