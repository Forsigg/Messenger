from data.users_data import AbstractDataManager
import sqlite3
from pathlib import Path

#import datausersmanager


class DataFriendsManager(AbstractDataManager):
    def __init__(self, user_login):
        self.user = user_login.lower()
        self.add_user(self.user)

    def connect(self):
        # функция для установления соединения с БД
        self._connect = sqlite3.connect(Path('data', 'users_data', 'users_data.db'))
        self._cursor = self._connect.cursor()
        self._cursor.execute("CREATE TABLE IF NOT EXISTS friends (user_login TEXT, user_friends BLOB)")

    def add_user(self, user_login):
        # добавление пользователя в таблицу, которая хранит пары user_login: user_friends
        self.connect()
        self._cursor.execute(f"INSERT INTO friends (user_login) VALUES ('{user_login}')")
        self._connect.commit()
        self._connect.close()

    def add_one(self, friend_login):
        # добавление друга в список друзей
        self.connect()
        friends = list(self._cursor.execute(f"SELECT * FROM friends WHERE user_login='{self.user}'"))[0][1]

        if friends == [None]:
            friends = friend_login + ','
        elif friends.find(friend_login) != -1:
            self._connect.close()
            return print(f'Пользователь {friend_login} уже находится в списке ваших друзей.')
        else:
            friends.append(str(friend_login + ','))
            friends = ''.join(friends)

        self._cursor.execute(f"UPDATE friends SET user_friends='{friends}' WHERE user_login='{self.user}'")
        self._connect.commit()
        print(f'Пользователь {friend_login} успешно добавлен в список друзей.')
        self._connect.close()

    def delete_one(self, friend_login):
        # удаление из списка друзей
        self.connect()
        friends = list(self._cursor.execute(f"SELECT * FROM friends WHERE user_login='{self.user}'"))[0][1]

        if friends == [None]:
            self._connect.close()
            return print('У вас нет друзей для удаления :(')
        elif friends.find(friend_login) == -1:
            self._connect.close()
            return print (f'Пользователя {friend_login} нет в списке ваших друзей.')
        else:
            friends = friends.replace(friend_login + ',', '')

        self._cursor.execute(f"UPDATE friends SET user_friends='{friends}' WHERE user_login='{self.user}'")
        self._connect.commit()
        print (f'Пользователь {friend_login} успешно удален из списка друзей.')
        self._connect.close()


    def get_one(self, friend_login):
        # получение сведений о друге
        user_manager = datausersmanager.DataUsersManager()
        return user_manager.get_one(friend_login)


    def get_all(self):
        # получение списка всех друзей
        self.connect()

        friends = list(self._cursor.execute(f"SELECT * FROM friends WHERE user_login='{self.user}'"))[0][1]
        friends = friends.split(',')
        print ('Список ваших друзей:')
        for friend in friends:
            print (friend)

        self._connect.close()



if __name__ == '__main__':
    manager = DataFriendsManager('клаус')
    manager.add_one('dominick')
    manager.add_one('шлёпа')
    manager.get_one('клаус')