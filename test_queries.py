import pandas as pd
from database.queries import get_all_users, get_training_data_for_user

def main():
    users = get_all_users()
    print(users)
    Kuba_training_data = get_training_data_for_user(1) 
    print(Kuba_training_data[0])


if __name__ == "__main__":
    main()