import sqlite3
import logging

DB_NAME = 'workout_data_base.db'

def connect():
    try:
        conn = sqlite3.connect(DB_NAME)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    except sqlite3.Erorr as e:
        logging.error(f"Failed to connect to DB: {e}")
        raise

def init_db():
    with connect() as conn:
        with open('schema.sql', 'r') as f:
            conn.executescript(f.read())
def addTraining_session(training_day: str, body_weight: float, mood: str, date: str) -> int:
    """ Add new training session and returnin ID."""
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO training_sessions (training_day, body_weight, mood, date)
             VALUES (?,?,?,?)
            """,
            (training_day, body_weight, mood, date)
        )
        return cursor.lastrowid


def add_exercise_with_session_key(session_id: int, excercise: str, weight: float, reps: int):
    """Add exercise to existing training session."""
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO exercises (session_id, exercise, weight, reps)
            VALUES (?,?,?,?)""",
            (session_id, excercise, weight, reps)
        )
def count_sessions():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM training_sessions")
        return cursor.fetchone()[0]
    
def get_all_session():
    with connect() as conn:
        cursor = conn.cursor()
        return cursor.execute("SELECT * FROM training_sessions").fetchall()

def get_exercises_for_session(session_id):
    with connect() as conn:
        cursor = conn.cursor()
        return cursor.execute("SELECT * FROM exercises WHERE session_id = ?", (session_id,)).fetchall()


# def addBook():
#     title = input("Title: ")
#     author = input("Author: ")
#     genre = input("Genre: ")
#     year_published = int(input("Year published: "))
#     with connect() as conn:
#         conn.execute(
#             "INSERT INTO books (title, author, genre, year_published) VALUES (?, ?, ?, ?)",
#             (title, author, genre, year_published)
#         )
# def get_books():
#     with connect() as conn:
#         return conn.execute(
#             "SELECT * FROM books"
#         ).fetchall()
# def delete_all_books():
#     with connect() as conn:
#         conn.execute(
#             "DELETE FROM books"
#         )
# def delete_book_id():
#     id = int(input("Chose book to delete by id "))
#     with connect() as conn:
#         conn.execute(
#             "DELETE FROM books WHERE id = ?", (id,)
#         )
#         print("book deleted")
# def get_books_by_genre():
#     genre = input("Chose genre book: ")
#     with connect() as conn:
#         return conn.execute(
#             "SELECT * FROM books WHERE genre = ?", (genre, )
#         ).fetchall()
# def count_books_by_author:
#     author = input("Chose author for counting")
#     with conect() as conn:
#         return conn.execute(
#             "SELECT author, COUNT(*) FROM books"
#         )