from PyQt5 import QtWidgets, QtCore
from view import main_window
from utility import get_movie_rating


class MainWindowInit(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super(MainWindowInit, self).__init__()
        self.is_get_all = False
        self.constant_limit = 10
        self.len_of_headers = len(self.movies_controller.get_keys())

    def addSignal(self):
        self.pushButton.clicked.connect(self.load_all_data_in_table)
        self.pushButton_8.clicked.connect(self.load_more_date_from_constant)
        self.pushButton_7.clicked.connect(self.load_more_date_from_input)
        self.set_combo_box_items(self.comboBox)
        self.set_combo_box_items(self.comboBox_2)
        self.pushButton_6.clicked.connect(self.load_data_by_order_column)
        self.pushButton_5.clicked.connect(self.load_data_by_search)
        self.checkrate = CheckRate(self.movies)
        self.checkrate.new_signal.connect(self.set_data_rate)
        self.checkrate.start()

    @QtCore.pyqtSlot(int, str)
    def set_data_rate(self, r, text):
        it = QtWidgets.QTableWidgetItem(text)
        self.tableWidget.setItem(r, self.len_of_headers, it)

    def load_all_data_in_table(self):
        self.is_get_all = True
        self.movies = self.movies_controller.get_all()
        self.tableWidget.load_content_from_db(self.movies)
        self.checkrate.terminate()
        self.checkrate.set_movies(self.movies)
        self.checkrate.start()

    def load_more_date_from_constant(self):
        self.limit_count += self.constant_limit
        self.movies = self.movies_controller.get_by_limit(self.limit_count)
        self.tableWidget.load_content_from_db(self.movies)
        self.checkrate.terminate()
        self.checkrate.set_movies(self.movies)
        self.checkrate.start()

    def load_more_date_from_input(self):
        limit_count_from_line = self.lineEdit.text()
        if limit_count_from_line:
            self.limit_count += int(limit_count_from_line)
            self.movies = self.movies_controller.get_by_limit(self.limit_count)
            self.tableWidget.load_content_from_db(self.movies)
            self.checkrate.terminate()
            self.checkrate.set_movies(self.movies)
            self.checkrate.start()

    def load_data_by_order_column(self):
        column_name = self.comboBox_2.currentText()
        order = self.comboBox_3.currentText()
        self.movies = self.movies_controller.get_by_order(
            column_name,
            self.limit_count,
            order
        )
        self.tableWidget.load_content_from_db(self.movies)
        self.checkrate.terminate()
        self.checkrate.set_movies(self.movies)
        self.checkrate.start()

    def load_data_by_search(self):
        column_name = self.comboBox.currentText()
        search_text = self.lineEdit_2.text()
        self.movies = self.movies_controller.get_by_search(
            search_text,
            column_name
        )
        if not self.movies:
            self.label_5.setText(
                "<html><head/><body><p><span style=\" color:#ff0000;\">"
                "No result for search: {} "
                "</span></p></body></html>".format(
                    search_text
                )
            )
        else:
            self.tableWidget.load_content_from_db(self.movies)
            self.checkrate.terminate()
            self.checkrate.set_movies(self.movies)
            self.checkrate.start()

    def set_combo_box_items(self, combo_box):
        headers_list = self.movies_controller.get_keys()
        for index, name in enumerate(headers_list):
            if index >= len(headers_list)-2:
                break
            combo_box.addItem(name)


class CheckRate(QtCore.QThread):
    new_signal = QtCore.pyqtSignal(int, str)

    def __init__(self, movies=[], parent=None):
        QtCore.QThread.__init__(self, parent)
        self.movies = movies

    def run(self):
        list_len = len(self.movies)
        index = 0
        while index < list_len:
            movie = self.movies[index]
            rating = get_movie_rating(movie.name, movie.creation_date)
            self.new_signal.emit(index, rating)
            index += 1

    def set_movies(self, movies):
        self.is_stopped = False
        self.movies = movies
