class User:
    """
    Represents a user in the library system, such as a student, teacher, or admin.

    Attributes:
        user_id (int): A unique identifier for the user.
        name (str): The name of the user.
        email (str): The email address of the user.
        role (str): The role of the user (e.g., 'student', 'teacher', 'admin').
    """

    def __init__(self, user_id, name, email, role):
        """
        The constructor for the User class.

        Parameters:
            user_id (int): The unique identifier for the user.
            name (str): The name of the user.
            email (str): The email address of the user.
            role (str): The role of the user (e.g., 'student', 'teacher', 'admin').
        """
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = role

    def __str__(self):
        """
        Returns a human-readable string representation of the User instance.

        Returns:
            str: A string describing the user.
        """
        return f"{self.name} ({self.role})"
