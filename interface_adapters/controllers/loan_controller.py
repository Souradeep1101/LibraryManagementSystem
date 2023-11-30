class LoanController:
    """
    Controller for handling loan-related requests.
    """

    def __init__(self, borrow_book_use_case, return_book_use_case, delete_loan_use_case, search_loan_use_case,
                 show_database_tables_use_case):
        self.show_database_tables_use_case = show_database_tables_use_case
        self.delete_loan_use_case = delete_loan_use_case
        self.borrow_book_use_case = borrow_book_use_case
        self.return_book_use_case = return_book_use_case
        self.search_loan_use_case = search_loan_use_case

    def borrow_book(self, book_id, user_id, loan_date, due_date):
        """
        Creates a new loan record for borrowing a book in the library.

        Parameters:
            book_id (int): The unique identifier of the book being loaned.
            user_id (int): The unique identifier of the user who is borrowing the book.
            loan_date (str): The date when the book is loaned out.
            due_date (str): The due date for returning the book.
        """
        try:
            self.borrow_book_use_case.execute(book_id, user_id, loan_date, due_date)
            return "Book borrowed successfully."
        except Exception as e:
            return str(e)

    def return_book(self, loan_id, return_date):
        """
        Updates a loan record for returning a book in the library.

        Parameters:
            loan_id (int): The unique identifier of the loan.
            return_date (str): The date when the book is loaned out.
        """
        try:
            self.return_book_use_case.execute(loan_id, return_date)
            return "Book returned successfully."
        except Exception as e:
            return str(e)

    def delete_loan(self, loan_id):
        """
        Deletes a loan record from the library system.

        Parameters:
            loan_id (int): The unique identifier of the loan to be deleted.
        """
        try:
            return self.delete_loan_use_case.execute(loan_id)
        except Exception as e:
            return str(e)

    def search_loan(self, id_field_name, id_value, fetchone=True):
        """
        Searches loan(s) from the library.

        Parameters:
            id_field_name (str): The column/field name of the id.
            id_value (str or int): The unique identifier of the column/field.
            fetchone (bool): Check if the user needs only one loan.
        """
        try:
            return self.search_loan_use_case.execute(id_field_name, id_value, fetchone)
        except Exception as e:
            return str(e)

    def get_loans(self, fetchone=True):
        """
        Retrieves all loan record(s) from the database.

        Parameters:
            fetchone (bool): Check if the user needs only one loan.

        Returns:
            Loan record(s) with their headers from the database.
        """
        try:
            return self.show_database_tables_use_case.execute('loans', fetchone)
        except Exception as e:
            return str(e)
