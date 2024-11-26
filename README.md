# ENG
### Project Description

The Book-service project is implemented in Python 3.12.1.
The project itself is a console application that keeps track of books. In other words, the application stores data about all the books added by users, including the book's status ("in-stock", "out-of-stock").
During the development of the service, the principles of OOP were followed to create clean and readable code, with the ability to easily add new functionality.

### Project Functionality

When you run the application, a menu appears in the console:
```
1. Display all books
2. Add a new book
3. Remove a book
4. Take a book(change the status of the book)
5. Find a book
0. Exit
```


When navigating to the 1st menu item "Display all books", a list of all books is displayed in the console.

When adding a book, the user is prompted to enter the book's title, author, and publication year. The book's status is set to "in-stock" by default. An automatic book ID is assigned to the book before it is added.

In the "Delete a book" submenu, the user is prompted to enter the book's ID. If the book ID is invalid, an error message is displayed, and the user is returned to the main menu.

In the "Take a book/Return a book" menu item, the user is prompted to choose whether to take or return a book. If the book is already on the shelf and the user tries to return it, an error message is displayed. If the book is not on the shelf and the user tries to take it, an error message is displayed. If the user enters an invalid book ID or status, an error message is displayed, and the user is returned to the main menu.

In the "Find a book" menu item, the user is prompted to enter a search query. The application searches for books by title, author, or publication year and displays the matching books. If no books are found, an error message is displayed.

The last menu item is for exiting the program.

### Data storage implementation
Data storage is handled by the `BookRepository` class, which stores `Book` objects. To ensure that the application remembers added books even after restarting, data is saved to a `data.json` file in JSON format.


# RUS
### Описание проекта 
Проект Book-service реализован на ЯП Python 3.12.1.
Сам проект под собой подразумевает консольное приложение, которое ведет учет книг. Другими словами приложение хранит данные о всех добавленных пользователем книгах, в том числе статус книги("в наличии", "нет в наличии"). 
При разработке сервиса придерживался принципов ООП, для создания чистого и читаемого кода, с возможностью легкого добавления нового функционала
### Функционал проекта
Запустив приложение, в консоли появляется меню:
```
1. Показать все книги
2. Добавить новую книгу
3. Удалить книгу
4. Взять книгу с полки/поставить книгу на полку(изменение статуса книги)
5. Найти книгу
0. Выход
```
При навигации в 1 пункт меню "Показать все книги", в консоль списком выводятся все книги

При добавлении книги нужно уточнить название книги, автора и год выпуска книги, статус книги по-умолчанию "В наличии". Так же реализовано автоматическая нумерация книг, другими словами, при добавлении новой книги, она получает свой идентификатор, который присваивается книге до момента ее удаления.

Для удаления книги пользователь должен перейти в подменю "Удалить книгу", в котором требуется указать ID книги, которую пользователь хочет удалить. После книга удаляется, если введен неверный ID книги, то приложение сообщает об ошибке в ID и возвращается в главное меню.

При выборе пункта меню "Взять книгу с полки/поставить книгу на полку" пользователю предлагается выбрать что сделать с книгой "взять/вернуть", Если книга уже есть на полке и пользователь пытается вернуть книгу, то приложение сообщает об ошибке, что книга уже есть на полке, Если книги нет на полке, то по аналогии приложение сообщает о том, что книга уже взята. Если пользователь укажет несуществующую книгу или несуществующий статус, то приложение выводит ошибку и возвращается в главное меню 

Так же в приложении реализован поиск книги по запросу. При навигации в пункт меню "5. Поиск книги", пользователю будет предложено написать поисковой запрос, который найдет книгу либо по названию, либо по автору, либо по году выпуска. Если пользователь введет запрос, по которому функция ничего не найдет, то выведется сообщение "Книга не найдена".

Последний пункт меню для выхода из программы.

### Реализация хранения данных
Хранение данных осуществляется через class BookRepository, который хранит в себе объекты класса Book, в которых уже хранится вся информация о книге. Для того, чтобы приложение "запоминало" все добавленные книги, даже после перезапуска приложения, данные сохраняются в файле data.json, в формате json.

