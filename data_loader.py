import json
from database.users import add_user
from database.sessions import add_training_session
from database.exercises import add_exercise

def load_data(file_path):
    with open(file_path, 'r') as f:
        users_data = json.load(f)

    for user_data in users_data:
        user = user_data["user"]
        user_id = add_user(user["name"], user["email"])

        for session in user_data["sessions"]:
            session_id = add_training_session(
                user_id,
                session["training_day"],
                session["body_weight"],
                session["mood"],
                session["date"],
                session.get("chest"), session.get("arms"), session.get("waist"),
                session.get("legs"), session.get("shoulders"),
                session.get("training_duration_minutes"), session.get("sleep_hours"),
                session.get("stress_level"), session.get("program_phase")
            )

            for ex in session["exercises"]:
                add_exercise(
                    session_id,
                    ex["exercise"],
                    ex["muscle_group"],
                    ex["weight"],
                    ex["reps"]
                )
