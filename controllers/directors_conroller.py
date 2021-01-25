from models import Director


class DirectorController:

    def __init__(self, session=None):
        self.__session = session

    def get_all(self):
        return self.__session.query(Director).all()

    @staticmethod
    def get_keys():
        return Director.keys_list()
