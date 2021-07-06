from PyQt6 import QtSql
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtSql import QSqlDatabase

INIT_QUERY = ("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    book_title TEXT UNIQUE,
    author TEXT
);""",
"""
CREATE TABLE IF NOT EXISTS clippings (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    book TEXT NOT NULL,
    author TEXT,
    clipping TEXT UNIQUE NOT NULL,
    start_location INTEGER NOT NULL,
    end_location INTEGER NOT NULL,
    date DATE,

    FOREIGN KEY (book) REFERENCES books(book_id)
);
""")

DATABASE = "QSQLITE"
DATABASE_NAME = "database.sqlite3"

def connect(sql_query): 
    connection = QSqlDatabase.addDatabase(DATABASE)
    connection.setDatabaseName(DATABASE_NAME)

    if initialise_connection(connection):
        connection.exec(sql_query)
        connection.commit()
        connection.close()
        return connection
    else:
        raise OSError
         


def initialise_database():
    for query in INIT_QUERY:
        print(connect(query))


def initialise_connection(connection):
    if not connection.open():
        QMessageBox.warning(
            None,
            "Database Error",
            f"Database Error: {connection.lastError().text()}",
        )
        connection.close()
        return False
    else:
        return True