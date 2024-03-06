# This is a deliberately poorly implemented main script for a Library Management System.

from book_management import Library
from user_management import Members
from register_management import Register
from datetime import datetime
# import user_management
# import checkout_management

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. Get User by user_id")
    print("5. Check-In Book")
    print("6. Check-Out Book")
    print("7. Get list of checked-in books by User")
    print("8. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    library = Library()
    members = Members()
    register = Register()
    library.add_book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "9780590353403")
    library.add_book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
    library.add_book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")  # This should be added
    library.add_book("1984", "George Orwell", "9780451524935")  # This should be added
    while True:
        choice = main_menu()
        match choice:
            case '1':
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                library.add_book(title, author, isbn)
            case '2':
                library.list_books()
            case '3':
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                members.add_user(name, user_id)
            case '4':
                user_id = input("Enter user ID: ")
                user = members.get_user(user_id)
                print(f"User: {user.name}")
            case '5':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to check-in: ")
                register.check_in_book(user_id, isbn)
            case '6':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                register.check_out_book(user_id, isbn)
            case '7':
                user_id = input("Enter user ID: ")
                all_books = register.get_all_checked_in_books(user_id)
                for book in all_books:
                    print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Check-in date: {book.check_in_date}")
                    dt_object = datetime.fromtimestamp(book.check_in_date)
                    formatted_date = dt_object.strftime("%d-%m-%Y %H:%M")
                    print(f"Check-in date: {formatted_date}")
            case '8':
                print("Exiting.")
                break
            case _:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
