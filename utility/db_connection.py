from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


CURRENT_PATH = os.path.join(os.getcwd(), "db")
DB_PATH = os.path.join(CURRENT_PATH, "movies.db")


def get_session():
    engine = create_engine('sqlite:///{}'.format(DB_PATH))
    session = sessionmaker(bind=engine)
    # create a Session
    session = session()
    return session
