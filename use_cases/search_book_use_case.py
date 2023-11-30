from mysql.connector import Error


class SearchBookUseCase:
    """
    Use case for searching a book from the library.

    Attributes:
        book_repository (BookRepository): Repository for book-related operations.
    """

    def __init__(self, book_repository):
        self.book_repository = book_repository

    def execute(self, id_field_name, id_value, fetchone=True):
        """
        Executes the book searching process.

        Parameters:
            id_field_name (str): The column/field name of the id.
            id_value (str or int): The unique identifier of the column/field.
            fetchone (bool): Check if the user needs only one book.
        """
        try:
            book = self.book_repository.get_books_by_id(id_field_name, id_value, fetchone)
            if not book:
                raise Exception("Book not found.")
            else:
                print("Book found successfully.")
                return book
        except Error as e:
            print(f"An error occurred: {e}")
            return f"An error occurred: {e}"
