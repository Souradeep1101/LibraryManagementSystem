class BookController:
    """
    Controller for handling book-related requests.
    """

    def __init__(self, add_book_use_case, update_book_info_use_case, delete_book_use_case):
        self.delete_book_use_case = delete_book_use_case
        self.add_book_use_case = add_book_use_case
        self.update_book_info_use_case = update_book_info_use_case

    def add_book(self, title, author, isbn, publication_year, genre):
        try:
            self.add_book_use_case.execute(title, author, isbn, publication_year, genre)
            return "Book added successfully."
        except Exception as e:
            return str(e)

    def update_book_info(self, book_id, title, author, isbn, publication_year, genre):
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
