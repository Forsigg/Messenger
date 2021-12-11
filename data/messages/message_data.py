from data.messages import Message
from data.users_data.abstract_datamanager import AbstractDataManager
import sqlite3
from pathlib import Path

class MessageData(AbstractDataManager):
    def __init__(self, user_login):
        self.user = user_login

    def connect(self):
        self._connection = sqlite3.connect(Path(__file__).parent.joinpath('user_messages.db'))
        self._cursor = self._connection.cursor()
        self._cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.user}_messages (text TEXT, author TEXT, receiver TEXT, date TEXT)")

    def add_one(self, message: Message):
        self.connect()
        self._cursor.execute(
            f"INSERT INTO {self.user}_messages (text, author, receiver, date) VALUES ('{message.text}', '{message.author}', '{message.receiver}', '{message.date}')"
        )
        self._connection.commit()
        self._connection.close()


    def delete_one(self, message: Message):
        self.connect()
        self._cursor.execute(
            f"DELETE FROM {self.user}_messages WHERE text='{message.text}', author='{message.author}', receiver='{message.receiver}', date='{message.date}'"
        )
        self._connection.commit()
        self._connection.close()


    def get_one(self, message):
        self.connect()
        current_message = self._cursor.execute(
            f"SELECT * FROM {self.user}_messages WHERE text='{message.text}' AND author='{message.author}'AND receiver='{message.receiver}' AND date='{message.date}'"
        )

        print (message)

        self._connection.close()


    def get_all_mine(self, receiver):
        self.connect()
        messages = list(self._cursor.execute(f"SELECT * FROM {self.user}_messages WHERE receiver='{receiver}'"))
        self._connection.close()
        return messages

    def get_all_yours(self, friend):
        self.connect()
        messages = list(self._cursor.execute(f"SELECT * FROM {self.user}_messages WHERE author='{friend}'"))
        self._connection.close()
        return messages

if __name__ == '__main__':
    db = MessageData('клаус')
    print (db.get_all_mine('jora'))
    print (db.get_all_yours('jora'))
