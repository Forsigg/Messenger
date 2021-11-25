from data.abstract_datamanager import AbstractDataManager
import sqlite3

class DataFriendsManager(AbstractDataManager):
    def __init__(self):
        # self.__connect = sqlite3.connect('')