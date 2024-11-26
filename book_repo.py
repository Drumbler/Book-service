import json
import os
from book import Book, BookStatus
from exceptions import BookNotFound, BookIsMissing, BookIsOnTheShelf, InvalidYear
from datetime import datetime


class BookRepository:

    def __init__(self):
        self.books = []

    def __find_book_by_id(self, book_id):
        book = next(
            (book for book in book_repository.books if book.book_id == str(book_id)), None)
        if book is None:
            raise BookNotFound

        return book

    def load_books(self):
        if not os.path.exists("database/data.json"):
            with open("database/data.json", 'w', encoding='utf-8') as file:
                json.dump([], file, ensure_ascii=False, indent=4)

        with open("database/data.json", 'r', encoding='utf-8') as file:
            self.books = [Book(
                book_id=data['book_id'],
                title=data['title'],
                author=data['author'],
                year=data['year'],
                status=BookStatus(data['status'])
            ) for data in json.load(file)]

    def get_books(self):
        return self.books

    def save_books(self):
        data = [book.to_dict() for book in book_repository.books]
        with open("database/data.json", 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def display_books(books):
        print("\n")
        for book in books:
            print(book)

    # добавить проверку на наличие символов в названии и т.д.
    def add_book(self, title, author, year: int):
        if not title or not author:
            raise ValueError("All fields must be filled")
        if not isinstance(year, int):
            raise ValueError("Year must be a valid integer")
        if year > datetime.now().year:
            raise InvalidYear("Book cannot be from the future")
        if self.books:
            last_id = int(self.books[-1].book_id)
            new_id = str(last_id + 1)
        else:
            new_id = "1"
        new_book = Book(new_id, title, author, year, BookStatus.IN_STOCK)
        self.books.append(new_book)
        self.save_books()

    def remove_book(self, book_to_remove_id):
        book_to_remove = self.__find_book_by_id(book_to_remove_id)
        self.books.remove(book_to_remove)
        self.save_books()

    def alter_book(self, book_to_alter_id, status):
        book_to_alter = self.__find_book_by_id(book_to_alter_id)
        if (status == BookStatus.OUT_OF_STOCK and
                book_to_alter.status == BookStatus.OUT_OF_STOCK):
            raise BookIsMissing
        elif (status == BookStatus.IN_STOCK and
              book_to_alter.status == BookStatus.IN_STOCK):
            raise BookIsOnTheShelf
        book_to_alter.update_status(status)
        self.save_books()

    def find_book(self, search_query):
        result = []
        search_lower = search_query.lower()
        for book in self.books:
            if (search_lower in book.title.lower() or
                search_lower in book.author.lower() or
                    str(book.year) == search_lower):
                result.append(book)
        return result


book_repository = BookRepository()
