from mysql.connector import Error


class DeleteUserUseCase:
    """
    Use case for deleting a user from the library system.

    Attributes:
        user_repository (UserRepository): Repository for user-related operations.
    """

    def __init__(self, user_repository, loan_repository):
        self.loan_repository = loan_repository
        self.user_repository = user_repository

    def can_delete_user(self, user_id):
        # Check if there are any loans associated with the user
        loans = self.loan_repository.get_loans_by_id('user_id', user_id, fetchone=False)
        return len(loans) == 0

    def execute(self, user_id):
        """
        Executes the process of deleting a user from the library.

        Parameters:
            user_id (int): The unique identifier of the user to be deleted.
        """
        try:
            if self.can_delete_user(user_id):
                self.user_repository.delete_user(user_id)
                print("User deleted successfully.")
                return "User deleted successfully."
            else:
                print("Cannot delete user: There are active loans associated with this user.")
                return "Cannot delete user: There are active loans associated with this user."
        except Error as e:
            print(f"An error occurred while deleting the user: {e}")
            return f"An error occurred while deleting the user: {e}"
