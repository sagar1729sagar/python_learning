import sqlite3
books_file = 'books.txt'


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name TEXT PRIMARY KEY , author TEXT, read INTEGER)')
    connection.commit()
    connection.close()


def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]


def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books VALUES (?,?,0)', (name, author))
    connection.commit()
    connection.close()


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)


# def delete_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)
