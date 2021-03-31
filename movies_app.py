import sys
import cowsay
from PyQt5 import QtWidgets
from view import MainWindowInit


class MovieApp(MainWindowInit):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addSignal()


def main():
    cowsay.ghostbusters("Movies App Started")
    app = QtWidgets.QApplication(sys.argv)
    window = MovieApp()
    window.show()
    app.exec_()
    cowsay.kitty("Movies App Closed. Bye")


if __name__ == '__main__':
    main()
