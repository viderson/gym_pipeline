from . import connect

def add_user(name, email):
    """ add user to database """
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        return cursor.fetchone()[0]
