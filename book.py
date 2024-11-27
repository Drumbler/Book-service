import enum


class BookStatus(enum.Enum):
    '''
    Enum for book status: availability on the shelf or not.
    '''
    IN_STOCK = "in-stock"
    OUT_OF_STOCK = "out-of-stock"


class Book:
    '''
    Model "Book", where all added book data is stored
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
        Method changes the book status to a new one
        '''
        self.status = new_status

    def to_dict(self) -> dict:
        '''
        Method returns a dictionary with book data
        '''
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status.value,
        }

