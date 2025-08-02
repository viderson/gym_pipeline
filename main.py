from database import init_db
from data_loader import load_session_from_json
from database import count_sessions

def main():
    init_db()
    load_session_from_json("many_sessions_100.json")
    print(f"\n Total sessions in DB: {count_sessions()}")


if __name__ == "__main__":
    main()
