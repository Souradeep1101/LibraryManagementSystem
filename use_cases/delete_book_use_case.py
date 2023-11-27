from mysql.connector import Error


class DeleteBookUseCase:
    """
    Use case for deleting a book from the library system.

    Attributes:
        book_repository (BookRepository): Repository for book-related operations.
    """

    def __init__(self, book_repository):
        self.book_repository = book_repository

    def execute(self, book_id):
        """
        Executes the process of deleting a book from the library.

        Parameters:
            book_id (int): The unique identifier of the book to be deleted.
        """
        try:
            self.book_repository.delete_book(book_id)
            print("Book deleted successfully.")
        except Error as e:
            print(f"An error occurred while deleting the book: {e}")
