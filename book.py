import enum


class BookStatus(enum.Enum):
    IN_STOCK = "in-stock"
    OUT_OF_STOCK = "out-of-stock"


class Book:
    def __init__(self, book_id, title, author, year, status: BookStatus):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self) -> str:
        return f"Title: {self.book_id}. {self.title}, author: {self.author}, year {self.year}, status: {self.status.value}"

    def update_status(self, new_status):

        self.status = new_status

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status.value,
        }
