from mysql.connector import Error


class DeleteUserUseCase:
    """
    Use case for deleting a user from the library system.

    Attributes:
        user_repository (UserRepository): Repository for user-related operations.
    """

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user_id):
        """
        Executes the process of deleting a user from the library.

        Parameters:
            user_id (int): The unique identifier of the user to be deleted.
        """
        try:
            self.user_repository.delete_user(user_id)
            print("User deleted successfully.")
        except Error as e:
            print(f"An error occurred while deleting the user: {e}")
