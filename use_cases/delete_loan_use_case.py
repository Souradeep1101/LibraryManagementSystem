from mysql.connector import Error


class DeleteLoanUseCase:
    """
    Use case for deleting a loan record from the library system.

    Attributes:
        loan_repository (LoanRepository): Repository for loan-related operations.
    """

    def __init__(self, loan_repository):
        self.loan_repository = loan_repository

    def execute(self, loan_id):
        """
        Executes the process of deleting a loan record.

        Parameters:
            loan_id (int): The unique identifier of the loan to be deleted.
        """
        try:
            self.loan_repository.delete_loan(loan_id)
            print("Loan record deleted successfully.")
        except Error as e:
            print(f"An error occurred while deleting the loan record: {e}")
