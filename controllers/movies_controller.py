from models import Movie
from sqlalchemy import asc, desc


class MovieController:

    def __init__(self, session=None):
        self.session = session

    def get_all(self, limit_count):
        return self.session.query(Movie).offset(limit_count).all()

    def get_by_limit(self, limit, count):
        return self.session.query(Movie).offset(limit).limit(count).all()

    def get_by_order(self, column_name, limit, order):
        column_name = column_name.lower().replace(" ", "_")
        if order == "desc":
            data = self.session.query(Movie).order_by(desc(column_name))
        else:
            data = self.session.query(Movie).order_by(asc(column_name))

        return data.limit(limit).all()

    def get_by_search(self, search_text, column_name):
        if column_name == "Name":
            movie_model_column = Movie.name
        elif column_name == "Title":
            movie_model_column = Movie.title
        else:
            movie_model_column = Movie.creation_date

        movie_data = self.session.query(Movie).filter(
            movie_model_column.contains(search_text)
        )
        return movie_data.all()

    @staticmethod
    def get_keys():
        return Movie.keys_list()
