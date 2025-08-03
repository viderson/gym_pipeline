from database import init_db
from data_loader import load_data


def main():
    init_db()
    load_data("sample_data_1000_sessions.json")
    print("Database initialized and data loaded.")


if __name__ == "__main__":
    main()