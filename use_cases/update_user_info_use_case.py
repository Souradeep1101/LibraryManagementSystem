from mysql.connector import Error


class UpdateUserInfoUseCase:
    """
    Use case for updating existing user information in the library system.

    Attributes:
        user_repository (UserRepository): Repository for user-related operations.
    """

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user_id, name, email, role):
        """
        Executes the update process for user information.

        Parameters:
            user_id (int): The ID of the user to be updated.
            name (str): The updated name of the user.
            email (str): The updated email address.
            role (str): The updated role of the user.
        """
        try:
            self.user_repository.update_user(user_id, name, email, role)
            print("User information updated successfully.")
        except Error as e:
            print(f"An error occurred while updating user info: {e}")
