from abc import abstractmethod

class AbstractDataManager(object):
    '''
    Класс задает интерфейс для других дата менеджеров
    '''

    @property
    @abstractmethod
    def add_one(self, *args):
        raise NotImplemented

    @abstractmethod
    def delete_one(self, data):
        raise NotImplemented

    @abstractmethod
    def get_one(self, data):
        raise NotImplemented

    @abstractmethod
    def get_all(self):
        raise NotImplemented