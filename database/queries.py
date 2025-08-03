from . import connect

def get_all_users():
    """
    Returns a list of all users from the 'users' table.

    Returns:
        List[Tuple[int, str, str]]: [(id, name, email), ...]
    """
    with connect() as conn:
        cursor = conn.cursor()
        return cursor.execute("SELECT * FROM users").fetchall()
def get_training_data_for_user(user_id: int):
    """
    Returns all training data for a given user by joining exercises and sessions.

    Returns:
        List[Tuple]: 
            (session_id, training_day, date, body_weight, mood,
             chest, arms, waist, legs, shoulders,
             training_duration_minutes, sleep_hours, stress_level, program_phase,
             exercise, muscle_group, weight, reps)
    """
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT
            ts.id AS session_id,
            ts.training_day,
            ts.date,
            ts.body_weight,
            ts.mood,
            ts.chest,
            ts.arms,
            ts.waist,
            ts.legs,
            ts.shoulders,
            ts.training_duration_minutes,
            ts.sleep_hours,
            ts.stress_level,
            ts.program_phase,

            e.exercise,
            e.muscle_group,
            e.weight,
            e.reps
        FROM training_sessions ts
        JOIN exercises e ON ts.id = e.session_id
        WHERE ts.user_id = ?
        ORDER BY ts.date ASC, ts.id ASC;
        """, (user_id, ))
        return cursor.fetchall()
