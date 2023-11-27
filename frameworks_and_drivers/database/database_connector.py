import mysql.connector
from mysql.connector import Error
import config


def create_db_connection():
    """Creates and returns a connection to the specified database."""
    dbinfo = config.DB_CONFIG  # Accessing configuration
    try:
        conn = mysql.connector.connect(
            host=dbinfo['host'],
            user=dbinfo['username'],
            passwd=dbinfo['password'],
            database=dbinfo['database'],
        )
        return conn
    except Error as err:
        print(f"Error: '{err}'")
        return None


def create_server_connection():
    """Creates a connection to the MySQL server."""
    dbinfo = config.DB_CONFIG  # Accessing configuration
    try:
        conn = mysql.connector.connect(
            host=dbinfo['host'],
            user=dbinfo['username'],
            passwd=dbinfo['password'],
        )
        print("MySQL Server connection successful")
        return conn
    except Error as err:
        print(f"Error: '{err}'")
        return None


def create_database(conn, query):
    """Creates a database."""
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


def use_database(conn, query):
    """Opens a database."""
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        print("Database opened successfully")
    except Error as err:
        print(f"Error: '{err}'")


def create_table(conn, query):
    """Creates a table in the database."""
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        print("Table created successfully")
    except Error as err:
        print(f"Error: '{err}'")


# Replace with your MySQL server information
db_info = config.DB_CONFIG
database = db_info['database']  # LibrarySystem

# Establishing a server connection
connection = create_server_connection()

# SQL query to create a database
create_database_query = f"CREATE DATABASE IF NOT EXISTS {database}"
create_database(connection, create_database_query)
use_database_query = f"USE {database}"
use_database(connection, use_database_query)

# SQL queries to create tables
create_books_table_query = """
CREATE TABLE IF NOT EXISTS books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    isbn VARCHAR(13),
    publication_year INT,
    genre VARCHAR(100)
);
"""

create_users_table_query = """
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    role VARCHAR(50) NOT NULL
);
"""

create_loans_table_query = """
CREATE TABLE IF NOT EXISTS loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    user_id INT,
    loan_date DATETIME,
    due_date DATETIME,
    return_date DATETIME NULL,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
"""

# Creating tables
create_table(connection, create_books_table_query)
create_table(connection, create_users_table_query)
create_table(connection, create_loans_table_query)
