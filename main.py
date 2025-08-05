from database import init_db
from data_loader import load_data

def main():
    init_db()
    load_data("training_data.json")
    

if __name__ == "__main__":
    main()
