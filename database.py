import sqlite3

DB_NAME = 'library.dv'

def connect():
    return sqlite3.connect(DB_NAME)
def init_db():
    with connect() as conn:
        with open('schema.sql', 'r') as f:
            conn.executescript(f.read())
def addBook():
    with connect() as conn:
        conn.execute(
            "INSERT INTO books (title, author, genre, year_published) VALUES (?, ?, ?, ?)",
            (title, author, genre, year_published)
        )
def get_books():
    with connect() as conn:
        return conn.execute(
            "SELECT * FROM books".fetchall()
        )