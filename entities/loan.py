from datetime import datetime


class Loan:
    """
    Represents a loan of a book in the library system, including its status and due dates.

    Attributes:
        loan_id (int): A unique identifier for the loan.
        book_id (int): The unique identifier of the book being loaned.
        user_id (int): The unique identifier of the user who has borrowed the book.
        loan_date (datetime): The date when the book was loaned out.
        due_date (datetime): The date by which the book should be returned.
        return_date (datetime, optional): The date when the book was actually returned.
    """

    def __init__(self, loan_id, book_id, user_id, loan_date, due_date, return_date=None):
        """
        The constructor for the Loan class.

        Parameters:
            loan_id (int): A unique identifier for the loan.
            book_id (int): The unique identifier of the book being loaned.
            user_id (int): The unique identifier of the user who has borrowed the book.
            loan_date (datetime): The date when the book was loaned out.
            due_date (datetime): The date by which the book should be returned.
            return_date (datetime, optional): The date when the book was actually returned.
        """
        self.loan_id = loan_id
        self.book_id = book_id
        self.user_id = user_id
        self.loan_date = loan_date
        self.due_date = due_date
        self.return_date = return_date

    def is_overdue(self):
        """
        Determines whether the book loan is overdue.

        Returns:
            bool: True if the book is overdue and not yet returned, False otherwise.
        """
        return datetime.now() > self.due_date if self.return_date is None else False

    def __str__(self):
        """
        Returns a human-readable string representation of the Loan instance.

        Returns:
            str: A string describing the loan.
        """
        return f"Loan ID: {self.loan_id}, Book ID: {self.book_id}, User ID: {self.user_id}"
