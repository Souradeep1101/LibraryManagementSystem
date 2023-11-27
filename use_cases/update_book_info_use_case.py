from mysql.connector import Error


class UpdateBookInfoUseCase:
    """
    Use case for updating existing book information in the library system.

    Attributes:
        book_repository (BookRepository): Repository for book-related operations.
    """

    def __init__(self, book_repository):
        self.book_repository = book_repository

    def execute(self, book_id, title, author, isbn, publication_year, genre):
        """
        Executes the update process for book information.

        Parameters:
            book_id (int): The ID of the book to be updated.
            title (str): The updated title of the book.
            author (str): The updated author of the book.
            isbn (str): The updated ISBN.
            publication_year (int): The updated publication year.
            genre (str): The updated genre of the book.
        """
        try:
            self.book_repository.update_book(book_id, title, author, isbn, publication_year, genre)
            print("Book information updated successfully.")
        except Error as e:
            print(f"An error occurred while updating book info: {e}")
