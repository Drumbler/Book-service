import json
import os
from typing import Iterable
from book import Book, BookStatus
from exceptions import BookNotFound, BookIsMissing, BookIsOnTheShelf, InvalidYear
from datetime import datetime


class BookRepository:

    '''
    Модель BookRepository имеет в себе приватный словарь __books, в котором хранятся 
    книги, предварительно выгруженные из файла data.json(Если книги имеются в файле data.json),
    и предварительно загруженные в память для их записи в data.json
    '''

    __books: dict[int, Book]

    def __init__(self): # инициализация класса
        self.__books = {}

    def find_book_by_id(self, book_id: int) -> Book: # Поиск книги в словаре __books по ID
        book = self.__books.get(book_id, None)
        if book is None: # Обработка ошибки, в случае, когда в словаре __books не было найдено ни одной книги 
            raise BookNotFound
        return book

    def load_books(self): # функция выгрузки книг из data.json в словарь __books
        if not os.path.exists("database/data.json"):
            return

        with open("database/data.json", 'r', encoding='utf-8') as file: # 
            books = [Book(
                book_id=data['book_id'],
                title=data['title'],
                author=data['author'],
                year=data['year'],
                status=BookStatus(data['status'])
            ) for data in json.load(file)]
        self.__books = {book.book_id: book for book in books}

    def get_books(self) -> Iterable[Book]: # Функция, которая возвращает объект итератор с данными книг
        return self.__books.values()

    def save_books(self): # Метод класса для сохранения записанных в __books книг, в data.json 
        data = [book.to_dict() for book in book_repository.__books.values()]
        with open("database/data.json", 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int): # Метод класса для добавления книги в словарь __books
        if not title or not author: # Проверка входных данных, на случай когда пользователь вместо названия или автора оставил пустую строку
            raise ValueError("All fields must be filled")
        if not isinstance(year, int): # проверка входных данных, на случай когда пользователь ввел строку вместо числа в поле Year
            raise ValueError("Year must be a valid integer") 
        if year > datetime.now().year: # валидация года выпуска книги 
            raise InvalidYear("Book cannot be from the future")
        new_id = max(self.__books.keys()) + 1 if len(self.__books) > 0 else 0
        new_book = Book(new_id, title, author, year, BookStatus.IN_STOCK)
        self.__books[new_id] = new_book
        self.save_books()

    def remove_book(self, book_to_remove_id: int) -> Book: # Метод для удаления книги из __books, после удаления изменения сразу сохраняются в data.json
        book_to_delete = self.find_book_by_id(book_to_remove_id)
        del self.__books[book_to_remove_id]
        self.save_books()
        return book_to_delete

    def alter_book(self, book_to_alter_id: int, status: BookStatus) -> Book: # Метод для изменения статуса книги 
        book_to_alter = self.find_book_by_id(book_to_alter_id)
        if (status == BookStatus.OUT_OF_STOCK and # Проверка входных данных, в случае если пользователь ввел тот же статус книги
                book_to_alter.status == BookStatus.OUT_OF_STOCK):
            raise BookIsMissing
        elif (status == BookStatus.IN_STOCK and
              book_to_alter.status == BookStatus.IN_STOCK):
            raise BookIsOnTheShelf
        book_to_alter.update_status(status)
        self.save_books()
        return book_to_alter

    def find_book(self, search_query) -> list[Book]: # Метод поиска книги по запросу пользователя
        result = []
        search_lower = search_query.lower()
        for book in self.__books.values():
            if (search_lower in book.title.lower() or
                search_lower in book.author.lower() or
                    str(book.year) == search_lower):
                result.append(book)
        return result


book_repository = BookRepository()
