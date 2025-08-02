from database.py import connect, init_db, addBook, get_books

def main():
    while True:
        print("\n1. Add Book\n2. Viev by Genre\ns. Count by Author\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            addBook()
        elif choice == '2':
            get_books()
        elif choice == '3':
            pass
        elif choice == '4':
            break

if __name__ == '__main__':
    main()