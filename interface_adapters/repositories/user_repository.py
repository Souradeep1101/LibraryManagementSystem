from mysql.connector import Error


class UserRepository:
    """
    Repository class for handling the database operations related to users.
    """

    def __init__(self, connection):
        """
        Initializes the UserRepository with a database connection.

        Parameters:
            connection: A MySQL database connection object.
        """
        self.connection = connection

    def add_user(self, name, email, role):
        """
        Adds a new user to the database.

        Parameters:
            name (str): The name of the user.
            email (str): The email address of the user.
            role (str): The role of the user (e.g., 'student', 'teacher', 'admin').
        """
        query = """
                INSERT INTO users (name, email, role) 
                VALUES (%s, %s, %s)
                """
        args = (name, email, role)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            self.connection.commit()
            print("User added successfully")
        except Error as e:
            print(f"Error: '{e}'")
            self.connection.rollback()

    def get_user_by_id(self, user_id):
        """
        Retrieves a user from the database by their ID.

        Parameters:
            user_id (int): The unique identifier of the user.

        Returns:
            A user record from the database.
        """
        query = "SELECT * FROM users WHERE user_id = %s"
        args = (user_id,)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            user = cursor.fetchone()
            return user
        except Error as e:
            print(f"Error: '{e}'")

    def update_user(self, user_id, name, email, role):
        """
        Updates the details of an existing user in the database.

        Parameters:
            user_id (int): The unique identifier of the user to be updated.
            name (str): The new name of the user.
            email (str): The new email address.
            role (str): The new role of the user.
        """
        query = """
                UPDATE users 
                SET name = %s, email = %s, role = %s 
                WHERE user_id = %s
                """
        args = (name, email, role, user_id)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            self.connection.commit()
            print("User updated successfully")
        except Error as e:
            print(f"Error: '{e}'")
            self.connection.rollback()

    def delete_user(self, user_id):
        """
        Deletes a user from the database.

        Parameters:
            user_id (int): The unique identifier of the user to be deleted.
        """
        query = "DELETE FROM users WHERE user_id = %s"
        args = (user_id,)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            self.connection.commit()
            print("User deleted successfully")
        except Error as e:
            print(f"Error: '{e}'")
            self.connection.rollback()

    # Additional methods can be added here as needed.
