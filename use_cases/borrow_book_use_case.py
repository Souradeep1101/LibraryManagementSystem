from mysql.connector import Error


class BorrowBookUseCase:
    """
    Use case for borrowing a book from the library.

    Attributes:
        book_repository (BookRepository): Repository for book-related operations.
        loan_repository (LoanRepository): Repository for loan-related operations.
    """

    def __init__(self, book_repository, loan_repository):
        self.book_repository = book_repository
        self.loan_repository = loan_repository

    def execute(self, book_id, user_id, loan_date, due_date):
        """
        Executes the book borrowing process.

        Parameters:
            book_id (int): The ID of the book to be borrowed.
            user_id (int): The ID of the user borrowing the book.
            loan_date (datetime): The date when the book is borrowed.
            due_date (datetime): The due date for returning the book.
        """
        try:
            book = self.book_repository.get_book_by_id(book_id)
            if not book:
                raise Exception("Book not found.")

            self.loan_repository.create_loan(book_id, user_id, loan_date, due_date)
            print("Book borrowed successfully.")
        except Error as e:
            print(f"An error occurred: {e}")
