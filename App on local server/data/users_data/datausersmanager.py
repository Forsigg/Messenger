import sqlite3
from data.users_data import AbstractDataManager
from pathlib import Path



class DataUsersManager(AbstractDataManager):
    def connect(self):
        self._connect = sqlite3.connect(Path(__file__).parent.joinpath('users_data.db'))
        self._cursor = self._connect.cursor()
        self._cursor.execute("CREATE TABLE IF NOT EXISTS users (user_login, user_password)")

    def add_one(self, user_login, user_password):
        self.connect()
        self._cursor.execute(f"INSERT INTO users VALUES ('{user_login}', '{user_password}')")
        self._connect.commit()
        self._connect.close()


    def delete_one(self, user_login):
        self.connect()
        self._cursor.execute(f"DELETE FROM users WHERE user_login='{user_login}';")
        self._connect.commit()
        self._connect.close()


    def get_all(self, *args):
        self.connect()
        users = [user for user in self._cursor.execute(f"SELECT * FROM users;")]
        self._connect.close()
        return users


    def get_one(self, user_login):
        self.connect()
        user = list(self._cursor.execute(f"SELECT * FROM users WHERE user_login='{user_login}'"))
        if user == []:
            self._connect.close()
            return False
        else:
            self._connect.close()
            return user



    def user_in_base(self,user_login):
        self.connect()
        user = list(self._cursor.execute(f"SELECT * FROM users WHERE user_login='{user_login}'"))
        if user == []:
            self._connect.close()
            return False
        else:
            self._connect.close()
            return True



    def is_right_password(self, user_login, user_password):
        self.connect()
        a = self._cursor.execute(f"SELECT * FROM users WHERE user_login='{user_login}' AND user_password='{user_password}'")
        if list(a) == []:
            self._connect.close()
            return False
        else:
            self._connect.close()
            return True
