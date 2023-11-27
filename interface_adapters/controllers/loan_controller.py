class LoanController:
    """
    Controller for handling loan-related requests.
    """

    def __init__(self, borrow_book_use_case, return_book_use_case):
        self.borrow_book_use_case = borrow_book_use_case
        self.return_book_use_case = return_book_use_case

    def borrow_book(self, book_id, user_id, loan_date, due_date):
        try:
            self.borrow_book_use_case.execute(book_id, user_id, loan_date, due_date)
            return "Book borrowed successfully."
        except Exception as e:
            return str(e)

    def return_book(self, loan_id, return_date):
        try:
            self.return_book_use_case.execute(loan_id, return_date)
            return "Book returned successfully."
        except Exception as e:
            return str(e)
