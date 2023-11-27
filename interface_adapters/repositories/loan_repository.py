from mysql.connector import Error


class LoanRepository:
    """
    Repository class for handling the database operations related to book loans.
    """

    def __init__(self, connection):
        """
        Initializes the LoanRepository with a database connection.

        Parameters:
            connection: A MySQL database connection object.
        """
        self.connection = connection

    def create_loan(self, book_id, user_id, loan_date, due_date):
        """
        Creates a new loan record in the database.

        Parameters:
            book_id (int): The unique identifier of the book being loaned.
            user_id (int): The unique identifier of the user who is borrowing the book.
            loan_date (datetime): The date when the book is loaned out.
            due_date (datetime): The due date for returning the book.
        """
        query = """
                INSERT INTO loans (book_id, user_id, loan_date, due_date) 
                VALUES (%s, %s, %s, %s)
                """
        args = (book_id, user_id, loan_date, due_date)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            self.connection.commit()
            print("Loan created successfully")
        except Error as e:
            print(f"Error: '{e}'")
            self.connection.rollback()

    def get_loan_by_id(self, loan_id):
        """
        Retrieves a loan record from the database by its ID.

        Parameters:
            loan_id (int): The unique identifier of the loan.

        Returns:
            A loan record from the database.
        """
        query = "SELECT * FROM loans WHERE loan_id = %s"
        args = (loan_id,)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            loan = cursor.fetchone()
            return loan
        except Error as e:
            print(f"Error: '{e}'")

    def update_loan(self, loan_id, book_id, user_id, loan_date, due_date, return_date):
        """
        Updates the details of an existing loan record in the database.

        Parameters:
            loan_id (int): The unique identifier of the loan to be updated.
            book_id (int): The updated unique identifier of the book.
            user_id (int): The updated unique identifier of the user.
            loan_date (datetime): The updated loan date.
            due_date (datetime): The updated due date.
            return_date (datetime): The date when the book was returned.
        """
        query = """
                UPDATE loans 
                SET book_id = %s, user_id = %s, loan_date = %s, due_date = %s, return_date = %s 
                WHERE loan_id = %s
                """
        args = (book_id, user_id, loan_date, due_date, return_date, loan_id)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            self.connection.commit()
            print("Loan updated successfully")
        except Error as e:
            print(f"Error: '{e}'")
            self.connection.rollback()

    def delete_loan(self, loan_id):
        """
        Deletes a loan record from the database.

        Parameters:
            loan_id (int): The unique identifier of the loan to be deleted.
        """
        query = "DELETE FROM loans WHERE loan_id = %s"
        args = (loan_id,)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            self.connection.commit()
            print("Loan deleted successfully")
        except Error as e:
            print(f"Error: '{e}'")
            self.connection.rollback()

    # Additional methods can be added here as needed.
