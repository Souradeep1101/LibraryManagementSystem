import sys
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


def tuples_to_dicts(tuples, headers):
    """
    Converts a list of tuples into a list of dictionaries based on provided headers.

    Parameters:
        tuples (list of tuples): The data returned from the database.
        headers (list of str): The column headers for the data.

    Returns:
        list of dicts: Converted list of dictionaries.
    """
    return [dict(zip(headers, row)) for row in tuples]


def get_table_data(table_name):
    """
    Fetches all data from the specified table.

    Parameters:
        table_name (str): Name of the database table to fetch data from.

    Returns:
        list: List of dictionaries where each dictionary represents a row of data.
    """
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
    if content:
        return tuples_to_dicts(content, headers)
    else:
        return [dict(zip(headers, [None] * len(headers)))]


# Definition of form functions

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


def search_book_form():
    """
    Prompt the user for the book ID or book Title and search the specified book.
    """
    # Ensure the session state key exists
    if 'search_key' not in st.session_state:
        st.session_state['search_key'] = 'book_id'

    search_type = st.radio("Search book by", ["Book ID", "Book Title"])

    # Update the session state key based on the search type
    if search_type == "Book ID":
        search_key = 'book_id'
    else:
        search_key = 'title'

    # Update the session state
    st.session_state['search_key'] = search_key

    with st.form("Search Book"):
        # Conditional input fields based on the radio selection
        if search_type == "Book ID":
            book_id = st.number_input("Enter Book ID", min_value=1, step=1, key=search_key)
        else:
            book_title = st.text_input("Enter Book Title", key=search_key)

        submit_button = st.form_submit_button("Search Book")

        if submit_button:
            if search_type == "Book ID":
                book = book_controller.search_book(search_key, book_id, fetchone=False)
            else:
                book = book_controller.search_book(search_key, book_title, fetchone=False)

            if book['content']:
                headers = book['headers']  # This fetches the column headers
                content = book['content']  # This fetches the content of the table
                st.dataframe(tuples_to_dicts(content, headers))
            else:
                st.write("No results found.")


def search_user_form():
    """
    Create a form in Streamlit to search for a user by either their ID or name.
    """
    # Ensure the session state key exists
    if 'search_user_key' not in st.session_state:
        st.session_state['search_user_key'] = 'user_id'

    search_type = st.radio("Search user by", ["User ID", "User Name"], key='search_user_radio')

    # Update the session state key based on the search type
    search_key = 'user_id' if search_type == "User ID" else 'name'

    # Update the session state
    st.session_state['search_user_key'] = search_key

    with st.form("Search User"):
        # Conditional input fields based on the radio selection
        user_input = st.number_input("Enter User ID", min_value=1, step=1, key=search_key) \
            if search_type == "User ID" else \
            st.text_input("Enter User Name", key=search_key)

        submit_button = st.form_submit_button("Search User")

        if submit_button:
            user = user_controller.search_user(search_key, user_input, fetchone=False)

            if user['content']:
                headers = user['headers']  # This fetches the column headers
                content = user['content']  # This fetches the content of the table
                st.dataframe(tuples_to_dicts(content, headers))
            else:
                st.write("No results found.")


def search_loan_form():
    """
    Create a form in Streamlit to search for a loan by loan ID, user ID, or book ID.
    """
    # Ensure the session state key exists
    if 'search_loan_key' not in st.session_state:
        st.session_state['search_loan_key'] = 'loan_id'

    search_type = st.radio("Search loan by", ["Loan ID", "User ID", "Book ID"], key='search_loan_radio')

    # Update the session state key based on the search type
    search_key = 'loan_id' if search_type == "Loan ID" else ('user_id' if search_type == "User ID" else 'book_id')

    # Update the session state
    st.session_state['search_loan_key'] = search_key

    with st.form("Search Loan"):
        # Conditional input fields based on the radio selection
        if search_type == "Loan ID":
            loan_input = st.number_input("Enter Loan ID", min_value=1, step=1, key=search_key)
        elif search_type == "User ID":
            loan_input = st.number_input("Enter User ID", min_value=1, step=1, key=search_key)
        else:
            loan_input = st.number_input("Enter Book ID", min_value=1, step=1, key=search_key)

        submit_button = st.form_submit_button("Search Loan")

        if submit_button:
            loan = loan_controller.search_loan(search_key, loan_input, fetchone=False)

            if loan['content']:
                headers = loan['headers']  # This fetches the column headers
                content = loan['content']  # This fetches the content of the table
                st.dataframe(tuples_to_dicts(content, headers))
            else:
                st.write("No results found.")


def main():
    """
        Main function to run the Streamlit application.
        Contains the navigation menu and page routing.
    """
    st.title("Library Management System")
    st.text("Developed by Souradeep Banerjee 💗")
    st.divider()

    menu = ["Home", "Add Book", "Update Book Info", "Register User", "Borrow Book", "Return Book", "Delete User",
            "Delete Loan", "Delete Book", "Search Book",
            "Search User", "Search Loan", "Exit"]
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
    elif choice == "Search Book":
        search_book_form()
    elif choice == "Search User":
        search_user_form()
    elif choice == "Search Loan":
        search_loan_form()
    elif choice == "Exit":
        st.write("Exiting the application.")
        sys.exit()


if __name__ == "__main__":
    main()
