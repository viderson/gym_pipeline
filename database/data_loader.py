import json
from database.users import add_user
from database.sessions import add_training_session
from database.exercises import add_exercise

def load_data(file_path):
    # Wczytaj dane z pliku JSON
    with open(file_path, 'r') as f:
        users_records = json.load(f)  # lista użytkowników z sesjami

    for user_record in users_records:
        user_info = user_record["user"]
        sessions = user_record["sessions"]

        # Dodaj użytkownika do bazy i pobierz jego ID
        user_id = add_user(user_info["name"], user_info["email"])

        for session_data in sessions:
            # Dodaj sesję treningową do bazy
            session_id = add_training_session(
                user_id=user_id,
                training_day=session_data["training_day"],
                body_weight=session_data["body_weight"],
                mood=session_data["mood"],
                date=session_data["date"],
                chest=session_data.get("chest"),
                arms=session_data.get("arms"),
                waist=session_data.get("waist"),
                legs=session_data.get("legs"),
                shoulders=session_data.get("shoulders"),
                training_duration_minutes=session_data.get("training_duration_minutes"),
                sleep_hours=session_data.get("sleep_hours"),
                stress_level=session_data.get("stress_level"),
                program_phase=session_data.get("program_phase")
            )

            # Dodaj każde ćwiczenie do danej sesji
            for exercise in session_data["exercises"]:
                add_exercise(
                    session_id=session_id,
                    exercise_name=exercise["exercise"],
                    muscle_group=exercise["muscle_group"],
                    weight=exercise["weight"],
                    reps=exercise["reps"]
                )
