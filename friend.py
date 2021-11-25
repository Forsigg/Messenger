from data.datausersmanager import DataUsersManager

users_data = DataUsersManager()

class Friend():
    friends_list = {}

    def __init__(self):
        pass

    def add_friend(self):
        print ('Введите логин пользователя, которого хотите добавить в друзья:')
        temp_friend = input()
        if users_data.get_one(temp_friend) == False:
            return 'Пользователь с таким логином не найден.'
        else:
            print (f'Как вы хотите записать пользователя {temp_friend} ?')
            friend_name = input()
            self.friends_list[friend_name] = temp_friend.User()
            return f'{friend_name} ({temp_friend}) добавлен в Ваш список друзей.'

    def delete_from_friends(self):
        print ('Введите имя пользователя, которого хотите удалить из списка друзей:')
        temp_del_friend = input()
        if temp_del_friend not in self.friends_list.keys():
            return f'Пользователя с именем "{temp_del_friend} нет в списке ваших друзей."'
        else:
            confirm = input(f'Вы уверены, что хотите удалить пользователя "{temp_del_friend}" c логином "{self.friends_list[temp_del_friend]}" из списка друзей?')
            if confirm.lower() == 'да':
                return f'Пользователь {self.friends_list.pop(temp_del_friend)} был удален из списка друзей.'
