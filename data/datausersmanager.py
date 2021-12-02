import sqlite3
from data.abstract_datamanager import AbstractDataManager
from data.datafriendmanager import DataFriendsManager


class DataUsersManager(AbstractDataManager):
    def __init__(self):
        self._connect = sqlite3.connect(r'data/users_data.db')
        self._cursor = self._connect.cursor()
        self._cursor.execute("CREATE TABLE IF NOT EXISTS users (user_login text, user_password text)")

    def add_one(self, user_login, user_password):
        self._cursor.execute(f"INSERT INTO users VALUES ('{user_login}', '{user_password}')")

        friend_manager = DataFriendsManager()
        friend_manager.add_one(user_login)

        self._connect.commit()



    def delete_one(self, user_login):
        self._cursor.execute(f"DELETE FROM users WHERE user_login='{user_login}'")
        self._connect.commit()

    def get_all(self):
        return [user for user in self._cursor.execute(f"SELECT * FROM users")]

    def get_one(self, user_login):
        return list(self._cursor.execute(f"SELECT * FROM users WHERE user_login='{user_login}'")) != []

    def user_in_base(self,user_login):
        if self._cursor.execute(f"SELECT user_login FROM users WHERE user_login='{user_login}'") != None:
            return True
        else:
            return False

    def is_right_password(self, user_login, user_password):
        return list(self._cursor.execute(f"SELECT * FROM users WHERE user_login='{user_login}' AND user_password='{user_password}'")) != []


USERS_DATA = DataUsersManager()

if __name__ == '__main__':
    datamanager = DataUsersManager()
    # datamanager.add_user('Gena', '123')
    # print (datamanager.is_right_password('Gena', '123'))
    print (datamanager.get_one('Genaa'))
    print (datamanager.get_all())

