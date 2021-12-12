from data.messages import Message
from data.messages import MessageData

class MessageManager(object):
    def __init__(self, user_in, user_out):
        self.user_in = user_in
        self.user_out = user_out

    def send_message(self, message: Message):
        postman = MessageData(self.user_in)
        postman.add_one(message)
        postman = MessageData(self.user_out)
        postman.add_one(message)

    def get_message(self, message: Message):
        postman = MessageData(self.user_out)
        postman.add_one(message)

    def get_all(self):
        postman = MessageData(self.user_in)
        mine = postman.get_all_mine(self.user_out)
        yours = postman.get_all_yours(self.user_out)
        all_messages = mine + yours
        return sorted(all_messages, key=lambda tup: tup[3])

if __name__ == '__main__':
    manager = MessageManager('клаус', 'jora')
    print (manager.get_all())
