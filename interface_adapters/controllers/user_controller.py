class UserController:
    """
    Controller for handling user-related requests.
    """

    def __init__(self, user_registration_use_case, update_user_info_use_case, delete_user_use_case):
        self.delete_user_use_case = delete_user_use_case
        self.user_registration_use_case = user_registration_use_case
        self.update_user_info_use_case = update_user_info_use_case

    def register_user(self, name, email, role):
        try:
            self.user_registration_use_case.execute(name, email, role)
            return "User registered successfully."
        except Exception as e:
            return str(e)

    def update_user_info(self, user_id, name, email, role):
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
