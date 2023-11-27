from mysql.connector import Error


class UserRegistrationUseCase:
    """
    Use case for registering a new user in the library system.

    Attributes:
        user_repository (UserRepository): Repository for user-related operations.
    """

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, name, email, role):
        """
        Executes the user registration process.

        Parameters:
            name (str): The name of the user.
            email (str): The email address of the user.
            role (str): The role of the user (e.g., 'student', 'teacher', 'admin').
        """
        try:
            self.user_repository.add_user(name, email, role)
            print("User registered successfully.")
        except Error as e:
            print(f"An error occurred during registration: {e}")
