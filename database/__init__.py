import sqlite3
import os

folder_1 = os.path.dirname(__file__)
folder_1 = folder_1[:folder_1.rfind('\\')]
db_file_path = folder_1 + '\workout_data_base.db'

DB_NAME = db_file_path

def connect():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    with connect() as conn:
        with open(os.path.join(os.path.dirname(__file__), 'schema.sql'), 'r') as f:
            conn.executescript(f.read())
