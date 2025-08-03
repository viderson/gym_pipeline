from database.queries import get_all_users

def main():
    users = get_all_users()
    print(users)

if __name__ == "__main__":
    main()