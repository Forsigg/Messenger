from data.abstract_datamanager import AbstractDataManager
import sqlite3
from pathlib import Path


class DataFriendsManager(AbstractDataManager):
    def __init__(self):
        self._connect = sqlite3.connect(Path('users_data.db'))
        self._cursor = self._connect.cursor()
        self._cursor.execute("CREATE TABLE IF NOT EXISTS friends (user_login TEXT, user_friends BLOB)")

    def add_user(self, user_login):
        self._cursor.execute(f"INSERT INTO friends (user_login) VALUES ('{user_login}')")
        self._connect.commit()

    def add_one(self, user_login, friend_login):
        friends = list(self._cursor.execute(f"SELECT * FROM friends WHERE user_login='{user_login}'"))
        friends = [friends[0][1]]

        if friends == [None]:
            friends = friend_login + ','
        else:
            friends.append(str(friend_login + ','))
            friends = ' '.join(friends)

        self._cursor.execute(f"UPDATE friends SET user_friends='{friends}' WHERE user_login='{user_login}'")
        self._connect.commit()

    def delete_one(self, data):
        pass

    @property
    def get_one(self, data):
        pass

    @property
    def get_all(self):
        pass


if __name__ == '__main__':
    manager = DataFriendsManager()
    # manager.add_user('клаус')
    manager.add_one(user_login='клаус', friend_login='лялька')
