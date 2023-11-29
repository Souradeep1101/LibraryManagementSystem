from mysql.connector import Error


class ReturnBookUseCase:
    """
    Use case for returning a book to the library.

    Attributes:
        loan_repository (LoanRepository): Repository for loan-related operations.
    """

    def __init__(self, loan_repository):
        self.loan_repository = loan_repository

    def execute(self, loan_id, return_date):
        """
        Executes the book returning process.

        Parameters:
            loan_id (int): The ID of the loan record.
            return_date (datetime): The date when the book is returned.
        """
        try:
            loan = self.loan_repository.get_loans_by_id('loan_id', loan_id)
            if not loan:
                raise Exception("Loan record not found.")

            self.loan_repository.update_loan(
                loan_id, loan[1], loan[2], loan[3], loan[4], return_date
            )
            print("Book returned successfully.")
        except Error as e:
            print(f"An error occurred: {e}")
