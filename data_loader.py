import json
from database import addTraining_session, add_exercise_with_session_key

def load_session_from_json(file_path):
    with open(file_path, 'r') as f:
        sessions = json.load(f)
    
    for session in sessions:
        training_day = session["training_day"]
        body_weight = session["body_weight"]
        mood = session["mood"]
        date = session["date"]

        session_id = addTraining_session(training_day, body_weight, mood, date)

    for ex in session["exercises"]:
        add_exercise_with_session_key(
            session_id,
            ex["exercise"],
            ex["weight"],
            ex["reps"]
        )
    print(f"Loaded session: {training_day} ({date})")

