import sqlite3
from data.users_data.abstract_datamanager import AbstractDataManager
from data.users_data.datafriendmanager import DataFriendsManager
from pathlib import Path


class DataUsersManager(AbstractDataManager):
    def connect(self):
        self._connect = sqlite3.connect(Path('users_data.db'))
        self._cursor = self._connect.cursor()
        self._cursor.execute("CREATE TABLE IF NOT EXISTS users (user_login text, user_password text)")

    def add_one(self, user_login, user_password):
        self.connect()
        self._cursor.execute(f"INSERT INTO users VALUES ('{user_login}', '{user_password}')")

        friend_manager = DataFriendsManager(user_login)
        friend_manager.add_one(user_login)

        self._connect.commit()
        self._connect.close()

    def delete_one(self, user_login):
        self.connect()
        self._cursor.execute(f"DELETE FROM users WHERE user_login='{user_login}'")
        self._connect.commit()
        self._connect.close()

    def get_all(self):
        self.connect()
        users = [user for user in self._cursor.execute(f"SELECT * FROM users")]
        for user in users: print (user)
        self._connect.close()


    def get_one(self, user_login):
        self.connect()
        user = (list(self._cursor.execute(f"SELECT * FROM users WHERE user_login='{user_login}'")))
        if user == []:
            return print (f'Пользователя {user_login} не существует.')
        else:
            print (user[0][0])
        self._connect.close()

    def user_in_base(self,user_login):
        self.connect()
        if self._cursor.execute(f"SELECT user_login FROM users WHERE user_login='{user_login}'") != None:
            self._connect.close()
            return True
        else:
            self._connect.close()
            return False

    def is_right_password(self, user_login, user_password):
        self.connect()
        print (list(self._cursor.execute(
            f"SELECT * FROM users WHERE user_login='{user_login}' AND user_password='{user_password}'")) != [])
        self._connect.close()


if __name__ == '__main__':
    USERS_DATA = DataUsersManager()
    datamanager = DataUsersManager()
    # datamanager.add_user('Gena', '123')
    # print (datamanager.is_right_password('Gena', '123'))
    print (datamanager.get_one('Genaa'))
    print (datamanager.get_all())

