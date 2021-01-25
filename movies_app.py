import sys
from PyQt5 import QtWidgets
from view import MainWindowInit


class MovieApp(MainWindowInit):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addSignal()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MovieApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
