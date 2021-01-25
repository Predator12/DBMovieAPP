from sqlalchemy import Column, Integer, DATE, VARCHAR
from sqlalchemy.orm import relationship
from models import Base, ActorMovie, DirectorMovie


class Movie(Base):
    __tablename__ = "movies"
    id = Column("movie_id", Integer, primary_key=True)
    name = Column(VARCHAR)
    title = Column(VARCHAR)
    creation_date = Column(DATE)
    actors = relationship(
        'Actor',
        secondary=ActorMovie,
        backref='Movie'
    )
    directors = relationship(
        'Director',
        secondary=DirectorMovie,
        backref='Movie'
    )

    def __init__(self, name, title, creation_date):
        self.name = name
        self.title = title
        self.creation_date = creation_date

    @staticmethod
    def keys_list():
        return ["Name", "Title", "Creation Date", "Actors", "Directors"]

    def to_dict(self):
        return {
            "name": self.name,
            "title": self.title,
            "creation_date": self.creation_date,
            "actors": self.actors,
            "directors": self.directors
        }
