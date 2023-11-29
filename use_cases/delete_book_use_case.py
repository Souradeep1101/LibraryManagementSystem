from mysql.connector import Error


class DeleteBookUseCase:
    """
    Use case for deleting a book from the library system.

    Attributes:
        book_repository (BookRepository): Repository for book-related operations.
    """

    def __init__(self, book_repository, loan_repository):
        self.loan_repository = loan_repository
        self.book_repository = book_repository

    def can_delete_book(self, book_id):
        # Check if there are any loans associated with the book
        loans = self.loan_repository.get_loans_by_id('book_id', book_id, fetchone=False)
        return len(loans) == 0

    def execute(self, book_id):
        """
        Executes the process of deleting a book from the library.

        Parameters:
            book_id (int): The unique identifier of the book to be deleted.
        """
        try:
            if self.can_delete_book(book_id):
                self.book_repository.delete_book(book_id)
                print("Book deleted successfully.")
                return "Book deleted successfully."
            else:
                print("Cannot delete book: There are active loans associated with it.")
                return "Cannot delete book: There are active loans associated with it."
        except Error as e:
            print(f"An error occurred while deleting the book: {e}")
            return f"An error occurred while deleting the book: {e}"
