import os
import subprocess
import sys


def install_requirements():
    """
    Installs the required Python packages listed in requirements.txt.

    It uses pip to install all the dependencies.
    """
    print("Installing required Python packages from requirements.txt...")
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
    print("Dependencies installed successfully.")


def create_config_file():
    """
    Creates a config.py file with database configuration details.

    Prompts the user for database connection details and writes them to config.py.
    """
    print("\nSetting up Configuration for Library Management System")

    # Prompting for database connection details
    host = input("Enter database host (e.g., localhost): ")
    username = input("Enter database username: ")
    password = input("Enter database password: ")
    database = input("Enter database name (e.g., LibraryManagementSystem): ")

    # Creating the content for config.py
    config_content = f"""# config.py
DB_CONFIG = {{
    'host': '{host}',
    'username': '{username}',
    'password': '{password}',
    'database': '{database}'
}}
"""

    # Writing the content to config.py
    with open("config.py", "w") as file:
        file.write(config_content)

    print("config.py file has been created successfully.")


def run_database_setup():
    """
    Sets up the database using database_connector.py.

    Changes the working directory to the directory containing database_connector.py,
    executes the script to create the database and tables, then returns to the root directory.
    """
    print("\nSetting up the Database...")
    os.chdir("frameworks_and_drivers/database")
    subprocess.run([sys.executable, "database_connector.py"], check=True)
    os.chdir("../../")


def main():
    """
    Main function to execute the setup process.

    Orchestrates the creation of the configuration file, installation of Python packages,
    and the setup of the database by calling the respective functions.
    """
    install_requirements()
    create_config_file()
    run_database_setup()


if __name__ == "__main__":
    main()
