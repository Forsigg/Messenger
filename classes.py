import os
import sys

users_data = {}

class User():
    def __init__(self):
        self.is_log_in = False
        self.is_register()

    def wrapper(self):
        os.system('CLS')
        print ('----------')

    def log_in(self):
        self.wrapper()
        while self.is_log_in == False:
            print ("Пожалуйста, введите данные для идентификации пользователя.")
            temp_login = input('Логин: ')
            temp_pass = input('Пароль: ')

            if temp_login not in users_data:
                print('Такого пользователя не существует. Желаете зарегистрироваться?')
                if input().lower() == 'да':
                    return self.register()
                else:
                    sys.exit()
            if temp_pass != self.password:
                print("Неправильно введен пароль. Попробуйте снова")
            else:
                self.is_log_in = True
                return print(f"Приветствуем, {self.login}!")

    def is_register(self):
        print('Вы уже зарегистрированы? ')
        status = input()
        if status.lower() == 'да':
            self.log_in()
        else:
            self.register()

    def register(self):
        self.wrapper()
        print ('Для регистрации, пожалуйста, введите следующие данные: ')
        self.login = input('Логин: ')
        while True:
            temp_pass = input('Пароль: ')
            conf_temp_pass = input('Повторите пароль: ')
            if temp_pass != conf_temp_pass:
                print ('Пароли не совпадают. Попробуйте снова.')
            else:
                self.password = temp_pass
                break
        print (f'Привет, {self.login}!')
        users_data[self.login] = [self.password,]


class Friend():
    friends_list = {}

    def __init__(self):
        pass

    def add_friend(self):
        print ('Введите логин пользователя, которого хотите добавить в друзья:')
        temp_friend = input()
        if temp_friend not in users_data:
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

class Message:
    def __init__ (self):
        pass

    def send_message(self):
        pass

if __name__ == '__main__':
    user_test = User()
    print (users_data)