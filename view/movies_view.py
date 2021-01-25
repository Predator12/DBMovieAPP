from view import ActorsTableWindow, DirectorsTableWindow
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem,\
    QPushButton, qApp, QHeaderView
from controllers import MovieController


class MoviesTableWidget(QTableWidget):
    def __init__(self, centralwidget):
        super().__init__(centralwidget)
        self.w = None
        self.movies = []
        self.movie_keys = []

    def load_content_from_db(self, movies=None):
        if movies:
            self.movies = movies
        self.movie_keys = MovieController.get_keys()
        self.movie_keys.append("Rate")
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.setColumnCount(len(self.movie_keys))
        self.setRowCount(len(self.movies))
        self.setHorizontalHeaderLabels(self.movie_keys)
        header = self.horizontalHeader()

        for row_index, movie in enumerate(self.movies):
            dict_movie = movie.to_dict()
            for col_index, item in enumerate(dict_movie):
                header.setSectionResizeMode(col_index, QHeaderView.Stretch)
                if item == "actors":
                    btn_actor = QPushButton('Actors')
                    self.setCellWidget(row_index, col_index, btn_actor)
                    btn_actor.clicked.connect(self.show_actors_window)
                elif item == "directors":
                    btn_directors = QPushButton('Directors')
                    self.setCellWidget(row_index, col_index, btn_directors)
                    btn_directors.clicked.connect(self.show_directors_window)
                else:
                    self.setItem(
                        row_index,
                        col_index,
                        QTableWidgetItem(str(dict_movie[item]))
                    )
            self.setItem(row_index, 5, QTableWidgetItem(str("")))

    def show_actors_window(self):
        button = qApp.focusWidget()
        index = self.indexAt(button.pos())
        actors = self.movies[index.row()].actors
        self.w = ActorsTableWindow(actors)
        self.w.show()

    def show_directors_window(self):
        button = qApp.focusWidget()
        index = self.indexAt(button.pos())
        directors = self.movies[index.row()].directors
        self.w = DirectorsTableWindow(directors)
        self.w.show()
