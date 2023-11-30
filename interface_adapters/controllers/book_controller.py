class BookController:
    """
    Controller for handling book-related requests.
    """

    def __init__(self, add_book_use_case, update_book_info_use_case, delete_book_use_case, search_book_use_case,
                 show_database_tables_use_case):
        self.delete_book_use_case = delete_book_use_case
        self.add_book_use_case = add_book_use_case
        self.update_book_info_use_case = update_book_info_use_case
        self.search_book_use_case = search_book_use_case
        self.show_database_tables_use_case = show_database_tables_use_case

    def add_book(self, title, author, isbn, publication_year, genre):
        """
        Adds a new book to the library.

        Parameters:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            publication_year (int): The year of publication.
            genre (str): The genre of the book.
        """
        try:
            self.add_book_use_case.execute(title, author, isbn, publication_year, genre)
            return "Book added successfully."
        except Exception as e:
            return str(e)

    def update_book_info(self, book_id, title, author, isbn, publication_year, genre):
        """
        Updates the details of an existing book in the library.

        Parameters:
            book_id (int): The unique identifier of the book to be updated.
            title (str): The new title of the book.
            author (str): The new author of the book.
            isbn (str): The new ISBN.
            publication_year (int): The new year of publication.
            genre (str): The new genre of the book.
        """
        try:
            self.update_book_info_use_case.execute(book_id, title, author, isbn, publication_year, genre)
            return "Book information updated successfully."
        except Exception as e:
            return str(e)

    def delete_book(self, book_id):
        """
        Deletes a book from the library.

        Parameters:
            book_id (int): The unique identifier of the book to be deleted.
        """
        try:
            return self.delete_book_use_case.execute(book_id)
        except Exception as e:
            return str(e)

    def search_book(self, id_field_name, id_value, fetchone=True):
        """
        Searches a book from the library.

        Parameters:
            id_field_name (str): The column/field name of the id.
            id_value (str or int): The unique identifier of the column/field.
            fetchone (bool): Check if the user needs only one book.
        """
        try:
            return self.search_book_use_case.execute(id_field_name, id_value, fetchone)
        except Exception as e:
            return str(e)

    def get_books(self, fetchone=True):
        """
        Retrieves all book record(s) from the database.

        Parameters:
            fetchone (bool): Check if the user needs only one book.

        Returns:
            Book record(s) with their headers from the database.
        """
        try:
            return self.show_database_tables_use_case.execute('books', fetchone)
        except Exception as e:
            return str(e)
