from sqlalchemy import Column, Integer, ForeignKey, Table
from models import Base

DirectorMovie = Table(
    'directors_movies',
    Base.metadata,
    Column('director_id', Integer, ForeignKey('directors.director_id')),
    Column('movie_id', Integer, ForeignKey('movies.movie_id'))
)
