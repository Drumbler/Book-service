import json
import os
from book import Book, BookStatus
from exceptions import BookNotFound, BookIsMissing, BookIsOnTheShelf


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
            return

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

    def add_book(self, last_id, title, author, year): # добавить проверку на наличие символов в названии и т.д.
        new_book = Book(last_id, title, author, year, BookStatus.IN_STOCK)
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
        for book in self.books:
            if (search_query.lower() in book.title.lower() or
                # убрать повторяющиеся search_query.lower()
                search_query.lower() in book.author.lower() or
                    str(book.year) == search_query.lower()):  # Добавить валидацию на год
                result.append(book)
        return result


book_repository = BookRepository()
