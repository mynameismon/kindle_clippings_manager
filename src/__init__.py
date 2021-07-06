
import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtSql import QSqlDatabase

from src.database import DATABASE, DATABASE_NAME, initialise_connection, initialise_database
from src.views import Window


def main():
    """RP Contacts main function."""
    # Create the application
    app = QApplication(sys.argv)
    # Connect to the database before creating any window
    connection = QSqlDatabase.addDatabase(DATABASE)
    connection.setDatabaseName(DATABASE_NAME)
    print(initialise_connection(connection))
    if not initialise_connection(connection):
        print("Oops!")
        connection.close()
        sys.exit(1)
    # Create the main window if the connection succeeded
    initialise_database()
    win = Window()
    win.show()
    # Run the event loop
    print("Starting App...")
    sys.exit(app.exec())