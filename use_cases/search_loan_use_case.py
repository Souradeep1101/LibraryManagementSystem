from mysql.connector import Error


class SearchLoanUseCase:
    """
    Use case for searching loan(s) from the library.

    Attributes:
        loan_repository (LoanRepository): Repository for loan-related operations.
    """

    def __init__(self, loan_repository):
        self.loan_repository = loan_repository

    def execute(self, id_field_name, id_value, fetchone):
        """
        Executes the loan searching process.

        Parameters:
            id_field_name (str): The column/field name of the id.
            id_value (str or int): The unique identifier of the column/field.
            fetchone (bool): Check if the user needs only one loan.
        """
        try:
            loan = self.loan_repository.get_loans_by_id(id_field_name, id_value, fetchone)
            if not loan:
                raise Exception("Loan not found.")
            else:
                print("Loan(s) found successfully.")
                return loan
        except Error as e:
            print(f"An error occurred: {e}")
            return f"An error occurred: {e}"
