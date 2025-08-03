from . import connect

def add_exercise(session_id, exercise, muscle_group, weight, reps):
    """ add exercise with training session key to database """
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO exercises (session_id, exercise, muscle_group, weight, reps)
            VALUES (?, ?, ?, ?, ?)
        """, (session_id, exercise, muscle_group, weight, reps))
