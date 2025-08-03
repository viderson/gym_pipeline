import pandas as pd 
from database.queries import get_all_users, get_training_data_for_user

def build_user_dataframe(user_id: int) -> pd.DataFrame:
    rows = get_training_data_for_user(user_id)
    columns = [
        "session_id", "training_day", "date", "body_weight", "mood", "dchest", "arms", "waist", "legs", "shoulders", "training_duration_minutes",
        "sleep_hours", "stress_level", "program_phase", "exercise", "muscle_group", "weight", "reps"
    ]
    df = pd.DataFrame(rows,columns = columns)
    df["volume"] = df["weight"] * df["reps"]
    return df