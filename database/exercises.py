from . import connect

def add_exercise(session_id, exercise_name, muscle_group, weight, reps):
    """
    Adds an exercise to the database, linked to a training session.
    """
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO exercises (
                session_id,
                exercise,
                muscle_group,
                weight,
                reps
            ) VALUES (?, ?, ?, ?, ?)
        """, (session_id, exercise_name, muscle_group, weight, reps))
        conn.commit()
