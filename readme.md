# Library Management System

A comprehensive CLI and GUI based Library Management System to facilitate the management of book loans, returns, and user registration within a library. This system uses Python for the backend, MySQL for the database, and Streamlit for the web-based GUI.

## Features

- Add, update, and remove books from the library's catalog.
- Register users and update user information.
- Borrow and return books with due date management.
- View comprehensive tables of books, users, and loans.
- Command-Line Interface (CLI) for traditional use.
- Graphical User Interface (GUI) powered by Streamlit for a more modern approach.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What you need to install the software:

- Python 3.11+
- MySQL
- Streamlit
- Tabulate

### Installation

A step by step guide to get a development environment running:

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   ```
2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ``` 
    
3.  Set up the MySQL database using the scripts provided in `frameworks_and_drivers/database/`.

### Configuration

Create a `config.py` file in the root directory with the following content:

```bash
# config.py
DB_CONFIG = {
    'host': 'your_host',
    'username': 'your_username',
    'password': 'your_password',
    'database': 'LibrarySystem'
}
```

Replace the placeholders with your actual database configuration.

### Running the Application

To run the CLI application:

```bash
python LibraryManagementSystem/ui/gui/cli_main.py
``` 

To run the GUI application with Streamlit:

```bash
streamlit run LibraryManagementSystem/ui/gui/streamlit_main.py
``` 

## Usage

The application provides a menu-driven interface to interact with the library system. Follow the on-screen prompts to perform various operations.

## Contributing

Please read [CONTRIBUTING.md](https://chat.openai.com/c/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/yourusername/library-management-system/tags).

## Authors

-   **Souradeep Banerjee** - _Developer_ - [Souradeep1101](https://github.com/Souradeep1101)

See also the list of [contributors](https://github.com/yourusername/library-management-system/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://chat.openai.com/c/LICENSE.md) file for details.

## Acknowledgments

-   Hat tip to anyone whose code was used
-   Inspiration
-   etc