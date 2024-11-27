import enum


class BookStatus(enum.Enum):
    IN_STOCK = "in-stock"
    OUT_OF_STOCK = "out-of-stock"


class Book:
    '''
    Модель "Book", в ней хранятся все данные добавленной книги
    '''

    def __init__(self, book_id: int, title: str, author: str, year: int, status: BookStatus):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self) -> str:
        return (f"Title: {self.book_id}. {self.title}, author: {self.author}, year {self.year}, status: {self.status.value}")

    def update_status(self, new_status: BookStatus):
        '''
        Метод изменяет статус книги на новый
        '''
        self.status = new_status

    def to_dict(self) -> dict:
        '''
        Метод возвращает словарь с данными книги
        '''
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status.value,
        }
