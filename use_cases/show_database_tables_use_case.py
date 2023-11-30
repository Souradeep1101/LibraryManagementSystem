from mysql.connector import Error


class ShowDatabaseTablesUseCase:
    """
    Use case for searching existing database tables from the library.

    Attributes:
        repository (UserRepository or LoanRepository or BookRepository): Repository for user-related operations.
    """

    def __init__(self, repository):
        self.repository = repository

    def execute(self, table_name, fetchone=True):
        """
        Executes the book searching process.

        Parameters: table_name (str): The table name of the database. The table_name must be either of these (
        'books', 'users', 'loans')

        fetchone (bool): Check if the user needs only one record.
        """
        try:
            if table_name == 'books':
                data = self.repository.get_books(fetchone)
            elif table_name == 'users':
                data = self.repository.get_users(fetchone)
            elif table_name == 'loans':
                data = self.repository.get_loans(fetchone)
            else:
                raise Exception("Error: Couldn't retrieve table. 'table_name' not entered correctly.")
            return data
        except Error as e:
            print(f"An error occurred: {e}")
            return f"An error occurred: {e}"
