import streamlit as st
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

# Initializing controllers with the respective use cases
book_controller = BookController(add_book_use_case, update_book_info_use_case, delete_book_use_case)
user_controller = UserController(user_registration_use_case, update_user_info_use_case, delete_user_use_case)
loan_controller = LoanController(borrow_book_use_case, return_book_use_case, delete_loan_use_case)


def fetch_data(query):
    """
    Fetches data from the database based on the provided SQL query.

    Parameters:
        query (str): SQL query to execute.

    Returns:
        list: List of dictionaries where each dictionary represents a row of data.
    """
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def get_table_data(table_name):
    """
    Fetches all data from the specified table.

    Parameters:
        table_name (str): Name of the database table to fetch data from.

    Returns:
        list: List of dictionaries where each dictionary represents a row of data.
    """
    return fetch_data(f"SELECT * FROM {table_name}")


# Definition of form functions (add_book_form, update_book_form, register_user_form, borrow_book_form,
# return_book_form) remain unchanged.

def add_book_form():
    with st.form("Add Book"):
        title = st.text_input("Title")
        author = st.text_input("Author")
        isbn = st.text_input("ISBN")
        publication_year = st.number_input("Publication Year", min_value=1900, max_value=2023, step=1)
        genre = st.text_input("Genre")
        submit_button = st.form_submit_button("Add Book")

        if submit_button:
            result = book_controller.add_book(title, author, isbn, publication_year, genre)
            st.success(result)


def update_book_form():
    with st.form("Update Book Info"):
        book_id = st.number_input("Book ID", min_value=1, step=1)
        title = st.text_input("New Title")
        author = st.text_input("New Author")
        isbn = st.text_input("New ISBN")
        publication_year = st.number_input("New Publication Year", min_value=1900, max_value=2023, step=1)
        genre = st.text_input("New Genre")
        submit_button = st.form_submit_button("Update Book")

        if submit_button:
            result = book_controller.update_book_info(book_id, title, author, isbn, publication_year, genre)
            st.success(result)


def register_user_form():
    with st.form("Register User"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        role = st.text_input("Role (e.g., 'student', 'teacher', 'admin')")
        submit_button = st.form_submit_button("Register User")

        if submit_button:
            result = user_controller.register_user(name, email, role)
            st.success(result)


def borrow_book_form():
    with st.form("Borrow Book"):
        book_id = st.number_input("Book ID", min_value=1, step=1)
        user_id = st.number_input("User ID", min_value=1, step=1)
        loan_date = st.text_input("Loan Date (YYYY-MM-DD)")
        due_date = st.text_input("Due Date (YYYY-MM-DD)")
        submit_button = st.form_submit_button("Borrow Book")

        if submit_button:
            result = loan_controller.borrow_book(book_id, user_id, loan_date, due_date)
            st.success(result)


def return_book_form():
    with st.form("Return Book"):
        loan_id = st.number_input("Loan ID", min_value=1, step=1)
        return_date = st.text_input("Return Date (YYYY-MM-DD)")
        submit_button = st.form_submit_button("Return Book")

        if submit_button:
            result = loan_controller.return_book(loan_id, return_date)
            st.success(result)


def delete_user_form():
    """
    Create a form in Streamlit to delete a user.
    """
    with st.form("Delete User"):
        user_id = st.number_input("User ID to delete", min_value=1, step=1)
        submit_button = st.form_submit_button("Delete User")

        if submit_button:
            result = user_controller.delete_user(user_id)
            st.success(result)


def delete_loan_form():
    """
    Create a form in Streamlit to delete a loan.
    """
    with st.form("Delete Loan"):
        loan_id = st.number_input("Loan ID to delete", min_value=1, step=1)
        submit_button = st.form_submit_button("Delete Loan")

        if submit_button:
            result = loan_controller.delete_loan(loan_id)
            st.success(result)


def delete_book_form():
    """
    Create a form in Streamlit to delete a book.
    """
    with st.form("Delete Book"):
        book_id = st.number_input("Book ID to delete", min_value=1, step=1)
        submit_button = st.form_submit_button("Delete Book")

        if submit_button:
            result = book_controller.delete_book(book_id)
            st.success(result)


def main():
    """
        Main function to run the Streamlit application.
        Contains the navigation menu and page routing.
    """
    st.title("Library Management System")

    menu = ["Home", "Add Book", "Update Book Info", "Register User", "Borrow Book", "Return Book", "Delete User",
            "Delete Loan", "Delete Book", "Exit"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Books")
        books_data = get_table_data('books')
        st.dataframe(books_data)

        st.subheader("Users")
        users_data = get_table_data('users')
        st.dataframe(users_data)

        st.subheader("Loans")
        loans_data = get_table_data('loans')
        st.dataframe(loans_data)
    elif choice == "Add Book":
        add_book_form()
    elif choice == "Update Book Info":
        update_book_form()
    elif choice == "Register User":
        register_user_form()
    elif choice == "Borrow Book":
        borrow_book_form()
    elif choice == "Return Book":
        return_book_form()
    elif choice == "Delete User":
        delete_user_form()
    elif choice == "Delete Loan":
        delete_loan_form()
    elif choice == "Delete Book":
        delete_book_form()
    elif choice == "Exit":
        st.write("Exiting the application.")
        st.stop()


if __name__ == "__main__":
    main()
