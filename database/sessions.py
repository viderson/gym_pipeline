from . import connect

def add_training_session(user_id, training_day, body_weight, mood, date,
                         chest=None, arms=None, waist=None, legs=None, shoulders=None,
                         training_duration_minutes=None, sleep_hours=None,
                         stress_level=None, program_phase=None):
    """ add training session with user key to database"""
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO training_sessions (
                user_id, training_day, body_weight, mood, date,
                chest, arms, waist, legs, shoulders,
                training_duration_minutes, sleep_hours, stress_level, program_phase
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (user_id, training_day, body_weight, mood, date,
              chest, arms, waist, legs, shoulders,
              training_duration_minutes, sleep_hours, stress_level, program_phase))
        return cursor.lastrowid
