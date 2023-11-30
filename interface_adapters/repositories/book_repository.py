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

    def get_books_by_id(self, id_field_name, id_value, fetchone=True):
        """
        Retrieves book record(s) from the database by its ID.

        Parameters:
            id_field_name (str): The column/field name of the id.
            id_value (str or int): The unique identifier of the column/field.
            fetchone (bool): Check if the user needs only one book.

        Returns:
            Book record(s) from the database.
        """
        query = f"SELECT * FROM books WHERE {id_field_name} = %s"
        args = (id_value,)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            headers = [i[0] for i in cursor.description]
            if fetchone:
                book = cursor.fetchone()
            else:
                book = cursor.fetchall()
            return {'content': book, 'headers': headers}
        except Error as e:
            print(f"Error: '{e}'")

    def get_books(self, fetchone=True):
        """
        Retrieves all book record(s) from the database.

        Parameters:
            fetchone (bool): Check if the user needs only one book.

        Returns:
            Book record(s) with their headers from the database.
        """
        query = f"SELECT * FROM books"

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            headers = [i[0] for i in cursor.description]
            if fetchone:
                books = cursor.fetchone()
            else:
                books = cursor.fetchall()
            return {'content': books, 'headers': headers}
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
