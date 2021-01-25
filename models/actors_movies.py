from sqlalchemy import Column, Integer, ForeignKey, Table
from models import Base

ActorMovie = Table(
    'actors_movies',
    Base.metadata,
    Column('actor_id', Integer, ForeignKey('actors.actor_id')),
    Column('movie_id', Integer, ForeignKey('movies.movie_id'))
)
