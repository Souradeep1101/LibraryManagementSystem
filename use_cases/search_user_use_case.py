from mysql.connector import Error


class SearchUserUseCase:
    """
    Use case for searching a user from the library.

    Attributes:
        user_repository (UserRepository): Repository for user-related operations.
    """

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, id_field_name, id_value, fetchone):
        """
        Executes the user searching process.

        Parameters:
            id_field_name (str): The column/field name of the id.
            id_value (str or int): The unique identifier of the column/field.
            fetchone (bool): Check if the user needs only one loan.
        """
        try:
            user = self.user_repository.get_users_by_id(id_field_name, id_value, fetchone)
            if not user:
                raise Exception("User not found.")
            else:
                print("User found successfully.")
                return user
        except Error as e:
            print(f"An error occurred: {e}")
            return f"An error occurred: {e}"
