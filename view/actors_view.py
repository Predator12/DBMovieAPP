from PyQt5.QtWidgets import QGridLayout, QWidget,\
    QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize

from controllers import ActorController


class ActorsTableWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, actors):
        super().__init__()
        layout = QGridLayout()
        self.actors = actors
        self.setMinimumSize(QSize(580, 280))
        self.setWindowTitle("Actors")
        self.setLayout(layout)
        self.actor_keys = ActorController().get_keys()
        table = QTableWidget(self)
        table.setColumnCount(len(self.actor_keys))
        table.setRowCount(len(self.actors))
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        table.setHorizontalHeaderLabels(self.actor_keys)

        for index, actor in enumerate(self.actors):
            table.setItem(index, 0, QTableWidgetItem(actor.first_name))
            table.setItem(index, 1, QTableWidgetItem(actor.last_name))
            table.setItem(index, 2, QTableWidgetItem(str(actor.birthday)))
            table.setItem(index, 3, QTableWidgetItem(actor.nationality))

        table.resizeColumnsToContents()
        #
        layout.addWidget(table, 0, 0)
