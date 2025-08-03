from . import connect

def add_user(name, email):
    """
    Adds a new user to the database if not already present.
    Returns the user ID.
    """
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO users (name, email)
            VALUES (?, ?)
        """, (name, email))
        conn.commit()

        cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        result = cursor.fetchone()
        return result[0] if result else None
