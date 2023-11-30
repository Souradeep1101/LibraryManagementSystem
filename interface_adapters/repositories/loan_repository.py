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
            loan_date (str): The date when the book is loaned out.
            due_date (str): The due date for returning the book.
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

    def get_loans_by_id(self, id_field_name, id_value, fetchone=True):
        """
        Retrieves loan record(s) from the database by its ID.

        Parameters:
            id_field_name (str): The column/field name of the id.
            id_value (str or int): The unique identifier of the column/field.
            fetchone (bool): Check if the user needs only one loan.

        Returns:
            Loan record(s) from the database.
        """
        query = f"SELECT * FROM loans WHERE {id_field_name} = %s"
        args = (id_value,)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            headers = [i[0] for i in cursor.description]
            if fetchone:
                loan = cursor.fetchone()
            else:
                loan = cursor.fetchall()
            return {'content': loan, 'headers': headers}
        except Error as e:
            print(f"Error: '{e}'")

    def get_loans(self, fetchone=True):
        """
        Retrieves all loan record(s) from the database.

        Parameters:
            fetchone (bool): Check if the user needs only one loan.

        Returns:
            Loan record(s) with their headers from the database.
        """
        query = f"SELECT * FROM loans"

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            headers = [i[0] for i in cursor.description]
            if fetchone:
                loans = cursor.fetchone()
            else:
                loans = cursor.fetchall()
            return {'content': loans, 'headers': headers}
        except Error as e:
            print(f"Error: '{e}'")

    def update_loan(self, loan_id, book_id, user_id, loan_date, due_date, return_date):
        """
        Updates the details of an existing loan record in the database.

        Parameters:
            loan_id (int): The unique identifier of the loan to be updated.
            book_id (int): The updated unique identifier of the book.
            user_id (int): The updated unique identifier of the user.
            loan_date (str): The updated loan date.
            due_date (str): The updated due date.
            return_date (str): The date when the book was returned.
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
