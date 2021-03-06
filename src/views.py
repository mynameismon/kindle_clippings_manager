# -*- coding: utf-8 -*-

"""This module provides views to manage the contacts table."""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
    QFileDialog
)

from src.models import notes_model


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Kindle Notes Manager")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.contactsModel = notes_model()
        self.setupUI()

    def importClippings(self):
        """Imports Clippings."""
        filePicker = QFileDialog(self, "Choose a file to import clippings from", filter = 'Text Files (*.txt)')
        filePicker.setViewMode(filePicker.ViewMode.Detail)
        filePicker.setFileMode(filePicker.FileMode.ExistingFile)
        fileName = filePicker.getOpenFileName(self, 'Choose a file to open', filter = 'Text Files (*.txt)')[0]
        self.contactsModel.importClippings(fileName)
        print(fileName)
        

    def setupUI(self):
        """Setup the main window's GUI."""
        # Create the table view widget
        self.table = QTableView()
        self.table.setModel(self.contactsModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.resizeColumnsToContents()
        
        for column_number in (0, 5, 6, 7):
            self.table.hideColumn(column_number)
        # Create buttons
        self.addButton = QPushButton("Import")
        self.addButton.clicked.connect(self.importClippings)
        self.deleteButton = QPushButton("Delete")
        # self.deleteButton.clicked.connect(self.deleteContact)
        self.clearAllButton = QPushButton("Clear All")
        # self.clearAllButton.clicked.connect(self.clearContacts)
        # Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

