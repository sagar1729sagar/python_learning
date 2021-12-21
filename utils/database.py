from typing import List, Union

from utils.database_connection import DatabaseConnection
books_file = 'books.txt'
Book = Union[str, int]


def create_book_table() -> None:
    # connection = sqlite3.connect('data.db')
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name TEXT PRIMARY KEY , author TEXT, read INTEGER)')
    # connection.commit()
    # connection.close()


def get_all_books() -> List[tuple(str, str, bool)]:
    # connection = sqlite3.connect('data.db')
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
    # connection.commit()
    # connection.close()
    # print(books)
    return books


def add_book(name: Book, author: str) -> None:
    # connection = sqlite3.connect('data.db')

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO books VALUES (?,?,0)", (name, author))
    # connection.commit()
    # connection.close()


def _save_all_books(books) -> None:
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def mark_book_as_read(name: Book) -> None:
    # connection = sqlite3.connect('data.db')
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=? WHERE name=?',(1,name))
    # connection.commit()
    # connection.close()


def delete_book(name: Book) -> None:
    # connection = sqlite3.connect('data.db')
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name = ?',(name,))
    # connection.commit()
    # connection.close()

# def delete_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)
