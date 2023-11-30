class UserController:
    """
    Controller for handling user-related requests.
    """

    def __init__(self, user_registration_use_case, update_user_info_use_case, delete_user_use_case,
                 search_user_use_case, show_databases_use_case):
        self.show_database_tables_use_case = show_databases_use_case
        self.delete_user_use_case = delete_user_use_case
        self.user_registration_use_case = user_registration_use_case
        self.update_user_info_use_case = update_user_info_use_case
        self.search_user_use_case = search_user_use_case

    def register_user(self, name, email, role):
        """
        Registers a new user to the library.

        Parameters:
            name (str): The name of the user.
            email (str): The email address of the user.
            role (str): The role of the user (e.g., 'student', 'teacher', 'admin').
        """
        try:
            self.user_registration_use_case.execute(name, email, role)
            return "User registered successfully."
        except Exception as e:
            return str(e)

    def update_user_info(self, user_id, name, email, role):
        """
        Updates the details of an existing user in the library.

        Parameters:
            user_id (int): The unique identifier of the user to be updated.
            name (str): The new name of the user.
            email (str): The new email address.
            role (str): The new role of the user.
        """
        try:
            self.update_user_info_use_case.execute(user_id, name, email, role)
            return "User information updated successfully."
        except Exception as e:
            return str(e)

    def delete_user(self, user_id):
        """
        Deletes a user from the library system.

        Parameters:
            user_id (int): The unique identifier of the user to be deleted.
        """
        try:
            return self.delete_user_use_case.execute(user_id)
        except Exception as e:
            return str(e)

    def search_user(self, id_field_name, id_value, fetchone=True):
        """
        Searches a user from the library.

        Parameters:
            id_field_name (str): The column/field name of the id.
            id_value (str or int): The unique identifier of the column/field.
            fetchone (bool): Check if the user needs only one user.
        """
        try:
            return self.search_user_use_case.execute(id_field_name, id_value, fetchone)
        except Exception as e:
            return str(e)

    def get_users(self, fetchone=True):
        """
        Retrieves all user record(s) from the database.

        Parameters:
            fetchone (bool): Check if the user needs only one user.

        Returns:
            User record(s) with their headers from the database.
        """
        try:
            return self.show_database_tables_use_case.execute('users', fetchone)
        except Exception as e:
            return str(e)
