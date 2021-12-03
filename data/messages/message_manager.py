from message import Message
from message_data import MessageData

class MessageManager(object):
    def __init__(self, user_in, user_out):
        self.user_in = user_in
        self.user_out = user_out

    def send_message(self, message: Message):
        postman = MessageData(self.user_in)
        postman.add_one(message)

    def get_message(self, message: Message):
        postman = MessageData(self.user_out)
        postman.add_one(message)

    def show_all(self, user_out):
        postman


if __name__ == '__main__':
    manager = MessageManager('клаус', 'dominick')
    message = Message('hello!', 'клаус', 'dominick')
    manager.send_message(message)