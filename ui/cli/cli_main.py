import sys
from tabulate import tabulate
# Importing database connection and controllers for handling business logic
from frameworks_and_drivers.database.database_connector import create_db_connection
from interface_adapters.controllers.book_controller import BookController
from interface_adapters.controllers.user_controller import UserController
from interface_adapters.controllers.loan_controller import LoanController
from interface_adapters.repositories.book_repository import BookRepository
from interface_adapters.repositories.user_repository import UserRepository
from interface_adapters.repositories.loan_repository import LoanRepository
# Importing use cases which contain the application's business rules
from use_cases.add_new_book_use_case import AddNewBookUseCase
from use_cases.update_book_info_use_case import UpdateBookInfoUseCase
from use_cases.user_registration_use_case import UserRegistrationUseCase
from use_cases.update_user_info_use_case import UpdateUserInfoUseCase
from use_cases.borrow_book_use_case import BorrowBookUseCase
from use_cases.return_book_use_case import ReturnBookUseCase
from use_cases.delete_user_use_case import DeleteUserUseCase
from use_cases.delete_book_use_case import DeleteBookUseCase
from use_cases.delete_loan_use_case import DeleteLoanUseCase
from use_cases.search_loan_use_case import SearchLoanUseCase
from use_cases.search_book_use_case import SearchBookUseCase
from use_cases.search_user_use_case import SearchUserUseCase
from use_cases.show_database_tables_use_case import ShowDatabaseTablesUseCase

# Establishing a connection to the database
db_connection = create_db_connection()

# Initializing repositories with the database connection
book_repository = BookRepository(db_connection)
user_repository = UserRepository(db_connection)
loan_repository = LoanRepository(db_connection)

# Initializing use cases with their respective repositories
add_book_use_case = AddNewBookUseCase(book_repository)
update_book_info_use_case = UpdateBookInfoUseCase(book_repository)
user_registration_use_case = UserRegistrationUseCase(user_repository)
update_user_info_use_case = UpdateUserInfoUseCase(user_repository)
borrow_book_use_case = BorrowBookUseCase(book_repository, loan_repository)
return_book_use_case = ReturnBookUseCase(loan_repository)
delete_book_use_case = DeleteBookUseCase(book_repository, loan_repository)
delete_user_use_case = DeleteUserUseCase(user_repository, loan_repository)
delete_loan_use_case = DeleteLoanUseCase(loan_repository)
search_loan_use_case = SearchLoanUseCase(loan_repository)
search_user_use_case = SearchUserUseCase(user_repository)
search_book_use_case = SearchBookUseCase(book_repository)
show_books_table_use_case = ShowDatabaseTablesUseCase(book_repository)
show_users_table_use_case = ShowDatabaseTablesUseCase(user_repository)
show_loans_table_use_case = ShowDatabaseTablesUseCase(loan_repository)

# Initializing controllers with the respective use cases
book_controller = BookController(add_book_use_case, update_book_info_use_case, delete_book_use_case,
                                 search_book_use_case, show_books_table_use_case)
user_controller = UserController(user_registration_use_case, update_user_info_use_case, delete_user_use_case,
                                 search_user_use_case, show_users_table_use_case)
loan_controller = LoanController(borrow_book_use_case, return_book_use_case, delete_loan_use_case, search_loan_use_case,
                                 show_loans_table_use_case)


def display_table_data(data, headers):
    """Display the fetched data in a table format using tabulate."""
    print(tabulate(data, headers=headers, tablefmt='grid'))


def fetch_and_display_table_data(table_name):
    """Fetch data from a specific table and display it."""
    if table_name == 'books':
        data = book_controller.get_books(fetchone=False)
    elif table_name == 'users':
        data = user_controller.get_users(fetchone=False)
    elif table_name == 'loans':
        data = loan_controller.get_loans(fetchone=False)
    else:
        raise Exception("Error: Couldn't retrieve table. 'table_name' not entered correctly.")
    headers = data['headers']  # This fetches the column headers
    content = data['content']  # This fetches the content of the table
    print(f"\n{table_name.title()} Data:")
    display_table_data(content, headers)


# Functionality to add, update, register, borrow, and return books along with viewing database tables

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    isbn = input("Enter ISBN: ")
    publication_year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    print(book_controller.add_book(title, author, isbn, publication_year, genre))


def update_book_info():
    book_id = int(input("Enter book ID: "))
    title = input("Enter new book title: ")
    author = input("Enter new author name: ")
    isbn = input("Enter new ISBN: ")
    publication_year = int(input("Enter new publication year: "))
    genre = input("Enter new genre: ")
    print(book_controller.update_book_info(book_id, title, author, isbn, publication_year, genre))


def register_user():
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    role = input("Enter user role (e.g., 'student', 'teacher', 'admin'): ")
    print(user_controller.register_user(name, email, role))


def borrow_book():
    book_id = int(input("Enter book ID: "))
    user_id = int(input("Enter user ID: "))
    loan_date = input("Enter loan date (YYYY-MM-DD): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    print(loan_controller.borrow_book(book_id, user_id, loan_date, due_date))


def return_book():
    loan_id = int(input("Enter loan ID: "))
    return_date = input("Enter return date (YYYY-MM-DD): ")
    print(loan_controller.return_book(loan_id, return_date))


def delete_user():
    """
    Prompt the user for the user ID and delete the specified user.
    """
    user_id = int(input("Enter user ID to delete: "))
    print(user_controller.delete_user(user_id))


def delete_loan():
    """
    Prompt the user for the loan ID and delete the specified loan.
    """
    loan_id = int(input("Enter loan ID to delete: "))
    print(loan_controller.delete_loan(loan_id))


def delete_book():
    """
    Prompt the user for the book ID and delete the specified book.
    """
    book_id = int(input("Enter book ID to delete: "))
    print(book_controller.delete_book(book_id))


def search_book():
    """
    Prompt the user for the book ID or book Title and search the specified book.
    """
    print('Search book with: ')
    print('1. Book ID')
    print('2. Book Title')
    choice = input("Enter your choice: ")
    if choice == '1':
        book_id = int(input("Enter book ID to search: "))
        book = book_controller.search_book('book_id', book_id, fetchone=False)
    elif choice == '2':
        book_title = input("Enter book Title to search: ")
        book = book_controller.search_book('title', book_title, fetchone=False)
    else:
        print('Invalid Choice! Please Try again!')
        return
    headers = book['headers']
    content = book['content']
    display_table_data(content, headers)


def search_user():
    """
    Prompt the user for the user ID or username and search the specified book.
    """
    print('Search user with: ')
    print('1. User ID')
    print('2. User Name')
    choice = input("Enter your choice: ")
    if choice == '1':
        user_id = int(input("Enter user ID to search: "))
        user = user_controller.search_user('user_id', user_id, fetchone=False)
    elif choice == '2':
        user_name = input("Enter user Name to search: ")
        user = user_controller.search_user('name', user_name, fetchone=False)
    else:
        print('Invalid Choice! Please Try again!')
        return
    headers = user['headers']
    content = user['content']
    display_table_data(content, headers)


def search_loan():
    """
    Prompt the user for the user ID or username and search the specified book.
    """
    print('Search loan with: ')
    print('1. Loan ID')
    print('2. User ID')
    print('3. Book ID')
    choice = input("Enter your choice: ")
    if choice == '1':
        loan_id = int(input("Enter loan ID to search: "))
        loan = loan_controller.search_loan('loan_id', loan_id, fetchone=False)
    elif choice == '2':
        user_id = int(input("Enter user ID to search: "))
        loan = loan_controller.search_loan('user_id', user_id, fetchone=False)
    elif choice == '3':
        book_id = int(input("Enter book ID to search: "))
        loan = loan_controller.search_loan('book_id', book_id, fetchone=False)
    else:
        print('Invalid Choice! Please Try again!')
        return
    headers = loan['headers']
    content = loan['content']
    display_table_data(content, headers)


def main():
    """The main loop of the CLI, presenting the user with different actions to choose from."""

    while True:
        print("\nLibrary Management System CLI")
        print("1. Add Book")
        print("2. Update Book Info")
        print("3. Register User")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. View Database Tables")
        print("7. Delete User")
        print("8. Delete Loan")
        print("9. Delete Book")
        print("10. Search User")
        print("11. Search Loan")
        print("12. Search Book")
        print("0. Exit")
        choice = input("Enter choice: ")

        # Handling user input and performing corresponding actions
        try:
            if choice == "1":
                add_book()
            elif choice == "2":
                update_book_info()
            elif choice == "3":
                register_user()
            elif choice == "4":
                borrow_book()
            elif choice == "5":
                return_book()
            elif choice == "6":
                # Viewing database tables
                for table in ["books", "users", "loans"]:
                    fetch_and_display_table_data(table)
            elif choice == "7":
                delete_user()
            elif choice == "8":
                delete_loan()
            elif choice == "9":
                delete_book()
            elif choice == "10":
                search_user()
            elif choice == "11":
                search_loan()
            elif choice == "12":
                search_book()
            elif choice == "0":
                # Exiting the system
                print("Exiting the system.")
                sys.exit(0)
            else:
                # Handling invalid choices
                print("Invalid choice. Please try again.")

        except Exception as e:
            # Handling any exceptions that occur during operations
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
