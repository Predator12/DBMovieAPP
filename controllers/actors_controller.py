from models import Actor


class ActorController:

    def __init__(self, session=None):
        self.__session = session

    def get_all(self):
        return self.__session.query(Actor).all()

    @staticmethod
    def get_keys():
        return Actor.keys_list()
