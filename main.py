import sys
import os
import ui.cli.cli_main as cli


def main():
    """
    Main entry point for the Library Management System.

    Presents the user with a choice between a Command-Line Interface (CLI) and
    a Graphical User Interface (GUI), and launches the selected interface.
    """
    print("Welcome to the Library Management System")
    print("Choose the interface you would like to use:")
    print("1. Command-Line Interface (CLI)")
    print("2. Graphical User Interface (GUI)")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        # Launch the CLI
        cli.main()
    elif choice == "2":
        # Launch the GUI using Streamlit
        gui_path = "ui/gui/streamlit_main.py"
        os.system(f"streamlit run {gui_path}")
    else:
        # Handle invalid choice
        print("Invalid choice. Exiting the application.")
        sys.exit(1)


if __name__ == "__main__":
    # If this script is run as the main program, execute the main function.
    main()
