from mysql.connector import Error


class AddNewBookUseCase:
    """
    Use case for adding a new book to the library system.

    Attributes:
        book_repository (BookRepository): Repository for book-related operations.
    """

    def __init__(self, book_repository):
        self.book_repository = book_repository

    def execute(self, title, author, isbn, publication_year, genre):
        """
        Executes the process of adding a new book to the library.

        Parameters:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            publication_year (int): The year the book was published.
            genre (str): The genre of the book.
        """
        try:
            self.book_repository.add_book(title, author, isbn, publication_year, genre)
            print("New book added successfully.")
        except Error as e:
            print(f"An error occurred while adding the book: {e}")
