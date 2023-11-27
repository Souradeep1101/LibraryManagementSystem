from mysql.connector import Error


class BookRepository:
    """
    Repository class for handling the database operations related to books.
    """

    def __init__(self, connection):
        """
        Initializes the BookRepository with a database connection.

        Parameters:
            connection: A MySQL database connection object.
        """
        self.connection = connection

    def add_book(self, title, author, isbn, publication_year, genre):
        """
        Adds a new book to the database.

        Parameters:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            publication_year (int): The year of publication.
            genre (str): The genre of the book.
        """
        query = """
                INSERT INTO books (title, author, isbn, publication_year, genre) 
                VALUES (%s, %s, %s, %s, %s)
                """
        args = (title, author, isbn, publication_year, genre)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            self.connection.commit()
            print("Book added successfully")
        except Error as e:
            print(f"Error: '{e}'")
            self.connection.rollback()

    def get_book_by_id(self, book_id):
        """
        Retrieves a book from the database by its ID.

        Parameters:
            book_id (int): The unique identifier of the book.

        Returns:
            A book record from the database.
        """
        query = "SELECT * FROM books WHERE book_id = %s"
        args = (book_id,)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            book = cursor.fetchone()
            return book
        except Error as e:
            print(f"Error: '{e}'")

    def update_book(self, book_id, title, author, isbn, publication_year, genre):
        """
        Updates the details of an existing book in the database.

        Parameters:
            book_id (int): The unique identifier of the book to be updated.
            title (str): The new title of the book.
            author (str): The new author of the book.
            isbn (str): The new ISBN.
            publication_year (int): The new year of publication.
            genre (str): The new genre of the book.
        """
        query = """
                UPDATE books 
                SET title = %s, author = %s, isbn = %s, publication_year = %s, genre = %s 
                WHERE book_id = %s
                """
        args = (title, author, isbn, publication_year, genre, book_id)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            self.connection.commit()
            print("Book updated successfully")
        except Error as e:
            print(f"Error: '{e}'")
            self.connection.rollback()

    def delete_book(self, book_id):
        """
        Deletes a book from the database.

        Parameters:
            book_id (int): The unique identifier of the book to be deleted.
        """
        query = "DELETE FROM books WHERE book_id = %s"
        args = (book_id,)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            self.connection.commit()
            print("Book deleted successfully")
        except Error as e:
            print(f"Error: '{e}'")
            self.connection.rollback()

    # Additional methods can be added here as needed.
