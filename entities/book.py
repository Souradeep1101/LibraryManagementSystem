class Book:
    """
    Represents a book in the library system.

    Attributes:
        book_id (int): A unique identifier for the book.
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The International Standard Book Number.
        publication_year (int): The year in which the book was published.
        genre (str): The genre of the book.
    """

    def __init__(self, book_id, title, author, isbn, publication_year, genre):
        """
        The constructor for the Book class.

        Parameters:
            book_id (int): The unique identifier for the book.
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The International Standard Book Number.
            publication_year (int): The year in which the book was published.
            genre (str): The genre of the book.
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.genre = genre

    def __str__(self):
        """
        Returns a human-readable string representation of the Book instance.

        Returns:
            str: A string describing the book.
        """
        return f"{self.title} by {self.author}"
