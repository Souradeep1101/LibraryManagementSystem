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

    def get_users_by_id(self, id_field_name, id_value, fetchone=True):
        """
        Retrieves user record(s) from the database by its ID.

        Parameters:
            id_field_name (str): The column/field name of the id.
            id_value (str or int): The unique identifier of the column/field.
            fetchone (bool): Check if the user needs only one user.

        Returns:
            User record(s) from the database.
        """
        query = f"SELECT * FROM users WHERE {id_field_name} = %s"
        args = (id_value,)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            headers = [i[0] for i in cursor.description]
            if fetchone:
                user = cursor.fetchone()
            else:
                user = cursor.fetchall()
            return {'content': user, 'headers': headers}
        except Error as e:
            print(f"Error: '{e}'")

    def get_users(self, fetchone=True):
        """
        Retrieves all user record(s) from the database.

        Parameters:
            fetchone (bool): Check if the user needs only one user.

        Returns:
            User record(s) with their headers from the database.
        """
        query = f"SELECT * FROM users"

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            headers = [i[0] for i in cursor.description]
            if fetchone:
                users = cursor.fetchone()
            else:
                users = cursor.fetchall()
            return {'content': users, 'headers': headers}
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
