import sqlite3 as sq

def books_data():
    with sq.connect('books.db') as con:
        cur = con.cursor()
        cur.execute(
        '''CREATE TABLE IF NOT EXISTS books (
            book_id integer primary key autoincrement,
            name text,
            author text,
            style text,
            section text);''')
        


