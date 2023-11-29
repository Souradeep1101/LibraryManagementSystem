from mysql.connector import Error


class DeleteLoanUseCase:
    """
    Use case for deleting a loan record from the library system.

    Attributes:
        loan_repository (LoanRepository): Repository for loan-related operations.
    """

    def __init__(self, loan_repository):
        self.loan_repository = loan_repository

    def can_delete_loan(self, loan_id):
        # Check if the loan exists
        loan = self.loan_repository.get_loans_by_id('loan_id', loan_id)
        return loan is not None

    def execute(self, loan_id):
        """
        Executes the process of deleting a loan record.

        Parameters:
            loan_id (int): The unique identifier of the loan to be deleted.
        """
        try:
            if self.can_delete_loan(loan_id):
                self.loan_repository.delete_loan(loan_id)
                print("Loan record deleted successfully.")
                return "Loan record deleted successfully."
            else:
                print("Cannot delete loan: Loan record not found.")
                return "Cannot delete loan: Loan record not found."
        except Error as e:
            print(f"An error occurred while deleting the loan record: {e}")
            return f"An error occurred while deleting the loan record: {e}"
