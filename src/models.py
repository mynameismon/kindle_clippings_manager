# -*- coding: utf-8 -*-

"""This module provides a model to manage the contacts table."""

from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlTableModel


class notes_model:
    def __init__(self):
        self.model = self._initialise_model()

    @staticmethod
    def _initialise_model():
        """Create and set up the model."""
        clippings_table = QSqlTableModel()
        clippings_table.setTable("clippings")
        clippings_table.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        clippings_table.select()
        headers = ("Id", "Book", "Author", "Type", "Clipping")
        for columnIndex, header in enumerate(headers):
            clippings_table.setHeaderData(columnIndex, Qt.Orientation.Horizontal, header)
        return clippings_table
