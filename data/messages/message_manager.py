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

    def get_all(self):
        postman = MessageData(self.user_in)
        mine = postman.get_all_mine(self.user_out)
        yours = postman.get_all_yours(self.user_out)
        all_messages = mine + yours
        for message in all_messages:
            print (f'{message[1]}: {message[0]}   - to {message[2]}')

if __name__ == '__main__':
    manager = MessageManager('клаус', 'dominick')
