from PyQt5.QtWidgets import QGridLayout, QWidget, \
    QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize
from controllers import DirectorController


class DirectorsTableWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, directors):
        super().__init__()
        layout = QGridLayout()
        self.directors = directors
        self.setMinimumSize(QSize(580, 280))
        self.setWindowTitle("Directors")
        self.setLayout(layout)
        table = QTableWidget(self)
        self.director_keys = DirectorController().get_keys()
        table.setColumnCount(len(self.director_keys))
        table.setRowCount(len(self.directors))
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        table.setHorizontalHeaderLabels(self.director_keys)

        for index, director in enumerate(self.directors):
            table.setItem(index, 0, QTableWidgetItem(director.first_name))
            table.setItem(index, 1, QTableWidgetItem(director.last_name))
            table.setItem(index, 2, QTableWidgetItem(str(director.birthday)))
            table.setItem(index, 3, QTableWidgetItem(director.nationality))

        table.resizeColumnsToContents()
        #
        layout.addWidget(table, 0, 0)
