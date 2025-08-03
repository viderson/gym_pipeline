from . import connect

def get_all_users():
    """Select all users"""
    with connect() as conn:
        cursor = conn.cursor()
        return cursor.execute("SELECT * FROM users").fetchall()
