from sqlalchemy import Column, Integer, DATE, VARCHAR
from sqlalchemy.orm import relationship
from models import Base, DirectorMovie


class Director(Base):
    __tablename__ = "directors"
    id = Column("director_id", Integer, primary_key=True)
    first_name = Column(VARCHAR)
    last_name = Column(VARCHAR)
    birthday = Column(DATE)
    nationality = Column(VARCHAR)
    directors = relationship(
        'Movie',
        secondary=DirectorMovie,
        backref='Director'
    )

    def __init__(self, first_name, last_name, birthday, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.nationality = nationality

    @staticmethod
    def keys_list():
        return ["First Name", "Last Name", "Birthday", "Nationality"]
